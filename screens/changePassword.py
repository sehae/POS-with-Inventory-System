import sys
from PyQt5.QtCore import Qt, QDateTime, QTimer
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
)

from styles.universalStyles import HEADER_STYLE


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
        content_label1.setStyleSheet(HEADER_STYLE)
        layout.addWidget(content_label1)

        return frame

    def setupSystemFrame(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setFixedHeight(100)
        layout = QVBoxLayout(frame)

        self.system_time_label = QLabel()
        self.updateTime()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

        layout.addWidget(self.system_time_label)
        return frame

    def updateTime(self):
        current_date_time = QDateTime.currentDateTime().toString("MMMM d, yyyy, hh:mm AP")
        self.system_time_label.setText(current_date_time)

    def setupNavFrame(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setStyleSheet("background-color: red;")
        frame.setFixedWidth(100)

        layout = QHBoxLayout(frame)

        return frame

    def setupContentFrame(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setStyleSheet("background-color: blue;")

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChangePassword()
    sys.exit(app.exec_())
