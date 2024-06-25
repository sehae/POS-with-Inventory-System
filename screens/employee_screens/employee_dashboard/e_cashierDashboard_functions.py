from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDateTime

from maintenance.user_logs import user_log
from screens.employee_screens.employee_dashboard.employee_cashierDashboard import Ui_MainWindow
from validator.user_manager import userManager

user_manager = userManager()

class myEmployeeDashboard_Cashier(QtWidgets.QMainWindow):

    logout_signal = QtCore.pyqtSignal()
    pos_signal = QtCore.pyqtSignal()
    help_signal = QtCore.pyqtSignal()
    about_signal = QtCore.pyqtSignal()
    changepass_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.logoutButton.clicked.connect(self.logout)
        self.ui.posButton.clicked.connect(self.pos_signal.emit)
        self.ui.helpButton.clicked.connect(self.help_signal.emit)
        self.ui.aboutButton.clicked.connect(self.about_signal.emit)
        self.ui.changePassButton.clicked.connect(self.changepass_signal.emit)

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

    def logout(self):
        user_id = user_manager.get_current_user_id()
        user_action = 9
        username = user_manager.get_current_username()
        user_log(user_id, user_action, username)

        user_manager.reset_user_data()

        self.logout_signal.emit()
