from PyQt5 import QtWidgets
from screens.authentication_screens.login_screen.loginScreen import Ui_MainWindow

from PyQt5.QtWidgets import QMessageBox
from setup.connector import conn

class CustomLoginScreen(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.loginButton.clicked.connect(self.logs)

    def logs(self):
        username = self.userName.text()
        password = self.password.text()

        cursor = conn.cursor()
        query = "SELECT * FROM adminlogin WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))

        if cursor.fetchone() is not None:
            print("Login successful")
        else:
            print("Invalid Credentials")
