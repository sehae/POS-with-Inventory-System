from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QMainWindow
from screens.employee_screens.employee_pos.posPayment import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from validator.user_manager import userManager

user_manager = userManager()

class posPayment(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    order_signal = QtCore.pyqtSignal()
    home_signal = QtCore.pyqtSignal()
    menu_signal = QtCore.pyqtSignal()


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.orderBTN_2.clicked.connect(self.goOrder)
        self.backBTN_2.clicked.connect(self.goBack)
        self.menuBTN_2.clicked.connect(self.goMenu)
        self.homeBTN_2.clicked.connect(self.goHome)

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
        self.label_12.setText(fullname)  # Update the label with the fullname

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.label_11.setText(formattedDateTime)

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