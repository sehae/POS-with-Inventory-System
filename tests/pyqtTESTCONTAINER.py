import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, \
    QSizePolicy, QLineEdit
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtCore import Qt
from styles.emailConStyles import EMAIL_TEXTBOX_STYLE, LABEL_STYLE, BUTTON_STYLE


class FullScreenApp(QMainWindow):
    def __init__(self):
        super().__init__()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, '..', 'assets', 'logo1.png')

        self.setWindowTitle("Full Screen PyQt Example")
        self.setGeometry(100, 100, 800, 600)  # Initial dimensions (you can adjust these)
        self.showFullScreen()
        self.setStyleSheet("background-color: white;")  # Set the background color to white

        # Create three frames with different colors
        frame1 = self.create_frame(QColor(0, 255, 255))  # Red
        frame2 = self.create_frame(QColor(255, 0, 255))  # Green
        frame3 = self.create_frame(QColor(255, 255, 0))  # Blue

        # Create a layout to arrange the frames horizontally
        layout = QHBoxLayout()
        layout.addWidget(frame1)
        layout.addWidget(frame2)
        layout.addWidget(frame3)

        # Create a central widget to hold the layout
        central_widget = QFrame(self)
        central_widget.setLayout(layout)

        # Set the central widget
        self.setCentralWidget(central_widget)

        # Add an image above the label in the green frame
        image_label = QLabel(frame2)
        original_pixmap = QPixmap(image_path)  # Replace with your image path
        scaled_pixmap = original_pixmap.scaled(200, 200, Qt.KeepAspectRatio)  # Adjust the size as needed
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        label = QLabel("Enter the e-mail associated with your account and we’ll send you OTP to reset your password.", frame2)
        label.setStyleSheet(LABEL_STYLE)
        label.setWordWrap(True)
        label.setFixedWidth(400)

        label2 = QLabel("E-mail")
        label2.setAlignment(Qt.AlignLeft)
        label2.setStyleSheet(LABEL_STYLE)

        email_textbox = QLineEdit(frame2)
        email_textbox.setPlaceholderText("Enter your email")
        email_textbox.setFixedWidth(400)
        email_textbox.setStyleSheet(EMAIL_TEXTBOX_STYLE)

        button = QPushButton("Confirm", frame2)
        button.clicked.connect(self.on_button_click)
        button.setStyleSheet(BUTTON_STYLE)
        button.setFixedWidth(400)

        label3 = QLabel("If you don’t have an account, please coordinate with your manager for registering an account through admin.")
        label3.setStyleSheet(LABEL_STYLE)
        label3.setWordWrap(True)
        label3.setFixedWidth(400)

        green_layout = QVBoxLayout(frame2)
        green_layout.addWidget(image_label)
        green_layout.addWidget(label)
        green_layout.addWidget(label2)
        green_layout.addWidget(email_textbox, alignment=Qt.AlignCenter)
        green_layout.addWidget(button, alignment=Qt.AlignCenter)
        green_layout.addWidget(label3)
        green_layout.setAlignment(Qt.AlignCenter)

    def create_frame(self, color):
        frame = QFrame(self)
        frame.setStyleSheet(f"background-color: {color.name()}")
        return frame

    def on_button_click(self):
        print("Button clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = FullScreenApp()
    sys.exit(app.exec_())
