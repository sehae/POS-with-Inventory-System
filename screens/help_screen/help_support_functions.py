from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from screens.help_screen.help_support import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn

class helpSupport(QMainWindow, Ui_MainWindow):
    back_signal = pyqtSignal()
    manual_signal = pyqtSignal()
    faq_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.backButton_3.clicked.connect(self.back)
        self.editUserButton_3.clicked.connect(self.navigate_manual)
        self.addUserButton.clicked.connect(self.navigate_faq)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

    def navigate_faq(self):
        self.faq_signal.emit()

    def back(self):
        self.back_signal.emit()

    def navigate_manual(self):
        self.manual_signal.emit()

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.sysTimeDate_3.setText(formattedDateTime)