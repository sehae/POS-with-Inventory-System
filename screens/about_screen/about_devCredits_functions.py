from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QMainWindow
from screens.about_screen.about_devCredits import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from validator.user_manager import userManager

class aboutdevCredits(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    info_signal = QtCore.pyqtSignal()
    back_employee_signal = QtCore.pyqtSignal()


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.backButton.clicked.connect(self.back)
        self.editUserButton.clicked.connect(self.navigate_info)

        # Create an instance of userManager
        self.user_manager = userManager()

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

    def back(self):
        updated_user_type = self.user_manager.updated_userType
        if updated_user_type == "Admin":
            print("You clicked back as an admin")
            self.back_signal.emit()
        elif updated_user_type == "Employee":
            print("You clicked back as an employee")
            self.back_employee_signal.emit()


    def navigate_info(self):
        self.info_signal.emit()

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.sysTimeDate.setText(formattedDateTime)