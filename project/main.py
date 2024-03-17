import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PyQt6.QtGui import QIcon, QAction
from login_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.showFullScreen()

    sys.exit(app.exec())