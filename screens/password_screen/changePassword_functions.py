from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, QTimer, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMainWindow

from database.DB_Queries import GET_PASSWORD, UPDATE_PASSWORD_BY_USERNAME
from modules.maintenance.user_logs import user_log
from screens.password_screen.changePassword import Ui_MainWindow
from modules.security.hash import hash_password, verify_password
from server.local_server import conn
from shared.dialog import show_error_message, create_dialog_box
from shared.navigation_signal import auth_back
from styles.universalStyles import INVALID_FIELD_STYLE_WITH_ICON, INVALID_FIELD_STYLE_WITH_ICON_RIGHT, \
    VALID_FIELD_STYLE_WITH_ICON, VALID_FIELD_STYLE_WITH_ICON_RIGHT
from validator.password_validator import isValidPassword
from validator.user_manager import userManager


class changePassword(QMainWindow, Ui_MainWindow):
    back_signal = pyqtSignal()
    back_cashier_signal = pyqtSignal()
    back_kitchen_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.user_manager = userManager()

        self.backBTN.clicked.connect(lambda: auth_back(self.user_manager, self.back_signal, self.back_cashier_signal, self.back_kitchen_signal))

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        self.check_action = None
        self.saveBTN.clicked.connect(self.change_password)
        self.cancelBTN.clicked.connect(self.cancel)
        self.cp_visibility.clicked.connect(lambda: self.toggle_visibility(self.currentPassFIELD, self.cp_visibility))
        self.np_visibility.clicked.connect(lambda: self.toggle_visibility(self.newPassFIELD, self.np_visibility))
        self.rp_visibility.clicked.connect(lambda: self.toggle_visibility(self.retypeFIELD, self.rp_visibility))

        self.UiComponents()

    def on_username_updated(self, username):
        self.unFIELD.setText(username)

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.sysTimeDate.setText(formattedDateTime)

        username = self.user_manager.get_current_username()
        self.on_username_updated(username)

    def UiComponents(self):
        self.currentPassFIELD.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPassFIELD.setEchoMode(QtWidgets.QLineEdit.Password)
        self.retypeFIELD.setEchoMode(QtWidgets.QLineEdit.Password)
        self.unFIELD.setReadOnly(True)

        # Connect the check_password_match method to the textChanged events of the password fields
        self.newPassFIELD.textChanged.connect(self.check_password_match)
        self.retypeFIELD.textChanged.connect(self.check_password_match)

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
        new_password = self.newPassFIELD.text().strip()
        retype_password = self.retypeFIELD.text().strip()

        # Ensure both fields are not empty and match each other
        if new_password and retype_password and new_password == retype_password:
            check_icon = QIcon("assets/Icons/check.png")
            self.check_action = QAction(check_icon, "Passwords Match", self.newPassFIELD)
            self.newPassFIELD.addAction(self.check_action, QtWidgets.QLineEdit.TrailingPosition)
            self.retypeFIELD.addAction(self.check_action, QtWidgets.QLineEdit.TrailingPosition)
        else:
            if hasattr(self, 'check_action') and self.check_action:
                self.newPassFIELD.removeAction(self.check_action)
                self.retypeFIELD.removeAction(self.check_action)
                self.check_action = None  # Reset the check_action attribute

    def change_password(self):
        username = self.usernameFIELD.text().strip()
        current_password = self.currentPassFIELD.text().strip()
        new_password = self.newPassFIELD.text().strip()
        retype_password = self.retypeFIELD.text().strip()
        is_valid = isValidPassword(new_password)

        all_fields_valid = True

        # Validate current password
        if not current_password:
            self.currentPassFIELD.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON)
            self.cp_visibility.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON_RIGHT)
            all_fields_valid = False
        else:
            self.currentPassFIELD.setStyleSheet(VALID_FIELD_STYLE_WITH_ICON)
            self.cp_visibility.setStyleSheet(VALID_FIELD_STYLE_WITH_ICON_RIGHT)

        # Validate new password
        if not new_password:
            self.newPassFIELD.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON)
            self.np_visibility.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON_RIGHT)
            all_fields_valid = False
        else:
            self.newPassFIELD.setStyleSheet(VALID_FIELD_STYLE_WITH_ICON)
            self.np_visibility.setStyleSheet(VALID_FIELD_STYLE_WITH_ICON_RIGHT)

        # Validate retype password
        if not retype_password:
            self.retypeFIELD.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON)
            self.rp_visibility.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON_RIGHT)
            all_fields_valid = False
        else:
            self.retypeFIELD.setStyleSheet(VALID_FIELD_STYLE_WITH_ICON)
            self.rp_visibility.setStyleSheet(VALID_FIELD_STYLE_WITH_ICON_RIGHT)

        # Check if passwords match
        self.check_password_match()

        if not all_fields_valid:
            return

        if new_password != retype_password:
            show_error_message("Error", "Passwords do not match. Please retype your new password.")
            self.newPassFIELD.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON)
            self.np_visibility.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON_RIGHT)
            self.retypeFIELD.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON)
            self.rp_visibility.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON_RIGHT)
            return

        if new_password == current_password:
            show_error_message("Error", "New password must be different from your current password.")
            self.newPassFIELD.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON)
            self.np_visibility.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON_RIGHT)
            self.retypeFIELD.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON)
            self.rp_visibility.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON_RIGHT)
            return

        if not is_valid:
            show_error_message("Error", "New password does not meet the required criteria.")
            self.newPassFIELD.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON)
            self.np_visibility.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON_RIGHT)
            self.retypeFIELD.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON)
            self.rp_visibility.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON_RIGHT)
            return

        hashed_new_password = hash_password(new_password)
        cursor = conn.cursor()

        cursor.execute(GET_PASSWORD, (username,))
        stored_hashed_password = cursor.fetchone()[0]

        if verify_password(stored_hashed_password, current_password):
            cursor.execute(UPDATE_PASSWORD_BY_USERNAME, (hashed_new_password, username))
        else:
            show_error_message("Error", "Incorrect current password.")
            self.currentPassFIELD.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON)
            self.cp_visibility.setStyleSheet(INVALID_FIELD_STYLE_WITH_ICON_RIGHT)
            return

        conn.commit()
        create_dialog_box("Password changed successfully.", "Success")
        self.currentPassFIELD.clear()
        self.newPassFIELD.clear()
        self.retypeFIELD.clear()

        if hasattr(self, 'check_action') and self.check_action:
            self.newPassFIELD.removeAction(self.check_action)
            self.retypeFIELD.removeAction(self.check_action)
            self.check_action = None

        self.log_action()
        cursor.close()

    def cancel(self):
        self.currentPassFIELD.clear()
        self.newPassFIELD.clear()
        self.retypeFIELD.clear()
        self.currentPassFIELD.setStyleSheet(VALID_FIELD_STYLE_WITH_ICON)
        self.newPassFIELD.setStyleSheet(VALID_FIELD_STYLE_WITH_ICON)
        self.retypeFIELD.setStyleSheet(VALID_FIELD_STYLE_WITH_ICON)
        self.cp_visibility.setStyleSheet(VALID_FIELD_STYLE_WITH_ICON_RIGHT)
        self.np_visibility.setStyleSheet(VALID_FIELD_STYLE_WITH_ICON_RIGHT)
        self.rp_visibility.setStyleSheet(VALID_FIELD_STYLE_WITH_ICON_RIGHT)

        if hasattr(self, 'check_action') and self.check_action:
            self.newPassFIELD.removeAction(self.check_action)
            self.retypeFIELD.removeAction(self.check_action)
            self.check_action = None

    def log_action(self):
        user_id = self.user_manager.get_current_user_id()
        user_action = 12
        username = self.user_manager.get_current_username()
        user_log(user_id, user_action, username)
