from PyQt5 import QtWidgets
from screens.admin_screens.admin_dashboard.adminDashboard import Ui_MainWindow

from setup.connector import conn

class myAdminDashboard(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

    def open_admin_dashboard(self):
        self.admin_dashboard = QtWidgets.QMainWindow()  # Create a new QMainWindow
        self.setupUi(self.admin_dashboard)  # Call setupUi to setup the admin dashboard
        self.admin_dashboard.show()