from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDateTime, QTimer, Qt

from modules.maintenance.user_logs import user_log
from screens.employee_screens.employee_dashboard.employeeDashboard import Ui_MainWindow
from screens.employee_screens.employee_inventory.inventory_Modify_functions import inventoryModify
from validator.user_manager import userManager

user_manager = userManager()

class myEmployeeDashboard(QtWidgets.QMainWindow):

    logout_signal = QtCore.pyqtSignal()
    inventoryModify_signal = QtCore.pyqtSignal()
    help_signal = QtCore.pyqtSignal()
    about_signal = QtCore.pyqtSignal()
    changepass_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.inventory_modify = inventoryModify()
        self.ui.logoutButton.clicked.connect(self.logout)
        self.ui.inventoryButton.clicked.connect(self.navigate_inventory)
        self.ui.helpButton.clicked.connect(self.navigate_help)
        self.ui.aboutButton.clicked.connect(self.navigate_about)
        self.ui.changePassButton.clicked.connect(self.navigate_changepw)

        # Update date and time labels
        self.update_datetime()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)  # Update every second

    def update_fullname_label(self, fullname):
        self.ui.username.setText(fullname)  # Update the label with the fullname

    def update_datetime(self):
        # Get current date and time
        current_datetime = QDateTime.currentDateTime()

        # Update date label
        date = current_datetime.toString("dddd, MMMM d, yyyy")
        self.ui.date.setText(date)

        # Update time label
        time = current_datetime.toString("hh:mm:ss AP")
        self.ui.time.setText(time)
        self.update_fullname_label(user_manager.get_current_fullname())

    def navigate_changepw(self):
        self.changepass_signal.emit()

    def navigate_about(self):
        self.about_signal.emit()

    def navigate_pos(self):
        self.pos_signal.emit()

    def navigate_inventory(self):
        self.inventoryModify_signal.emit()

    def navigate_help(self):
        self.help_signal.emit()

    def logout(self):
        user_id = user_manager.get_current_user_id()
        user_action = 9
        username = user_manager.get_current_username()
        user_log(user_id, user_action, username)

        user_manager.reset_user_data()

        self.logout_signal.emit()
