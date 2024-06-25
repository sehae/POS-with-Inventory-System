from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow

from database.DB_Queries import CHECK_EMAIL, GET_USER_ID, GET_USERNAME
from maintenance.user_logs import user_log
from screens.authentication_screens.email_screen.emailScreen import Ui_MainWindow
from screens.authentication_screens.otp_screen.otpVerification_functions import OtpVerification
from server.local_server import conn
from validator.otp_validator import send_otp


class EmailScreen(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    email_verified = QtCore.pyqtSignal()

    def __init__(self, otp_screen):
        super().__init__()
        self.setupUi(self)
        self.continueButton.clicked.connect(self.check_email)
        self.backBTN.clicked.connect(self.back)
        self.otp_verification = otp_screen
        self.errorLBL.hide()

    def back(self):
        self.emailTextBox.clear()
        self.back_signal.emit()

    def check_email(self):
        email = self.emailTextBox.text().strip()
        cursor = conn.cursor()

        cursor.execute(CHECK_EMAIL, (email,))
        user = cursor.fetchone()

        if user:
            self.emailTextBox.setStyleSheet("")
            self.errorLBL.hide()
            self.otp_verification.sent_otp, self.otp_verification.sent_time = send_otp(email)
            self.otp_verification.update_email(email)
            self.email_verified.emit()
            self.log_action()
        else:
            self.emailTextBox.setStyleSheet("border: 2px solid red; border-radius: 5px;")
            self.errorLBL.setText("Email not found")
            self.errorLBL.show()

    def log_action(self):
        cursor = conn.cursor()
        email = self.emailTextBox.text().strip()
        cursor.execute(GET_USERNAME, (email,))
        username = cursor.fetchone()[0]
        cursor.execute(GET_USER_ID, (email,))
        user_id = cursor.fetchone()[0]
        cursor.close()

        user_log(user_id, 3, username)
