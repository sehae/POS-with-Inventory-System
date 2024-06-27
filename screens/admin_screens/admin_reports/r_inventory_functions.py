from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow

from screens.admin_screens.admin_reports.report_inventory import Ui_MainWindow
from modules.reports_and_analysis.generate_inventory import generate_daily_report, generate_weekly_report, generate_monthly_report

class inventoryReport(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    sales_report_signal = QtCore.pyqtSignal()
    inventory_report_signal = QtCore.pyqtSignal()
    trend_report_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dailyBTN.clicked.connect(self.daily_report)
        self.weeklyBTN.clicked.connect(self.weekly_report)
        self.monthlyBTN.clicked.connect(self.monthly_report)

        self.backBTN.clicked.connect(self.back_signal.emit)
        self.salesReportBTN.clicked.connect(self.sales_report_signal.emit)
        self.inventoryReportBTN.clicked.connect(self.inventory_report_signal.emit)
        self.trendAnalysisBTN.clicked.connect(self.trend_report_signal.emit)

    def daily_report(self):
        daily_report = generate_daily_report()
        daily_report.to_excel('daily_inventory_report.xlsx', index=False)
        print("Daily report generated successfully!")

    def weekly_report(self):
        weekly_report = generate_weekly_report()
        weekly_report.to_excel('weekly_inventory_report.xlsx', index=False)
        print("Weekly report generated successfully!")

    def monthly_report(self):
        monthly_report = generate_monthly_report()
        monthly_report.to_excel('monthly_inventory_report.xlsx', index=False)
        print("Monthly report generated successfully!")
