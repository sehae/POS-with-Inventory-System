import os
from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QGraphicsPixmapItem, QGraphicsScene

from modules.maintenance.user_logs import user_log
from modules.reports_and_analysis.generate_trend import load_config, save_config, analyze_avg_guest_pax, \
    analyze_preferred_soup_variations, analyze_best_selling_product, save_report_to_word, generate_daily_report, \
    generate_weekly_report, generate_monthly_report
from screens.admin_screens.admin_reports.report_trend import Ui_MainWindow
from styles.universalStyles import COMBOBOX_STYLE, COMBOBOX_STYLE_VIEW
from validator.user_manager import userManager


class trendReport(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    sales_report_signal = QtCore.pyqtSignal()
    inventory_report_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.backBTN.clicked.connect(self.back_signal.emit)
        self.salesReportBTN.clicked.connect(self.sales_report_signal.emit)
        self.inventoryReportBTN.clicked.connect(self.inventory_report_signal.emit)
        self.generateBTN.clicked.connect(self.generate_report)
        self.viewBTN.clicked.connect(self.view_report_location)
        self.selectfolderBTN.clicked.connect(self.selectReportDirectory)

        config = load_config()
        self.directory = config.get('DEFAULT', 'trend_path', fallback=None)
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
            trend_path = config.get('DEFAULT', 'trend_path', fallback=None)
            if trend_path:
                print(f"The report location is: {trend_path}")
                os.startfile(trend_path)  # Open the report directory in the file explorer
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
            dataframe = generate_daily_report()
        elif frequency == "Weekly":
            dataframe = generate_weekly_report()
        elif frequency == "Monthly":
            dataframe = generate_monthly_report()

        avg_guest_pax = analyze_avg_guest_pax(dataframe, frequency.lower())
        preferred_soup_variations = analyze_preferred_soup_variations(dataframe, frequency.lower())
        best_selling_product = analyze_best_selling_product(dataframe, frequency.lower())

        # Add check for empty dataframe before plotting
        if best_selling_product.empty:
            print(f"No data available for best selling product for {frequency.lower()} frequency.")
        else:
            # Generate and save report
            save_report_to_word(dataframe, frequency, self.directory, avg_guest_pax, preferred_soup_variations,
                                best_selling_product)
            success = True

        if success:
            print("Report generated successfully.")

            # Optional: Display a message box or update UI to notify the user
            QMessageBox.information(self, "Report Generated",
                                    f"{frequency} Trend Report: Successfully generated and saved.")

            user_manager = userManager._instance
            current_id = user_manager.get_current_user_id()
            username = user_manager.get_current_username()
            user_log(current_id, 18, username, f"Trend Report ({frequency})")
        else:
            QMessageBox.warning(self, "Failed", f"Failed to generate {frequency} report.")

        self.displayReport(frequency)

    def displayReport(self, frequency):
        viewer1scene = QGraphicsScene()
        viewer2scene = QGraphicsScene()

        viewer1Pixmap = QPixmap(f'{self.directory}/preferred_soup_{frequency.lower()}.png')
        viewer2Pixmap = QPixmap(f'{self.directory}/best_selling_product_{frequency.lower()}.png')

        viewer1scene.addPixmap(viewer1Pixmap)
        viewer2scene.addPixmap(viewer2Pixmap)

        self.viewer1.setScene(viewer1scene)
        self.viewer2.setScene(viewer2scene)
