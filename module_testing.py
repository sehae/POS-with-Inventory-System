import sys

from PyQt5 import QtWidgets

from screens.admin_screens.admin_inventory.barcode_functions import BarcodeDialog
from screens.admin_screens.admin_maintenance.m_ADDuser_functions import adminMaintenance


def main():
    # Create an instance of QApplication
    app = QtWidgets.QApplication(sys.argv)

    # Create an instance of your class
    window = BarcodeDialog()

    # Show your instance
    window.show()

    # Execute the application's main loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()