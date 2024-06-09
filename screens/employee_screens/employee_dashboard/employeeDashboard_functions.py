from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDateTime, QTimer, Qt
from screens.employee_screens.employee_dashboard.employeeDashboard import Ui_MainWindow
from screens.employee_screens.employee_pos.posOrder_functions import posOrder
from screens.employee_screens.employee_inventory.inventory_Modify_functions import inventoryModify
from screens.help_screen.help_FAQ_functions import helpFAQ

class myEmployeeDashboard(QtWidgets.QMainWindow):

    logout_signal = QtCore.pyqtSignal()
    pos_signal = QtCore.pyqtSignal()
    inventoryModify_signal = QtCore.pyqtSignal()
    help_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pos_order = posOrder()
        self.inventory_modify = inventoryModify()

        self.ui.posButton.clicked.connect(self.navigate_pos)
        self.ui.logoutButton.clicked.connect(self.logout)
        self.ui.inventoryButton.clicked.connect(self.navigate_inventory)
        self.ui.helpButton.clicked.connect(self.navigate_help)

        # Update date and time labels
        self.update_datetime()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)  # Update every second

    def update_datetime(self):
        # Get current date and time
        current_datetime = QDateTime.currentDateTime()

        # Update date label
        date = current_datetime.toString("dddd, MMMM d, yyyy")
        self.ui.date.setText(date)

        # Update time label
        time = current_datetime.toString("hh:mm:ss AP")
        self.ui.time.setText(time)

    def navigate_pos(self):
        self.pos_signal.emit()

    def navigate_inventory(self):
        self.inventoryModify_signal.emit()

    def navigate_help(self):
        self.help_signal.emit()

    def logout(self):
        self.logout_signal.emit()

