from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction

from database.DB_Queries import GET_ADMIN_PASSWORD, GET_EMPLOYEE_PASSWORD, UPDATE_ADMIN_PASSWORD, \
    UPDATE_EMPLOYEE_PASSWORD
from security.hash import hash_password, verify_password
from shared.dialog import show_error_message
from shared.navigation_signal import auth_back
from validator.password_validator import isValidPassword
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, QTimer, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from screens.password_screen.changePassword import Ui_MainWindow
from server.local_server import conn
from validator.user_manager import userManager


class changePassword(QMainWindow, Ui_MainWindow):
    back_signal = pyqtSignal()
    back_employee_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.user_manager = userManager()
        self.user_manager.username_updated.connect(self.on_username_updated)
        self.backBTN.clicked.connect(lambda: auth_back(self.user_manager, self.back_signal, self.back_employee_signal))

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        self.check_action = None
        self.saveBTN.clicked.connect(self.change_password)
        self.cp_visibility.clicked.connect(lambda: self.toggle_visibility(self.currentPassFIELD, self.cp_visibility))
        self.np_visibility.clicked.connect(lambda: self.toggle_visibility(self.newPassFIELD, self.np_visibility))
        self.rp_visibility.clicked.connect(lambda: self.toggle_visibility(self.retypeFIELD, self.rp_visibility))

        self.UiComponents()

    def on_username_updated(self, username):
        self.usernameFIELD.setText(username)

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.sysTimeDate.setText(formattedDateTime)

    def UiComponents(self):
        self.currentPassFIELD.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPassFIELD.setEchoMode(QtWidgets.QLineEdit.Password)
        self.retypeFIELD.setEchoMode(QtWidgets.QLineEdit.Password)
        self.usernameFIELD.setReadOnly(True)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOff.png"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOn.png"), QIcon.Normal, QIcon.On)
        self.cp_visibility.setIcon(icon)
        self.np_visibility.setIcon(icon)
        self.rp_visibility.setIcon(icon)

    def toggle_visibility(self, field, button):
        if field.echoMode() == QtWidgets.QLineEdit.Password:
            field.setEchoMode(QtWidgets.QLineEdit.Normal)
            button.setIcon(QtGui.QIcon("assets/Icons/visibilityOn.png"))
        else:
            field.setEchoMode(QtWidgets.QLineEdit.Password)
            button.setIcon(QtGui.QIcon("assets/Icons/visibilityOff.png"))

    def check_password_match(self):
        if self.newPassFIELD.text() == self.retypeFIELD.text():
            check_icon = QIcon("assets/Icons/check.png")
            self.check_action = QAction(check_icon, "Passwords Match", self.newPassFIELD)

            self.newPassFIELD.addAction(self.check_action, QtWidgets.QLineEdit.TrailingPosition)
            self.retypeFIELD.addAction(self.check_action, QtWidgets.QLineEdit.TrailingPosition)
        else:
            if self.check_action:
                self.newPassFIELD.removeAction(self.check_action)
                self.retypeFIELD.removeAction(self.check_action)

    def change_password(self):
        username = self.usernameFIELD.text()
        current_password = self.currentPassFIELD.text()
        new_password = self.newPassFIELD.text()
        retype_password = self.retypeFIELD.text()
        is_valid = isValidPassword(new_password)

        if not username or not current_password or not new_password or not retype_password:
            show_error_message("Error", "All fields must be filled. Please fill in the fields before changing your "
                                        "password.")
            return

        if new_password != retype_password:
            show_error_message("Error", "Passwords do not match. Please retype your new password.")
            return

        if new_password == current_password:
            show_error_message("Error", "New password must be different from your current password.")
            return

        if new_password == retype_password:
            if not isValidPassword(new_password):
                return

        hashed_new_password = hash_password(new_password)
        cursor = conn.cursor()

        user_type = self.user_manager.get_user_type()
        if user_type == 'admin':
            print(username)
            cursor.execute(GET_ADMIN_PASSWORD, (username,))
        elif user_type == 'employee':
            cursor.execute(GET_EMPLOYEE_PASSWORD, (username,))
        else:
            show_error_message("Error", "Invalid user type.")
            return

        stored_hashed_password = cursor.fetchone()[0]

        if verify_password(stored_hashed_password, current_password):
            print("Password is valid.")
            if is_valid:
                if user_type == 'admin':
                    cursor.execute(UPDATE_ADMIN_PASSWORD, (hashed_new_password, username))
                elif user_type == 'employee':
                    cursor.execute(UPDATE_EMPLOYEE_PASSWORD, (hashed_new_password, username))
                else:
                    show_error_message("Error", "Invalid user type.")
                    return
            else:
                print("The password is invalid.")
        else:
            show_error_message("Error", "Incorrect current password.")
            return

        conn.commit()
        show_error_message("Success", "Password changed successfully.")
        self.currentPassFIELD.clear()
        self.newPassFIELD.clear()
        self.retypeFIELD.clear()

        return