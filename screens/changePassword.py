import sys
from PyQt5.QtCore import Qt, QDateTime, QTimer, QSize
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QLabel,
    QScrollArea,
    QSizePolicy,
    QPushButton,
)
from PyQt5.QtGui import QFontDatabase, QFont

from assets.assetsDIR import get_navbar_button_icon
from styles.universalStyles import HEADER_TITLE, SYSTEM_LABEL, NAVBAR_BUTTON_STYLE

# Icons
icon = get_navbar_button_icon()

class ChangePasswordUI(QWidget):
    def __init__(self):
        super().__init__()

        # Header Contents
        self.frame1 = self.setupTitleFrame()
        self.frame2 = self.setupSystemFrame()

        # Body Contents
        self.frame3 = self.setupNavFrame()
        self.frame4 = self.setupContentFrame()

        main_layout = QVBoxLayout(self)
        header_layout = QHBoxLayout()
        container_layout = QHBoxLayout()

        header_layout.addWidget(self.frame1)
        header_layout.addWidget(self.frame2)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.addWidget(self.frame4)
        content_layout.setAlignment(Qt.AlignTop)

        scroll_area.setWidget(content_widget)

        container_layout.addWidget(self.frame3)
        container_layout.addWidget(scroll_area)

        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setAlignment(Qt.AlignLeft)

        main_layout.addLayout(header_layout)
        main_layout.addLayout(container_layout)

    def setupTitleFrame(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setFixedHeight(100)
        layout = QHBoxLayout(frame)

        content_label1 = QLabel("CHANGE PASSWORD")
        content_label1.setStyleSheet(HEADER_TITLE)
        content_label1.setFont(QFont("Quicksand"))

        layout.addWidget(content_label1)

        return frame

    def setupSystemFrame(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setFixedHeight(100)
        layout = QVBoxLayout(frame)
        layout.setAlignment(Qt.AlignRight| Qt.AlignCenter)

        self.system_time_label = QLabel()
        self.system_time_label.setStyleSheet(SYSTEM_LABEL)
        self.updateTime()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

        layout.addWidget(self.system_time_label)

        if hasattr(self, 'system_time_label'):
            username = QLabel("User's Name Placeholder")
            username.setStyleSheet(SYSTEM_LABEL)

            layout.addWidget(username, alignment=Qt.AlignRight)


        return frame

    def updateTime(self):
        current_date_time = QDateTime.currentDateTime().toString("MMMM d, yyyy, hh:mm AP")
        self.system_time_label.setText(current_date_time)

    def setupNavFrame(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setFixedWidth(115)
        layout = QVBoxLayout(frame)
        layout.setAlignment(Qt.AlignLeft | Qt.AlignCenter)

        button1 = QPushButton("CHANGE PASS")
        button1.setStyleSheet(NAVBAR_BUTTON_STYLE)
        button1.setIcon(icon)
        button1.setIconSize(icon.actualSize(QSize(40, 40)))
        button1.setFixedSize(96, 109)
        button2 = QPushButton("BACK")
        button2.setFixedSize(96, 109)
        button2.setStyleSheet(NAVBAR_BUTTON_STYLE)

        layout.addWidget(button1, alignment=Qt.AlignLeft)
        layout.addWidget(button2, alignment=Qt.AlignLeft)

        #layout.setSpacing(0)

        return frame

    def setupContentFrame(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)

        layout = QVBoxLayout(frame)

        for i in range(20):
            label = QLabel(f"Content {i}")
            layout.addWidget(label)

        frame.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        return frame

class ChangePassword(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 600)
        self.showFullScreen()

        self.ui = ChangePasswordUI()
        self.setCentralWidget(self.ui)

    def updateContentFrame(self, content):
        self.ui.updateContentFrame(content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChangePassword()
    sys.exit(app.exec_())