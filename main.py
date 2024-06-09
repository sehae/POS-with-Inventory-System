from screens.authentication_screens.login_screen.login_functions import myLoginScreen
from screens.admin_screens.admin_maintenance.m_EDITuser_functions import adminMaintenanceEDIT
from screens.admin_screens.admin_maintenance.m_ADDuser_functions import adminMaintenance
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
