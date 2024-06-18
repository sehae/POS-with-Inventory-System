from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtWidgets import QMainWindow

from screens.admin_screens.admin_maintenance.backup import Ui_MainWindow
from shared.navigation_signal import back
from styles.universalStyles import COMBOBOX_STYLE, COMBOBOX_STYLE_VIEW


class backupRestore(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backBTN.clicked.connect(lambda: back(self.back_signal))

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        self.UIComponents()

    def UIComponents(self):
        self.frequencyBOX.setStyleSheet(COMBOBOX_STYLE)
        self.frequencyBOX.view().setStyleSheet(COMBOBOX_STYLE_VIEW)
        self.backupDatesBOX.setStyleSheet(COMBOBOX_STYLE)
        self.backupDatesBOX.view().setStyleSheet(COMBOBOX_STYLE_VIEW)

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.sysTimeDate.setText(formattedDateTime)



