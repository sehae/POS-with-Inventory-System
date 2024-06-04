from PyQt5 import QtWidgets, QtGui
from screens.authentication_screens.login_screen.loginScreen import Ui_MainWindow
from screens.admin_screens.admin_dashboard.adminDashboard_functions import myAdminDashboard
from shared.dialog import show_error_message
from server.local_server import conn


class myLoginScreen(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.admin_dashboard = myAdminDashboard()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.loginButton.clicked.connect(self.logs)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.visibilityButton.clicked.connect(self.toggle_password_visibility)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOn.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.visibilityButton.setIcon(icon)

    def toggle_password_visibility(self):
        if self.password.echoMode() == QtWidgets.QLineEdit.Password:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.visibilityButton.setIcon(QtGui.QIcon("assets/Icons/visibilityOn.png"))
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.visibilityButton.setIcon(QtGui.QIcon("assets/Icons/visibilityOff.png"))

    def logs(self):
        username = self.userName.text()
        password = self.password.text()

        cursor = conn.cursor()
        query1 = "SELECT admin_id FROM adminlogin WHERE username = %s AND password = %s"
        cursor.execute(query1, (username, password))

        result = cursor.fetchone()
        if result is not None:
            admin_id = result[0]
            fetch_query = "SELECT first_name FROM admin WHERE admin_id = %s"
            cursor.execute(fetch_query, (admin_id,))
            admin_first_name = cursor.fetchone()[0]
            print(f"Login successful as admin: Welcome {admin_first_name}!")
            self.admin_dashboard.open_admin_dashboard()
            return

        query2 = "SELECT employee_id FROM employeelogin WHERE username = %s AND password = %s"
        cursor.execute(query2, (username, password))

        result = cursor.fetchone()
        if result is not None:
            employee_id = result[0]
            fetch_query = "SELECT first_name FROM employee WHERE employee_id = %s"
            cursor.execute(fetch_query, (employee_id,))
            employee_first_name = cursor.fetchone()[0]
            print(f"Login successful as Employee: Welcome {employee_first_name}!")

            return

        print("Invalid Credentials")
        show_error_message("Invalid Credentials.")


