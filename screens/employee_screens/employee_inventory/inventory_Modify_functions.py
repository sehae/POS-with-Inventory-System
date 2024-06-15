# inventory_Modify_functions.py

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt, pyqtSignal, QDate
from PyQt5.QtWidgets import QMainWindow
from screens.employee_screens.employee_inventory.inventory_Modify import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from server.local_server import conn

class inventoryModify(QMainWindow, Ui_MainWindow):
    barcode_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    inventory_table = QtCore.pyqtSignal()
    product_update_signal = QtCore.pyqtSignal()
    employee_update_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_10.clicked.connect(self.navigate_barcode)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_3.clicked.connect(self.navigate_inventory)
        self.pushButton_4.clicked.connect(self.save_product)
        self.pushButton_5.clicked.connect(self.confirm_clear_fields)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second


        self.comboBox.addItems(["Ingredient", "Beverage", "Food", "Miscellaneous"])
        self.comboBox.setCurrentIndex(-1)  # No initial selection
        # Populate comboBox_2 with product names
        self.populate_comboBox_2()

        # Connect signals to update comboBox_2 when the product table is modified
        self.product_update_signal.connect(self.populate_comboBox_2)
        self.employee_update_signal.connect(self.populate_comboBox_2)

        # Apply QDoubleValidator to buying_cost and selling_cost fields
        double_validator = QDoubleValidator(0.00, 9999.99, 2)
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.lineEdit_4.setValidator(double_validator)
        self.lineEdit_5.setValidator(double_validator)

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.label_2.setText(formattedDateTime)

    def navigate_barcode(self):
        self.barcode_signal.emit()

    def navigate_inventory(self):
        self.inventory_table.emit()

    def back(self):
        self.back_signal.emit()

    def save_product(self):
        name = self.comboBox_2.currentText()
        category = self.comboBox.currentText()
        quantity = self.lineEdit_4.text()
        expiry_date = self.dateEdit.date().toString('yyyy-MM-dd')  # Get the date as a string in the desired format
        threshold_value = self.lineEdit_5.text()

        if not self.validate_inputs(name, category, quantity, threshold_value):
            return

        try:
            cursor = conn.cursor()

            cursor.execute(f"""
                UPDATE product 
                SET 
                    Quantity={quantity}, 
                    Threshold_Value={threshold_value}, 
                    Category='{category}', 
                    Expiry_Date='{expiry_date}', 
                    Availability = 
                        CASE 
                            WHEN {quantity} = 0 THEN 'Out of Stock' 
                            WHEN {quantity} <= {threshold_value} THEN 'Low Stock' 
                            ELSE 'In Stock' 
                        END 
                WHERE Name='{name}'
            """)

            conn.commit()
            QMessageBox.information(self, "Success", "Product updated successfully.")
            self.product_update_signal.emit()
            self.employee_update_signal.emit()

            self.clear_fields()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def validate_inputs(self, name, category, quantity, threshold_value):
        valid = True

        if not name:
            self.comboBox_2.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_2.setStyleSheet("border: 1px solid green;")

        if category not in ["Ingredient", "Beverage", "Food", "Miscellaneous"]:
            self.comboBox.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox.setStyleSheet("border: 1px solid green;")

        if not quantity:
            self.lineEdit_4.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_4.setStyleSheet("border: 1px solid green;")

        if not threshold_value:
            self.lineEdit_5.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_5.setStyleSheet("border: 1px solid green;")

        if not valid:
            QMessageBox.warning(self, "Warning", "Please fill in all fields correctly.")

        return valid

    def confirm_clear_fields(self):
        reply = QMessageBox.question(self, 'Warning', 'This will discard all input from the fields. Are you sure?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.clear_fields()

    def clear_fields(self):
        self.comboBox_2.setCurrentIndex(-1)
        self.comboBox.setCurrentIndex(-1)
        self.lineEdit_4.clear()
        self.dateEdit.setDate(QDate(2024, 1, 1))
        self.lineEdit_5.clear()
        self.reset_styles()

    def reset_styles(self):
        self.comboBox_2.setStyleSheet("")
        self.comboBox.setStyleSheet("")
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_5.setStyleSheet("")
        self.comboBox.setStyleSheet("")

    def populate_comboBox_2(self):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT Name FROM product WHERE Status = 'active'")
            product_names = cursor.fetchall()

            self.comboBox_2.clear()
            for name in product_names:
                self.comboBox_2.addItem(name[0])

        except Exception as e:
            print(f"Error occurred while populating comboBox_2: {e}")

        finally:
            if conn.is_connected():
                cursor.close()
