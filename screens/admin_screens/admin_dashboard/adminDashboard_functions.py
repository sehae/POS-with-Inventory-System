from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDateTime, QTimer, Qt
from screens.admin_screens.admin_dashboard.adminDashboard import Ui_MainWindow
from validator.user_manager import userManager

user_manager_instance = userManager()

class myAdminDashboard(QtWidgets.QMainWindow):
    logout_signal = QtCore.pyqtSignal()
    maintenance_signal = QtCore.pyqtSignal()
    inventory_signal = QtCore.pyqtSignal()
    about_signal = QtCore.pyqtSignal()
    help_signal = QtCore.pyqtSignal()
    changepass_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.maintenanceButton.clicked.connect(self.navigate_maintenance)
        self.ui.inventoryButton.clicked.connect(self.navigate_inventory)
        self.ui.reportsButton.clicked.connect(self.navigate_reports)
        self.ui.changePassButton.clicked.connect(self.navigate_password)
        self.ui.helpButton.clicked.connect(self.navigate_help)
        self.ui.aboutButton.clicked.connect(self.navigate_about)
        self.ui.logoutButton.clicked.connect(self.logout)

        # Update date and time labels
        self.update_datetime()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)  # Update every second
        self.user_manager = user_manager_instance

        self.user_manager.fullname_updated.connect(self.update_full_name)

    def update_full_name(self, full_name):
        self.ui.username.setText(full_name)

    def update_datetime(self):
        # Get current date and time
        current_datetime = QDateTime.currentDateTime()

        # Update date label
        date = current_datetime.toString("dddd, MMMM d, yyyy")
        self.ui.date.setText(date)

        # Update time label
        time = current_datetime.toString("hh:mm:ss AP")
        self.ui.time.setText(time)

    def navigate_maintenance(self):
        self.maintenance_signal.emit()

    def navigate_inventory(self):
        self.inventory_signal.emit()

    def navigate_reports(self):
        return # Placeholder for future implementation

    def navigate_password(self):
        self.changepass_signal.emit()

    def navigate_help(self):
        self.help_signal.emit()

    def navigate_about(self):
        self.about_signal.emit()

    def logout(self):
        self.user_manager.reset_user_data()
        self.logout_signal.emit()

