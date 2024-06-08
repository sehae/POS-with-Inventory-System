from shared.imports import *
sys.path.append('path/to/Software-Engineering-Project')


def test():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = myLoginScreen()
    ui.setupUi(MainWindow)
    MainWindow.setWindowState(QtCore.Qt.WindowFullScreen)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    test()
