from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox

from screens.admin_screens.admin_inventory.inventoryAddProduct import Ui_MainWindow
from server.local_server import conn


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

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        self.comboBox.addItems(["Ingredient", "Beverage"])

        # Call populateComboBox to fill comboBox_2 with supplier names
        self.populateComboBox()

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
        print("Add_product called")

        # Get the values entered by the user
        name = self.lineEdit_2.text()
        category = self.comboBox.currentText()
        quantity = int(self.lineEdit_4.text())  # Convert to int
        buying_cost = self.lineEdit_3.text()
        selling_cost = self.lineEdit_5.text()
        supplier_name = self.comboBox_2.currentText()
        expiry_date = self.lineEdit_6.text()
        threshold_value = int(self.lineEdit_7.text())  # Convert to int

        # Check if any field is empty
        if not name or not category or not quantity or not buying_cost or not selling_cost or not supplier_name or not expiry_date or not threshold_value:
            QMessageBox.warning(self, "Warning", "Please fill in all fields.")
            return

        try:
            cursor = conn.cursor()

            # Calculate availability based on quantity and threshold value
            if quantity == 0:
                availability = 'Out of Stock'
            elif quantity <= threshold_value:
                availability = 'Low Stock'
            else:
                availability = 'In Stock'

            # Get the value of supplier id where supplier name gathered by the user
            cursor.execute("SELECT Supplier_ID FROM supplier WHERE Supplier_Name = %s", (supplier_name,))
            supplier_result = cursor.fetchone()

            supplier_id = supplier_result[0]


            # Insert into product table
            product_query = """
                INSERT INTO product (Name, Quantity, Category, Expiry_Date, Threshold_Value, Availability, Status) 
                VALUES (%s, %s, %s, %s, %s, %s, 'Active')
            """
            product_values = (name, quantity, category, expiry_date, threshold_value, availability)
            cursor.execute(product_query, product_values)

            # Get the value of product_id
            cursor.execute("Select Product_ID from product WHERE Name = %s", (name,))
            product_result = cursor.fetchone()

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

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred: {str(e)}")

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

                print("ComboBox_2 values changed successfully")

            else:
                print("No connection to the database.")

        except Exception as e:
            print("Error occurred while populating comboBox_2:", e)

