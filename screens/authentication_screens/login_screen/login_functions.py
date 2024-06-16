from datetime import datetime

from screens.authentication_screens.login_screen.loginScreen import Ui_MainWindow
from shared.imports import *
from styles.loginStyles import ERROR_LBL_HIDDEN, ERROR_LBL_VISIBLE
from maintenance.user_logs import user_log
from validator.user_manager import userManager

user_manager_instance = userManager()


class myLoginScreen(QMainWindow, Ui_MainWindow):
    login_successful = QtCore.pyqtSignal()
    login_successful_employee = QtCore.pyqtSignal()
    show_email_screen_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # Pass the userManager instance
        self.user_manager = user_manager_instance
        self.user_type = None
        self.user_manager.user_type_updated.connect(self.print_user_type)  # Connect signal to slot

        self.user_action = None
        self.parameter = None
        self.username = None
        self.user_id = None
        self.loginButton.clicked.connect(self.logs)
        self.visibilityButton.clicked.connect(self.toggle_password_visibility)
        self.forgotButton.clicked.connect(self.show_email_screen)
        self.UiComponents()

    def UiComponents(self):
        self.errorLBL.setStyleSheet(ERROR_LBL_HIDDEN)
        icon = QtGui.QIcon()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOff.png"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOn.png"), QIcon.Normal, QIcon.On)
        self.visibilityButton.setIcon(icon)

    def print_user_type(self, user_type):
        print(f"MYLOGINSCREEN: User type set to: {user_type}")

    def show_email_screen(self):
        self.show_email_screen_signal.emit()

    def toggle_password_visibility(self):
        if self.password.echoMode() == QtWidgets.QLineEdit.Password:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.visibilityButton.setIcon(QtGui.QIcon("assets/Icons/visibilityOn.png"))
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.visibilityButton.setIcon(QtGui.QIcon("assets/Icons/visibilityOff.png"))

    def logs(self):
        username = self.userName.text()
        provided_password = self.password.text()
        login_action = 2
        failed_login_action = 1

        try:
            cursor = conn.cursor()

            # Query the adminlogin table
            cursor.execute(GET_ADMIN_LOGIN, (username,))
            result = cursor.fetchone()

            if result:
                admin_id, stored_password, is_active = result

                # Verify the provided password against the stored password
                if verify_password(stored_password, provided_password):
                    if is_active:
                        cursor.execute(GET_ADMIN_FIRST_NAME, (admin_id,))
                        admin_first_name = cursor.fetchone()[0]
                        print(f"Login successful as admin: Welcome {admin_first_name}!")
                        cursor.execute(GET_ADMIN_LAST_NAME, (admin_id,))
                        admin_last_name = cursor.fetchone()[0]
                        admin_full_name = f"{admin_first_name} {admin_last_name}"
                        print(f"Login successful as admin: Welcome {admin_full_name}!")
                        self.user_type = "admin"
                        user_log(admin_id, login_action, self.user_type, username)
                        self.user_manager.set_user_type(self.user_type)  # Update user type in userManager
                        self.user_manager.set_current_username(username)  # Update current username in userManager
                        self.user_manager.set_current_fullname(admin_full_name)  # Update current full name in userManager
                        self.login_successful.emit()
                        return
                    else:
                        self.disabledAcc()
                        return
                else:
                    print("Incorrect password.")
                    self.user_type = "system"
                    user_log(admin_id, failed_login_action, self.user_type, username)
                    self.invalidCredentials()

            # Query the employeelogin table
            cursor.execute(GET_EMPLOYEE_LOGIN, (username,))
            result = cursor.fetchone()

            if result:
                employee_id, stored_password, is_active = result

                # Verify the provided password against the stored password
                if verify_password(stored_password, provided_password):
                    if is_active:
                        cursor.execute(GET_EMPLOYEE_FIRST_NAME, (employee_id,))
                        employee_first_name = cursor.fetchone()[0]
                        print(f"Login successful as Employee: Welcome {employee_first_name}!")
                        cursor.execute(GET_EMPLOYEE_LAST_NAME, (employee_id,))
                        employee_last_name = cursor.fetchone()[0]
                        employee_full_name = f"{employee_first_name} {employee_last_name}"
                        print(f"Login successful as Employee: Welcome {employee_full_name}!")
                        self.user_type = "employee"
                        user_log(employee_id, login_action, self.user_type, username)
                        self.user_manager.set_user_type(self.user_type)  # Update user type in userManager
                        self.user_manager.set_current_username(username)  # Update current username in userManager
                        self.user_manager.set_current_fullname(employee_full_name)  # Update current full name in userManager
                        self.login_successful_employee.emit()
                        return
                    else:
                        self.disabledAcc()
                        return
                else:
                    print("Incorrect password.")
                    self.user_type = "system"
                    user_log(employee_id, failed_login_action, self.user_type, username)
                    self.invalidCredentials()

            print("Invalid Credentials")
            self.invalidCredentials()

        except Exception as e:
            print(f"An error occurred during login: {e}")
            show_error_message("Error", f"An error occurred during login: {e}")
        finally:
            cursor.close()

    def disabledAcc(self):
        self.errorLBL.setText("There's no account with that username.")
        self.errorLBL.setStyleSheet(ERROR_LBL_VISIBLE)

    def invalidCredentials(self):
        self.errorLBL.setText("Invalid Credentials. Check your username and password.")
        self.errorLBL.setStyleSheet(ERROR_LBL_VISIBLE)