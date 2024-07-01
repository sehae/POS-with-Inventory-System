import os

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import QMainWindow, QGraphicsPixmapItem, QGraphicsScene, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap

from modules.reports_and_analysis.generate_inventory import save_config, save_report_to_word
from screens.admin_screens.admin_reports.report_inventory import Ui_MainWindow
from modules.reports_and_analysis.generate_inventory import generate_daily_report, generate_weekly_report, \
    generate_monthly_report, plot_reports, save_report_to_excel, load_config
from styles.universalStyles import COMBOBOX_STYLE, COMBOBOX_STYLE_VIEW


class inventoryReport(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    sales_report_signal = QtCore.pyqtSignal()
    trend_report_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.backBTN.clicked.connect(self.back_signal.emit)
        self.salesReportBTN.clicked.connect(self.sales_report_signal.emit)
        self.trendAnalysisBTN.clicked.connect(self.trend_report_signal.emit)
        self.selectfolderBTN.clicked.connect(self.selectReportDirectory)
        self.viewBTN.clicked.connect(self.view_report_location)

        config = load_config()
        self.directory = config.get('DEFAULT', 'report_path', fallback=None)
        if self.directory:
            self.filelocDISPLAY.setText(self.directory)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)  # Update every second

        self.UIComponents()

    def UIComponents(self):
        self.frequencyBOX.setStyleSheet(COMBOBOX_STYLE)
        self.frequencyBOX.view().setStyleSheet(COMBOBOX_STYLE_VIEW)
        self.generateBTN.clicked.connect(self.generateReport)

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
            report_path = config.get('DEFAULT', 'report_path', fallback=None)
            if report_path:
                print(f"The report location is: {report_path}")
                os.startfile(report_path)  # Open the report directory in the file explorer
            else:
                print("No report location has been set.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def generateReport(self):
        if not self.directory:
            # If no directory is selected, show a warning message or handle the case accordingly
            print("Please select a directory to save the reports.")
            return

        frequency = self.frequencyBOX.currentText()
        success = False
        if frequency == "Daily":
            report_data = generate_daily_report()
            plot_reports(report_data, 'Daily', self.directory)
            save_report_to_excel(report_data, 'Daily', self.directory)
            save_report_to_word(report_data, 'Daily', self.directory)
            success = True
        elif frequency == "Weekly":
            report_data = generate_weekly_report()
            plot_reports(report_data, 'Weekly', self.directory)
            save_report_to_excel(report_data, 'Weekly', self.directory)
            save_report_to_word(report_data, 'Weekly', self.directory)
            success = True
        elif frequency == "Monthly":
            report_data = generate_monthly_report()
            plot_reports(report_data, 'Monthly', self.directory)
            save_report_to_excel(report_data, 'Monthly', self.directory)
            save_report_to_word(report_data, 'Monthly', self.directory)
            success = True

        if success:
            QMessageBox.information(self, "Success", f"{frequency.capitalize()} report has been generated and saved to '{self.directory}'")

        self.displayReport(frequency)

    def displayReport(self, frequency):
        levelViewScene = QGraphicsScene()
        statusViewScene = QGraphicsScene()
        expiryViewScene = QGraphicsScene()

        levelViewPixmap = QPixmap(f'{self.directory}/inventory_levels_{frequency.lower()}.png')
        statusViewPixmap = QPixmap(f'{self.directory}/inventory_status_{frequency.lower()}.png')
        expiryViewPixmap = QPixmap(f'{self.directory}/expiry_date_time_series_{frequency.lower()}.png')

        levelViewScene.addItem(QGraphicsPixmapItem(levelViewPixmap))
        statusViewScene.addItem(QGraphicsPixmapItem(statusViewPixmap))
        expiryViewScene.addItem(QGraphicsPixmapItem(expiryViewPixmap))

        self.levelView.setScene(levelViewScene)
        self.statusView.setScene(statusViewScene)
        self.expiryView.setScene(expiryViewScene)

