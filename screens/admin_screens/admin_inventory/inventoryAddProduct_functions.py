from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QMainWindow
from screens.admin_screens.admin_inventory.inventoryAddProduct import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn

class adminInventoryAddProduct(QMainWindow, Ui_MainWindow):
    modify_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.addButton.clicked.connect(self.add_product)
        self.modifyProductButton.clicked.connect(self.navigate_modify)
        self.backButton.clicked.connect(self.back)
        self.category_comboBox.addItems(["Ingredient", "Beverage"])

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

    def navigate_modify(self):
        self.modify_signal.emit()

    def back(self):
        self.back_signal.emit()

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.dateLabel.setText(formattedDateTime)

    def add_product(self):
        print("add_product method called")