import os

from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QGraphicsScene, QGraphicsPixmapItem

from modules.maintenance.user_logs import user_log
from modules.reports_and_analysis.generate_sales import save_config, load_config, generate_daily_report, generate_weekly_report, \
    generate_monthly_report, plot_reports, save_report_to_excel, save_report_to_pdf
from screens.admin_screens.admin_reports.report_sales import Ui_MainWindow
from styles.universalStyles import COMBOBOX_STYLE, COMBOBOX_STYLE_VIEW
from validator.user_manager import userManager


class salesReport(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    inventory_report_signal = QtCore.pyqtSignal()
    trend_report_signal = QtCore.pyqtSignal()


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.backBTN.clicked.connect(self.back_signal.emit)
        self.inventoryReportBTN.clicked.connect(self.inventory_report_signal.emit)
        self.trendAnalysisBTN.clicked.connect(self.trend_report_signal.emit)
        self.generateBTN.clicked.connect(self.generate_report)
        self.viewBTN.clicked.connect(self.view_report_location)
        self.selectfolderBTN.clicked.connect(self.selectReportDirectory)

        config = load_config()
        self.directory = config.get('DEFAULT', 'sales_path', fallback=None)
        if self.directory:
            self.filelocDISPLAY.setText(self.directory)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)  # Update every second

        self.UiComponents()

    def UiComponents(self):
        self.frequencyBOX.setStyleSheet(COMBOBOX_STYLE)
        self.frequencyBOX.view().setStyleSheet(COMBOBOX_STYLE_VIEW)

    def updateDateTime(self):
        currentDateTime = QDateTime.currentDateTime()
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")
        self.sysTimeDate.setText(formattedDateTime)

    def selectReportDirectory(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory')

        if directory:
            save_config(directory)
            self.directory = directory
            self.filelocDISPLAY.setText(directory)

    def view_report_location(self):
        try:
            config = load_config()
            sales_path = config.get('DEFAULT', 'sales_path', fallback=None)
            if sales_path:
                print(f"The report location is: {sales_path}")
                os.startfile(sales_path)  # Open the report directory in the file explorer
            else:
                print("No report location has been set.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def generate_report(self):
        if not self.directory:
            QMessageBox.warning(self, "Report Generation Error",
                                "Please select a directory to save the report.")
            return

        frequency = self.frequencyBOX.currentText()
        success = False
        if frequency == "Daily":
            report_data = generate_daily_report()
            plot_reports(report_data, frequency, self.directory)
            save_report_to_excel(report_data, frequency, self.directory)
            save_report_to_pdf(report_data, frequency, self.directory)
            success = True
        elif frequency == "Weekly":
            report_data = generate_weekly_report()
            plot_reports(report_data, frequency, self.directory)
            save_report_to_excel(report_data, frequency, self.directory)
            save_report_to_pdf(report_data, frequency, self.directory)
            success = True
        elif frequency == "Monthly":
            report_data = generate_monthly_report()
            plot_reports(report_data, frequency, self.directory)
            save_report_to_excel(report_data, frequency, self.directory)
            save_report_to_pdf(report_data, frequency, self.directory)
            success = True

        if success:
            QMessageBox.information(self, "Report Generated",
                                    f"{frequency} Sales Report: Successfully generated and saved.")

            user_manager = userManager._instance
            current_id = user_manager.get_current_user_id()
            username = user_manager.get_current_username()
            user_log(current_id, 18, username, f"Sales Report ({frequency})")
        else:
            QMessageBox.warning(self, "Failed", f"Failed to generate {frequency} report.")

        self.displayReport(frequency)

    def displayReport(self, frequency):
        viewer1scene= QGraphicsScene()
        viewer2scene = QGraphicsScene()
        viewer3scene = QGraphicsScene()

        viewer1Pixmap = QPixmap(f'{self.directory}/total_sales_{frequency.lower()}.png')
        viewer2Pixmap = QPixmap(f'{self.directory}/sales_payment_method_{frequency.lower()}.png')
        viewer3Pixmap = QPixmap(f'{self.directory}/sales_category_{frequency.lower()}.png')

        viewer1scene.addItem(QGraphicsPixmapItem(viewer1Pixmap))
        viewer2scene.addItem(QGraphicsPixmapItem(viewer2Pixmap))
        viewer3scene.addItem(QGraphicsPixmapItem(viewer3Pixmap))

        self.viewer1.setScene(viewer1scene)
        self.viewer2.setScene(viewer2scene)
        self.viewer3.setScene(viewer3scene)
