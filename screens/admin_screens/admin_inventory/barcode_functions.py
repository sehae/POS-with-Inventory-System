import logging
import sys

from PyQt5.QtCore import QSizeF
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog

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

        self.printBTN.clicked.connect(self.print_barcode)
        self.cancelBTN.clicked.connect(self.close)

    def print_barcode(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setPageSizeMM(QSizeF(80, 200))  # Set page size to 80mm width, initial height 200mm

        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            painter = QPainter(printer)

            # Calculate height based on actual content height (in this case, image height)
            content_height = self.barcodeLBL.pixmap().height() * (80 / self.barcodeLBL.pixmap().width())
            printer.setPageSizeMM(QSizeF(80, content_height))  # Adjust page size based on content

            # Draw the pixmap
            painter.drawPixmap(0, 0, self.barcodeLBL.pixmap())  # Draw at position (0, 0) using the full size of the pixmap
            painter.end()

            logging.debug("Barcode printed successfully")
        else:
            logging.debug("Printing cancelled or failed")
