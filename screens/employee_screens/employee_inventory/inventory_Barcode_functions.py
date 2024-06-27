from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt, pyqtSignal, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow

from modules.maintenance.user_logs import user_log
from screens.employee_screens.employee_inventory.inventory_Barcode import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from validator.user_manager import userManager

user_manager = userManager()


class inventoryBarcode(QMainWindow, Ui_MainWindow):
    modify_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    inventory_table = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.modify_signal.emit)
        self.pushButton.clicked.connect(self.back_signal.emit)
        self.pushButton_3.clicked.connect(self.inventory_table.emit)

        self.updateBTN.clicked.connect(self.update_quantity)
        self.cancelBTN.clicked.connect(self.reset_fields)
        self.barcodeFIELD.setFocus()

        # Create a QTimer object
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)  # Update every second

        # Dictionary to store barcode counts
        self.barcode_counts = {}
        self.last_scanned_barcode = None

        # Set up regex validator for barcodeFIELD
        barcode_regex = QRegExp(r"^\d{13}$")
        barcode_validator = QRegExpValidator(barcode_regex, self.barcodeFIELD)
        self.barcodeFIELD.setValidator(barcode_validator)

        # Connect textChanged signal to a custom slot
        self.barcodeFIELD.textChanged.connect(self.check_barcode_length)

    def update_fullname_label(self, fullname):
        self.label_3.setText(fullname)  # Update the label with the fullname

    def updateDateTime(self):
        currentDateTime = QDateTime.currentDateTime()
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")
        self.label_2.setText(formattedDateTime)

    def check_barcode_length(self):
        if len(self.barcodeFIELD.text()) == 13:
            self.scan_barcode()

    def scan_barcode(self):
        barcode = self.barcodeFIELD.text()
        if not self.barcodeFIELD.hasAcceptableInput():
            QMessageBox.warning(self, "Invalid Barcode", "The barcode must be 13 digits long and contain only numbers.")
            return

        if self.last_scanned_barcode and self.last_scanned_barcode != barcode:
            reply = QMessageBox.question(
                self, 'Confirm Scan',
                "You are counting a different product. Are you sure?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )

            if reply == QMessageBox.No:
                return

            # If yes, reset the previous scan data
            self.barcode_counts[self.last_scanned_barcode] = 0
            self.last_scanned_barcode = None

        cursor = conn.cursor()
        cursor.execute("SELECT product_id FROM inventory WHERE barcode = %s;", (barcode,))
        product_id = cursor.fetchone()

        if product_id:
            cursor.execute("SELECT name, quantity FROM product WHERE product_id = %s;", (product_id[0],))
            product_data = cursor.fetchone()

            if product_data:
                product_name, quantity = product_data
                self.productFIELD.setText(product_name)
                self.quantityFIELD.setText(str(quantity))

                if barcode in self.barcode_counts:
                    self.barcode_counts[barcode] += 1
                else:
                    self.barcode_counts[barcode] = 1

                self.countFIELD.setText(str(self.barcode_counts[barcode]))
                self.last_scanned_barcode = barcode
                self.barcodeFIELD.clear()
                self.barcodeFIELD.setFocus()
            else:
                QMessageBox.warning(self, "Product Not Found", "Product data not found for the given barcode.")
        else:
            QMessageBox.warning(self, "Barcode Not Found", "No product found for the entered barcode.")

        cursor.close()

    def update_quantity(self):
        if self.last_scanned_barcode:
            barcode = self.last_scanned_barcode
            count = self.barcode_counts.get(barcode, 0)
            quantity = int(self.quantityFIELD.text())

            if count > 0:
                if count > quantity:
                    QMessageBox.warning(self, "Count Error", "You might have miscounted. The scanned count is more than the available quantity.")
                    return

                reply = QMessageBox.question(
                    self, 'Confirm Update',
                    "Are you sure you want to update the quantity?",
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                )

                if reply == QMessageBox.Yes:
                    cursor = conn.cursor()
                    cursor.execute("SELECT product_id FROM inventory WHERE barcode = %s;", (barcode,))
                    product_id = cursor.fetchone()

                    if product_id:
                        cursor.execute("UPDATE product SET quantity = %s WHERE product_id = %s;",
                                       (count, product_id[0]))
                        conn.commit()
                        QMessageBox.information(self, "Update Successful", f"The quantity for product is now {count}")
                    else:
                        QMessageBox.warning(self, "Update Failed", "Product ID not found.")

                    cursor.execute("SELECT name FROM product WHERE product_id = %s;", (product_id[0],))
                    product_name = cursor.fetchone()[0]

                    cursor.close()
                    self.barcode_counts[barcode] = 0
                    self.reset_fields()

                    id = user_manager.get_current_user_id()
                    username = user_manager.get_current_username()
                    user_log(id, 16, username, f"of {product_name} from {quantity} to {count}")
                else:
                    QMessageBox.information(self, "Update Cancelled", "The update was cancelled.")
            else:
                QMessageBox.warning(self, "No Scans", "No scans to update.")
        else:
            QMessageBox.warning(self, "No Barcode", "No barcode has been scanned.")

    def reset_fields(self):
        self.barcode_counts.clear()
        self.last_scanned_barcode = None
        self.countFIELD.clear()
        self.productFIELD.clear()
        self.quantityFIELD.clear()
        self.barcodeFIELD.clear()
        self.barcodeFIELD.setFocus()
