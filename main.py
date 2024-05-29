import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from screens.admin_screens.admin_maintenance.m_ADDuser_functions import adminMaintenance
from screens.authentication_screens.login_screen.login_functions import myLoginScreen

sys.path.append('path/to/Software-Engineering-Project')

def show_login_screen():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = adminMaintenance()
    ui.setupUi(MainWindow)
    MainWindow.setWindowState(QtCore.Qt.WindowFullScreen)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    show_login_screen()
