from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow

from screens.authentication_screens.password_recovery.passwordRecovery_Result import Ui_MainWindow


class PasswordResult(QMainWindow, Ui_MainWindow):
    login_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.backButton.clicked.connect(self.login_signal.emit)
