from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QDateTime, QTimer, QDate
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QComboBox
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from screens.admin_screens.admin_inventory.inventoryAddProduct import Ui_MainWindow
from server.local_server import conn
from validator.user_manager import userManager

user_manager = userManager()

class adminInventoryAddProduct(QMainWindow, Ui_MainWindow):
    modify_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    view_signal = QtCore.pyqtSignal()
    product_update_signal = QtCore.pyqtSignal()
    admin_product_update_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_4.clicked.connect(self.add_product)
        self.pushButton_10.clicked.connect(self.navigate_modify)
        self.pushButton_11.clicked.connect(self.navigate_view)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_5.clicked.connect(self.confirm_clear_fields)  # Connect clear button

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

        # Apply QDoubleValidator to buying_cost and selling_cost fields
        double_validator = QDoubleValidator(0.00, 9999.99, 2)
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.lineEdit_3.setValidator(double_validator)
        self.lineEdit_5.setValidator(double_validator)

    def navigate_view(self):
        self.view_signal.emit()

    def navigate_modify(self):
        self.modify_signal.emit()

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
        if not self.validate_inputs(name, category, quantity, buying_cost, selling_cost, supplier_name, threshold_value):
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

            # Get the value of supplier id where supplier name gathered by the user
            cursor.execute("SELECT Supplier_ID FROM supplier WHERE Supplier_Name = %s", (supplier_name,))
            supplier_result = cursor.fetchone()

            if supplier_result is None:
                QMessageBox.critical(self, "Error", "Supplier not found.")
                return

            supplier_id = supplier_result[0]

            # Insert into product table
            product_query = """
                INSERT INTO product (Name, Quantity, Category, Expiry_Date, Threshold_Value, Availability, Status) 
                VALUES (%s, %s, %s, %s, %s, %s, 'Active')
            """
            product_values = (name, quantity, category, expiry_date, threshold_value, availability)
            cursor.execute(product_query, product_values)

            # Get the value of product_id
            cursor.execute("SELECT Product_ID FROM product WHERE Name = %s", (name,))
            product_result = cursor.fetchone()

            if product_result is None:
                QMessageBox.critical(self, "Error", "Product not found after insertion.")
                return

            product_id = product_result[0]

            # Insert into inventory table
            inventory_query = """
                INSERT INTO inventory (Supplier_ID, Product_ID, Buying_Cost, Selling_Cost) 
                VALUES (%s, %s, %s, %s)
            """
            inventory_values = (supplier_id, product_id, buying_cost, selling_cost)
            cursor.execute(inventory_query, inventory_values)

            conn.commit()
            QMessageBox.information(self, "Success", "Product added successfully.")
            self.product_update_signal.emit()
            self.admin_product_update_signal.emit()

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

        if buying_cost:  # Check if buying_cost is not empty
            try:
                buying_cost_float = float(buying_cost)
                if not (buying_cost_float.is_integer() or round(buying_cost_float % 1, 2) == 0.00):
                    raise ValueError("Buying cost must have exactly two decimal places.")
                self.lineEdit_5.setStyleSheet("border: 1px solid green;")
            except ValueError:
                self.lineEdit_5.setStyleSheet("border: 1px solid red;")
                valid = False
        else:
            # Optional field is considered valid if empty
            self.lineEdit_3.setStyleSheet("border: 1px solid green;")

        if selling_cost:  # Check if selling_cost is not empty
            try:
                selling_cost_float = float(selling_cost)
                if not (selling_cost_float.is_integer() or round(selling_cost_float % 1, 2) == 0.00):
                    raise ValueError("Selling cost must have exactly two decimal places.")
                self.lineEdit_4.setStyleSheet("border: 1px solid green;")
            except ValueError:
                self.lineEdit_4.setStyleSheet("border: 1px solid red;")
                valid = False
        else:
            # Optional field is considered valid if empty
            self.lineEdit_5.setStyleSheet("border: 1px solid green;")

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
                query = "SELECT Supplier_Name FROM supplier"
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
