import logging
import sys

from PyQt5 import Qt, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QPixmap
from screens.admin_screens.admin_inventory.barcode import Ui_Dialog  # Import the generated dialog class

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class BarcodeDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Setup the UI from the generated class

        logging.debug("Initializing BarcodeDialog")

        pixmap = QPixmap()
        pixmap.loadFromData(open("debug_barcode.png", "rb").read(), "png")

        self.barcodeLBL.setPixmap(pixmap)
        logging.debug("Barcode image set in the label")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = BarcodeDialog()
    window.show()
    sys.exit(app.exec_())
