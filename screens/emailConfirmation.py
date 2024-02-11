import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, \
    QLineEdit
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtCore import Qt
from styles.emailConStyles import EMAIL_TEXTBOX_STYLE, LABEL_STYLE, BUTTON_STYLE

class FrameWithContent(QFrame):
    def __init__(self, parent=None,
                 color=QColor(255, 255, 255),
                 image_path=None,
                 label_text=None,
                 button_text=None,
                 placeholder_text=None,
                 bellow_button_text=None,
                 ):
        super().__init__(parent)
        self.setStyleSheet(f"background-color: {color.name()}")

        layout = QVBoxLayout(self)

        if image_path:
            self.add_image(layout, image_path)
            layout.addSpacing(50)

        if label_text:
            self.add_label(layout, label_text)
            layout.addSpacing(10)

        if placeholder_text:
            self.add_label2(layout, "E-mail")
            self.add_textbox(layout, placeholder_text)
            layout.addSpacing(20)

        if button_text:
            self.add_button(layout, button_text)
            layout.addSpacing(50)

        if bellow_button_text:
            self.add_label3(layout, bellow_button_text)

        layout.setAlignment(Qt.AlignCenter)

    def add_image(self, layout, image_path):
        image_label = QLabel(self)
        original_pixmap = QPixmap(image_path)
        scaled_pixmap = original_pixmap.scaled(200, 200, Qt.KeepAspectRatio)
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(image_label)

    def add_label(self, layout, text):
        label = QLabel(text, self)
        label.setStyleSheet(LABEL_STYLE)
        label.setWordWrap(True)
        label.setFixedWidth(400)
        layout.addWidget(label)

    def add_label2(self, layout, text):
        label2 = QLabel(text, self)
        label2.setAlignment(Qt.AlignLeft)
        label2.setStyleSheet(LABEL_STYLE)
        layout.addWidget(label2)

    def add_textbox(self, layout, placeholder_text):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText(placeholder_text)
        textbox.setFixedWidth(400)
        textbox.setFixedHeight(46)
        textbox.setStyleSheet(EMAIL_TEXTBOX_STYLE)
        layout.addWidget(textbox)

    def add_button(self, layout, text):
        button = QPushButton(text, self)
        button.clicked.connect(self.on_button_click)
        button.setStyleSheet(BUTTON_STYLE)
        button.setFixedWidth(400)
        button.setFixedHeight(46)
        layout.addWidget(button)

    def add_label3(self, layout, text):
        label3 = QLabel(text, self)
        label3.setStyleSheet(LABEL_STYLE)
        label3.setWordWrap(True)
        label3.setFixedWidth(400)
        layout.addWidget(label3)

    def on_button_click(self):
        print("Button clicked!")

class FullScreenApp(QMainWindow):
    def __init__(self):
        super().__init__()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, '..', 'assets', 'logo1.png')

        self.setGeometry(100, 100, 800, 600)
        self.showFullScreen()
        self.setStyleSheet("background-color: white;")

        # Create three frames with different colors
        frame1 = FrameWithContent(self, QColor(255, 255, 255))
        frame2 = FrameWithContent(self, QColor(255, 255, 255), image_path,
                                  "Enter the e-mail associated with your account and we’ll send you OTP to reset your password.",\
                                  "Continue", "Enter your email",\
                                  "If you don’t have an account, please coordinate with your manager for registering an account through admin.")
        frame3 = FrameWithContent(self, QColor(255, 255, 255))

        layout = QHBoxLayout()
        layout.addWidget(frame1)
        layout.addWidget(frame2)
        layout.addWidget(frame3)

        central_widget = QFrame(self)
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = FullScreenApp()
    sys.exit(app.exec_())
