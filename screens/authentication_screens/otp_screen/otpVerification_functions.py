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

        self.supplied_email = None
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
        self.errorLBL.hide()

    def setOTP(self, otp):
        self.sent_otp = otp

    def back(self):
        self.clearField()
        self.cancel_signal.emit()

    def clearField(self):
        self.otp1.clear()
        self.otp2.clear()
        self.otp3.clear()
        self.otp4.clear()
        self.otp5.clear()
        self.otp6.clear()

    def focus_next_field(self, current_field, next_field):
        if len(current_field.text()) == 1:
            next_field.setFocus()

    def update_email(self, email):
        self.supplied_email = email
        self.emailDISPLAY.setText(self.supplied_email)

    def verify_otp(self):
        otp_fields = [self.otp1, self.otp2, self.otp3, self.otp4, self.otp5, self.otp6]
        entered_otp = ''.join(field.text() for field in otp_fields)
        current_time = time.time()

        if current_time - self.sent_time > 180:
            self.errorLBL.setText("OTP expired. Please request a new OTP")
            self.errorLBL.show()
        elif str(entered_otp) == str(self.sent_otp):
            email = self.emailDISPLAY.text()
            try:
                self.otp_verified.emit(email)
                self.clearField()
                self.errorLBL.hide()
                for field in otp_fields:
                    field.setStyleSheet("")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            for field in otp_fields:
                field.setStyleSheet("border: 2px solid red; border-radius: 5px;")
            self.errorLBL.setText("Invalid OTP. Please try again.")
            self.errorLBL.show()

    def resend_otp(self):
        self.resendBTN.setEnabled(False)
        self.resendBTN.setStyleSheet(DISABLED_RESEND_BTN)
        print("Attempting to send OTP to:", self.supplied_email)
        try:
            self.sent_otp, self.sent_time = send_otp(self.supplied_email)
            print("OTP sent successfully")
        except Exception as e:
            print("Error while sending OTP:", e)
        self.resend_timer.start()

    def enable_resend_button(self):
        self.resendBTN.setEnabled(True)
        self.resendBTN.setStyleSheet(ENABLED_RESEND_BTN)
        self.resend_timer.stop()

    def update_timer_label(self):
        current_time = time.time()
        remaining_time = 180 - (current_time - self.sent_time)

        if remaining_time > 0:
            minutes = int(remaining_time // 60)
            seconds = int(remaining_time % 60)
            time_string = f"{minutes}:{seconds:02d}"
        else:
            time_string = "Expired"
            self.enable_resend_button()

        self.timer.setText(time_string)
