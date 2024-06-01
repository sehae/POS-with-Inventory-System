from PyQt5.QtWidgets import QMainWindow

from screens.authentication_screens.email_screen.emailScreen import Ui_MainWindow
from screens.authentication_screens.otp_screen.otpVerification_functions import OtpVerification
from setup.connector import conn
from validator.otp_validator import send_otp


class EmailScreen(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.continueButton.clicked.connect(self.check_email)

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
            otp_verification = OtpVerification()
            self.otp_window = QMainWindow()
            otp_verification.setupUi(self.otp_window)
            otp_verification.sent_otp, otp_verification.sent_time = send_otp(email)
            self.otp_window.show()
            otp_verification.update_email(email)

        else:
            print("Email not found")
