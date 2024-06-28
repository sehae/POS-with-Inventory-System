from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QDateTime, QTimer, QDate
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QComboBox
from PyQt5.QtGui import QIntValidator, QDoubleValidator

from modules.inventory.barcode_generator import generate_barcode
from screens.admin_screens.admin_inventory.barcode_functions import BarcodeDialog
from screens.admin_screens.admin_inventory.inventoryAddProduct import Ui_MainWindow
from screens.admin_screens.admin_inventory.inventorySupplier_functions import adminSupplier
from server.local_server import conn
from validator.user_manager import userManager

user_manager = userManager()

class adminInventoryAddProduct(QMainWindow, Ui_MainWindow):
    modify_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    view_signal = QtCore.pyqtSignal()
    supplier_signal = QtCore.pyqtSignal()
    product_update_signal = QtCore.pyqtSignal()
    admin_product_update_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.barcode_dialog = None

        self.pushButton_4.clicked.connect(self.add_product)
        self.pushButton_10.clicked.connect(self.navigate_modify)
        self.pushButton_11.clicked.connect(self.navigate_view)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_5.clicked.connect(self.confirm_clear_fields)  # Connect clear button
        self.pushButton_12.clicked.connect(self.navigate_supplier)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        # Add items to comboBox
        self.comboBox.addItems(["Ingredient", "Beverage", "Food", "Miscellaneous"])
        self.comboBox.setCurrentIndex(-1)  # No initial selection

        # Call populateComboBox to fill comboBox_2 with supplier names
        self.populateComboBox()
        self.comboBox_2.setCurrentIndex(-1)  # No initial selection

        # Set the default expiry date to 2024/01/01
        default_date = QDate(2024, 1, 1)
        self.dateEdit.setDate(default_date)

        # Integer only in quantity and threshold value
        int_validator = QIntValidator()
        self.lineEdit_4.setValidator(int_validator)
        self.lineEdit_7.setValidator(int_validator)

        self.admin_supplier = adminSupplier()

        self.admin_supplier.supplier_generated_signal.connect(self.populateComboBox)
        self.admin_supplier.supplier_updated_signal.connect(self.populateComboBox)

        # Apply QDoubleValidator to buying_cost and selling_cost fields
        double_validator = QDoubleValidator(0.00, 9999.99, 2)
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.lineEdit_3.setValidator(double_validator)
        self.lineEdit_5.setValidator(double_validator)

    def navigate_view(self):
        self.view_signal.emit()

    def navigate_modify(self):
        self.modify_signal.emit()

    def navigate_supplier(self):
        self.supplier_signal.emit()

    def back(self):
        self.back_signal.emit()

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.label_2.setText(formattedDateTime)

    def add_product(self):
        # Get the values entered by the user
        name = self.lineEdit_2.text()
        category = self.comboBox.currentText()
        quantity = self.lineEdit_4.text()
        buying_cost = self.lineEdit_3.text()
        selling_cost = self.lineEdit_5.text()
        supplier_name = self.comboBox_2.currentText()
        expiry_date = self.dateEdit.date().toString('yyyy-MM-dd')
        threshold_value = self.lineEdit_7.text()

        # Validate inputs
        if not self.validate_inputs(name, category, quantity, buying_cost, selling_cost, supplier_name,
                                    threshold_value):
            return

        try:
            cursor = conn.cursor()

            # Calculate availability based on quantity and threshold value
            if int(quantity) == 0:
                availability = 'Out of Stock'
            elif int(quantity) <= int(threshold_value):
                availability = 'Low Stock'
            else:
                availability = 'In Stock'

            # Fetch the latest Product_ID for the current date
            cursor.execute("SELECT MAX(Product_ID) FROM product")
            latest_product_id = cursor.fetchone()[0]

            if latest_product_id:
                # Extract numeric part and increment
                numeric_part = latest_product_id[3:]  # Assuming Product_ID format is POSNNN
                product_number = int(numeric_part)
                new_product_number = product_number + 1
                next_product_number = f"{new_product_number:03d}"
            else:
                # If no previous products, start from 001
                next_product_number = "001"

            # Construct new Product_ID
            new_product_id = f"PRD{next_product_number}"

            # Get the value of supplier id where supplier name gathered by the user
            cursor.execute("SELECT Supplier_ID FROM supplier WHERE Supplier_Name = %s", (supplier_name,))
            supplier_result = cursor.fetchone()

            if supplier_result is None:
                QMessageBox.critical(self, "Error", "Supplier not found.")
                return

            supplier_id = supplier_result[0]

            # Get current date in yyyy-MM-dd format
            current_date = QDateTime.currentDateTime().toString("yyyy-MM-dd")

            # Get current time in HH:mm format
            current_time = QDateTime.currentDateTime().toString("HH:mm")

            # Insert into product table
            product_query = """
                INSERT INTO product (Product_ID, Name, Quantity, Category, Expiry_Date, Threshold_Value, Availability, Status, Date, Time) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, 'Active', %s, %s)
            """
            product_values = (
                new_product_id, name, quantity, category, expiry_date, threshold_value, availability, current_date,
                current_time)
            cursor.execute(product_query, product_values)

            barcode_str = generate_barcode(name)

            # Insert into inventory table
            if category == "Ingredient":
                inventory_query = """
                    INSERT INTO inventory (Supplier_ID, Product_ID, Barcode) 
                    VALUES (%s, %s, %s)
                """
                inventory_values = (supplier_id, new_product_id, barcode_str)
            else:
                inventory_query = """
                    INSERT INTO inventory (Supplier_ID, Product_ID, Buying_Cost, Selling_Cost, Barcode) 
                    VALUES (%s, %s, %s, %s, %s)
                """
                inventory_values = (supplier_id, new_product_id, buying_cost or None, selling_cost or None, barcode_str)

            cursor.execute(inventory_query, inventory_values)

            conn.commit()
            QMessageBox.information(self, "Success", "Product added successfully.")
            self.product_update_signal.emit()
            self.admin_product_update_signal.emit()
            self.open_barcode()

            self.clear_fields()  # Clear fields after successful addition

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def validate_inputs(self, name, category, quantity, buying_cost, selling_cost, supplier_name, threshold_value):
        # Flag to check if all required inputs are valid
        valid = True

        if not name:
            self.lineEdit_2.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_2.setStyleSheet("border: 1px solid green;")

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

        if category != "Ingredient":
            if not buying_cost:
                self.lineEdit_3.setStyleSheet("border: 1px solid red;")
                valid = False
            else:
                try:
                    buying_cost_float = float(buying_cost)
                    if not (buying_cost_float.is_integer() or round(buying_cost_float % 1, 2) == 0.00):
                        raise ValueError("Buying cost must have exactly two decimal places.")
                    self.lineEdit_3.setStyleSheet("border: 1px solid green;")
                except ValueError:
                    self.lineEdit_3.setStyleSheet("border: 1px solid red;")
                    valid = False

            if not selling_cost:
                self.lineEdit_5.setStyleSheet("border: 1px solid red;")
                valid = False
            else:
                try:
                    selling_cost_float = float(selling_cost)
                    if not (selling_cost_float.is_integer() or round(selling_cost_float % 1, 2) == 0.00):
                        raise ValueError("Selling cost must have exactly two decimal places.")
                    self.lineEdit_5.setStyleSheet("border: 1px solid green;")
                except ValueError:
                    self.lineEdit_5.setStyleSheet("border: 1px solid red;")
                    valid = False

        if not supplier_name:
            self.comboBox_2.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_2.setStyleSheet("border: 1px solid green;")

        if not threshold_value:
            self.lineEdit_7.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_7.setStyleSheet("border: 1px solid green;")

        if not valid:
            QMessageBox.warning(self, "Warning", "Please fill in all fields correctly.")

        return valid

    def confirm_clear_fields(self):
        reply = QMessageBox.question(self, 'Warning', 'This will discard all input from the fields. Are you sure?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.clear_fields()

    def clear_fields(self):
        # Clear all input fields and reset styles
        self.lineEdit_2.clear()
        self.comboBox.setCurrentIndex(-1)
        self.lineEdit_4.clear()
        self.lineEdit_3.clear()
        self.lineEdit_5.clear()
        self.comboBox_2.setCurrentIndex(-1)
        self.dateEdit.setDate(QDate(2024, 1, 1))
        self.lineEdit_7.clear()
        self.reset_styles()

    def reset_styles(self):
        self.lineEdit_2.setStyleSheet("")
        self.comboBox.setStyleSheet("")
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_5.setStyleSheet("")
        self.comboBox_2.setStyleSheet("")
        self.dateEdit.setStyleSheet("")
        self.lineEdit_7.setStyleSheet("")

    def populateComboBox(self):
        try:
            if conn.is_connected():
                cursor = conn.cursor()

                # Execute the query to retrieve supplier names
                query = "SELECT Supplier_Name FROM supplier WHERE Status = 'Active'"
                cursor.execute(query)

                # Fetch all the supplier names
                supplier_names = cursor.fetchall()

                # Clear the comboBox_2 before adding new items
                self.comboBox_2.clear()

                # Add each supplier name to the comboBox_2
                for name in supplier_names:
                    self.comboBox_2.addItem(name[0])

            else:
                print("No connection to the database.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred while populating comboBox_2: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def open_barcode(self):
        self.barcode_dialog = BarcodeDialog()
        self.barcode_dialog.show()
