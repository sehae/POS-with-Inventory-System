import os.path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QLineEdit, QPushButton
import sys

class emailConfirmation(QMainWindow):
    def __init__(self):
        super().__init__()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, '..', 'assets', 'logo1.png')

        font = QFont("Lato", 12)

        screen_resolution = app.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        self.setFixedSize(width, height)
        self.main_layout = QVBoxLayout(self)

        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(225, 225, Qt.KeepAspectRatio)

        logo = QLabel(self)
        logo.setPixmap(pixmap)
        logo.resize(pixmap.width(), pixmap.height())
        logo.move((width - pixmap.width()) // 2, (height - pixmap.height()) // 4)

        label1 = QLabel("Enter the e-mail associated with your account and we’ll send you OTP to reset your password.", self)
        label1.setAlignment(Qt.AlignCenter)
        label1.setFont(font)

        label1.setGeometry(0, logo.y() + logo.height() + 20, width, 50)

        # Add email label below label1
        email_label = QLabel("Email:", self)
        email_label.setAlignment(Qt.AlignCenter)
        email_label.setFont(font)

        email_label.setGeometry(0, label1.y() + label1.height() + 10, width, 30)

        email_textbox = QLineEdit(self)
        email_textbox.setAlignment(Qt.AlignCenter)
        email_textbox.setFont(font)

        email_textbox.setGeometry((width - 200) // 2, email_label.y() + email_label.height() + 10, 200, 30)

        submit_button = QPushButton("Submit", self)
        submit_button.setFont(font)
        submit_button.setGeometry((width - 100) // 2, email_textbox.y() + email_textbox.height() + 10, 100, 30)

        result_label = QLabel("If you don’t have an account, please coordinate with your manager for registering an account through admin.", self)
        result_label.setAlignment(Qt.AlignCenter)
        result_label.setFont(font)

        result_label.setGeometry(0, submit_button.y() + submit_button.height() + 10, width, 30)

        self.showFullScreen()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = emailConfirmation()
    sys.exit(app.exec_())
