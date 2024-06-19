from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from screens.employee_screens.employee_inventory.inventory_Barcode import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from validator.user_manager import userManager

user_manager = userManager()

class inventoryBarcode(QMainWindow, Ui_MainWindow):
    modify_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    inventory_table = QtCore.pyqtSignal()



    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.navigate_modify)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_3.clicked.connect(self.navigate_inventory)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        # Connect the fullname_updated signal to the slot
        user_manager.fullname_updated.connect(self.update_fullname_label)

        # Set initial fullname if already set
        if user_manager.get_current_fullname():
            self.update_fullname_label(user_manager.get_current_fullname())

    def update_fullname_label(self, fullname):
        self.label_3.setText(fullname)  # Update the label with the fullname

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.label_2.setText(formattedDateTime)

    def navigate_modify(self):
        self.modify_signal.emit()

    def navigate_inventory(self):
        self.inventory_table.emit()

    def back(self):
        self.back_signal.emit()

