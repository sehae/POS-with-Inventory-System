from PyQt5 import QtWidgets, QtGui, QtCore
from screens.authentication_screens.login_screen.loginScreen import Ui_MainWindow
from screens.admin_screens.admin_dashboard.adminDashboard_functions import myAdminDashboard
from screens.employee_screens.employee_dashboard.employeeDashboard_functions import myEmployeeDashboard
from shared.dialog import show_error_message
from server.local_server import conn


class myLoginScreen(QtWidgets.QMainWindow):
    login_successful = QtCore.pyqtSignal()
    login_successful_employee = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.admin_dashboard = myAdminDashboard()
        self.employee_dashboard = myEmployeeDashboard()

        self.ui.loginButton.clicked.connect(self.logs)
        self.ui.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.ui.visibilityButton.clicked.connect(self.toggle_password_visibility)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOn.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.visibilityButton.setIcon(icon)


    def toggle_password_visibility(self):
        if self.ui.password.echoMode() == QtWidgets.QLineEdit.Password:
            self.ui.password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.visibilityButton.setIcon(QtGui.QIcon("assets/Icons/visibilityOn.png"))
        else:
            self.ui.password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.visibilityButton.setIcon(QtGui.QIcon("assets/Icons/visibilityOff.png"))

    def logs(self):
        username = self.ui.userName.text()
        password = self.ui.password.text()

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
            self.login_successful.emit()
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
            self.login_successful_employee.emit()
            return

        print("Invalid Credentials")
        show_error_message("Invalid Credentials.")
