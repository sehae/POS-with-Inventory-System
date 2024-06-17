from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow

from screens.authentication_screens.email_screen.emailScreen import Ui_MainWindow
from screens.authentication_screens.otp_screen.otpVerification_functions import OtpVerification
from server.local_server import conn
from validator.otp_validator import send_otp


class EmailScreen(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    email_verified = QtCore.pyqtSignal()

    def __init__(self, otp_screen):
        super().__init__()
        print("EmailScreen initialized")
        self.setupUi(self)
        self.continueButton.clicked.connect(self.check_email)
        self.backBTN.clicked.connect(self.back)
        self.otp_verification = otp_screen

    def back(self):
        self.emailTextBox.clear()
        self.back_signal.emit()

    def check_email(self):
        email = self.emailTextBox.text()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT email FROM employee WHERE email = %s UNION SELECT email FROM admin WHERE email = %s",
            (email, email)
        )
        user = cursor.fetchone()

        if user:
            print("Email found")
            self.otp_verification.sent_otp, self.otp_verification.sent_time = send_otp(email)
            self.otp_verification.update_email(email)
            self.email_verified.emit()
        else:
            print("Email not found")
