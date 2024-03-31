import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from screens.loginScreen import Ui_MainWindow

sys.path.append('path/to/Software-Engineering-Project')

def show_login_screen():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowState(QtCore.Qt.WindowFullScreen)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    show_login_screen()
