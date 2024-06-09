from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QMainWindow
from screens.employee_screens.employee_pos.posTable import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn

class posTable(QMainWindow, Ui_MainWindow):
    payment_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    order_signal = QtCore.pyqtSignal()


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.paymentBTN.clicked.connect(self.navigate_payment)
        self.backBTN.clicked.connect(self.back)
        self.orderBTN.clicked.connect(self.navigate_order)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.label_2.setText(formattedDateTime)

    def navigate_payment(self):
        self.payment_signal.emit()

    def back(self):
        self.back_signal.emit()

    def navigate_order(self):
        self.order_signal.emit()