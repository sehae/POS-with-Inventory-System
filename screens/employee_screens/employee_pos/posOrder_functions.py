from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QMainWindow
from screens.employee_screens.employee_pos.posOrder import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn

class posOrder(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    payment_signal = QtCore.pyqtSignal()
    home_signal = QtCore.pyqtSignal()
    menu_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.paymentBTN.clicked.connect(self.goPayment)
        self.backBTN.clicked.connect(self.goBack)
        self.menuBTN.clicked.connect(self.goMenu)
        self.homeBTN.clicked.connect(self.goHome)


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
        self.date.setText(formattedDateTime)

    def goHome(self):
        self.home_signal.emit()

    def goMenu(self):
        self.menu_signal.emit()

    def goPayment(self):
        self.payment_signal.emit()

    def goOrder(self):
        self.order_signal.emit()

    def goBack(self):
        self.back_signal.emit()
