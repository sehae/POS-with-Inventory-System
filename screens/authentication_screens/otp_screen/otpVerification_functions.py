import time

from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from screens.authentication_screens.otp_screen.otpVerification import Ui_MainWindow
from screens.authentication_screens.password_recovery.pwRecovery_functions import PasswordRecovery
from styles.universalStyles import DISABLED_RESEND_BTN, ENABLED_RESEND_BTN
from validator.otp_validator import send_otp


class OtpVerification(QMainWindow, Ui_MainWindow):
    cancel_signal = pyqtSignal()
    otp_verified = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sent_otp = None
        self.sent_time = time.time()
        self.resend_timer = QTimer()
        self.resend_timer.setInterval(1000)
        self.resend_timer.timeout.connect(self.update_timer_label)
        self.resend_timer.start()
        self.password_recovery = None
        self.password_recovery_window = None

        self.submitButton.clicked.connect(self.verify_otp)
        self.resendBTN.clicked.connect(self.resend_otp)
        self.cancelBTN.clicked.connect(self.back)

        self.otp1.textChanged.connect(lambda: self.focus_next_field(self.otp1, self.otp2))
        self.otp2.textChanged.connect(lambda: self.focus_next_field(self.otp2, self.otp3))
        self.otp3.textChanged.connect(lambda: self.focus_next_field(self.otp3, self.otp4))
        self.otp4.textChanged.connect(lambda: self.focus_next_field(self.otp4, self.otp5))
        self.otp5.textChanged.connect(lambda: self.focus_next_field(self.otp5, self.otp6))
        self.resendBTN.setEnabled(False)
        self.resendBTN.setStyleSheet(DISABLED_RESEND_BTN)

    def back(self):
        self.cancel_signal.emit()

    def focus_next_field(self, current_field, next_field):
        if len(current_field.text()) == 1:
            next_field.setFocus()

    def update_email(self, email):
        self.emailDISPLAY.setText(email)

    def verify_otp(self):
        entered_otp = self.otp1.text() + self.otp2.text() + self.otp3.text() + self.otp4.text() + self.otp5.text() + self.otp6.text()
        current_time = time.time()

        if current_time - self.sent_time > 300:
            print("OTP expired")
        elif str(entered_otp) == str(self.sent_otp):
            print("OTP verification successful")
            email = self.emailDISPLAY.text()
            try:
                self.otp_verified.emit(email)
                # self.password_recovery = PasswordRecovery(email)
                # self.password_recovery_window = QMainWindow()
                # self.password_recovery.setupUi(self.password_recovery_window)
                # self.password_recovery_window.show()
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Incorrect OTP")

    def resend_otp(self):
        self.resendBTN.setEnabled(False)
        self.resendBTN.setStyleSheet(DISABLED_RESEND_BTN)
        self.sent_otp, self.sent_time = send_otp(self.to_email)
        self.resend_timer.start()

    def enable_resend_button(self):
        self.resendBTN.setEnabled(True)
        self.resendBTN.setStyleSheet(ENABLED_RESEND_BTN)
        self.resend_timer.stop()

    def update_timer_label(self):
        current_time = time.time()
        remaining_time = 300 - (current_time - self.sent_time)

        if remaining_time > 0:
            minutes = int(remaining_time // 60)
            seconds = int(remaining_time % 60)
            time_string = f"{minutes}:{seconds:02d}"
        else:
            time_string = "Expired"
            self.enable_resend_button()

        self.timer.setText(time_string)

