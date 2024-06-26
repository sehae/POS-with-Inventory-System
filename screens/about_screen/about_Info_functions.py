from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from screens.about_screen.about_Info import Ui_MainWindow
from shared.navigation_signal import auth_back
from validator.user_manager import userManager

class aboutInfo(QMainWindow, Ui_MainWindow):
    back_signal = pyqtSignal()
    credits_signal = pyqtSignal()
    back_kitchen_signal = pyqtSignal()
    back_cashier_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user_manager = userManager()

        self.backButton.clicked.connect(lambda: auth_back(self.user_manager, self.back_signal,
                                                          self.back_kitchen_signal, self.back_cashier_signal))
        self.pushButton.clicked.connect(self.navigate_credits)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second


    def navigate_credits(self):
        self.credits_signal.emit()

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.sysTimeDate.setText(formattedDateTime)
