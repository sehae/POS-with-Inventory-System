import os
from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from modules.reports_and_analysis.generate_trend import load_config, save_config, generate_report, dataframe
from screens.admin_screens.admin_reports.report_trend import Ui_MainWindow
from styles.universalStyles import COMBOBOX_STYLE, COMBOBOX_STYLE_VIEW


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
            print("Please select a directory to save the report.")
            return

        frequency = self.frequencyBOX.currentText()
        try:
            generate_report(dataframe, frequency, self.directory)
            QMessageBox.information(self, "Success",
                                    f"{frequency.capitalize()} report has been generated and saved to '{self.directory}'")
        except Exception as e:
            print(f"An error occurred: {e}")

        self.displayReport(frequency)

    def displayReport(self, frequency):
        # Logic to display the generated report, if needed
        pass
