from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtWidgets import QMainWindow
from screens.about_screen.about_devCredits import Ui_MainWindow
from shared.navigation_signal import auth_back
from validator.user_manager import userManager

class aboutdevCredits(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    info_signal = QtCore.pyqtSignal()
    back_kitchen_signal = QtCore.pyqtSignal()
    back_cashier_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.backButton.clicked.connect(lambda: auth_back(self.user_manager, self.back_signal,
                                                          self.back_kitchen_signal, self.back_cashier_signal))
        self.editUserButton.clicked.connect(self.navigate_info)

        # Create an instance of userManager
        self.user_manager = userManager()

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

    def navigate_info(self):
        self.info_signal.emit()

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.sysTimeDate.setText(formattedDateTime)

    def update_username(self):
        user_manager = userManager._instance
        name = user_manager.get_current_fullname()
        print(self.userName.text())
        self.userName.setText(name)
        print(self.userName.text())
        print("w", name)
