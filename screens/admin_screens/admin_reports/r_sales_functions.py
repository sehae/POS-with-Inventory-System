from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.admin_screens.admin_reports.report_sales import Ui_MainWindow


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