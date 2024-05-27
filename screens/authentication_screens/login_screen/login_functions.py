from PyQt5 import QtWidgets
from screens.authentication_screens.login_screen.loginScreen import Ui_MainWindow
from screens.admin_screens.admin_dashboard.adminDashboard_functions import myAdminDashboard

from setup.connector import conn


class myLoginScreen(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.admin_dashboard = myAdminDashboard()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.loginButton.clicked.connect(self.logs)

    def logs(self):
        username = self.userName.text()
        password = self.password.text()

        cursor = conn.cursor()
        query1 = "SELECT * FROM adminlogin WHERE username = %s AND password = %s"
        cursor.execute(query1, (username, password))

        if cursor.fetchone() is not None:
            print("Login successful as admin")
            self.admin_dashboard.open_admin_dashboard()
            return

        query2 = "SELECT * FROM employeelogin WHERE username = %s AND password = %s"
        cursor.execute(query2, (username, password))

        if cursor.fetchone() is not None:
            print("Login successful as Employee")
            return

        print("Invalid Credentials")
