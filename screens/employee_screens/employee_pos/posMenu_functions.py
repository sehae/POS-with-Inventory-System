from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from PyQt5.QtCore import QDateTime, QTimer, QRegExp

# Assuming these imports are part of your project structure
from screens.employee_screens.employee_pos.posMenu import Ui_MainWindow
from shared.navigation_signal import auth_back, pos_back
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from screens.employee_screens.employee_pos.posOrderdetails_functions import posOrderdetails
from PyQt5.QtGui import QIntValidator

import json

from validator.user_manager import userManager


class posMenu(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    back_cashier_signal = QtCore.pyqtSignal()
    checkout_signal = QtCore.pyqtSignal()
    modify_signal = QtCore.pyqtSignal()
    order_signal = QtCore.pyqtSignal()
    history_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user_manager = userManager()

        self.backBTN.clicked.connect(lambda: pos_back(self.user_manager, self.back_signal, self.back_cashier_signal))
        self.checkoutBTN.clicked.connect(self.checkout_signal.emit)
        self.modifyBTN.clicked.connect(self.modify_signal.emit)
        self.orderBTN.clicked.connect(self.order_signal.emit)
        self.pushButton_8.clicked.connect(self.save_add_on)
        self.pushButton_9.clicked.connect(self.clear)
        self.historyBTN_2.clicked.connect(self.history_signal.emit)

        #self.pos_orderdetails = posOrderdetails()

        #self.pos_orderdetails.update_combobox_signal.connect(self.populate_comboBox_5)
        #self.pos_orderdetails.transaction_generated_signal.connect(self.populate_comboBox_5)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.timeout.connect(self.populate_table)
        self.timer.timeout.connect(self.populate_table_2)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        #self.admin_inventory_add = adminInventoryAddProduct()
        #self.admin_inventory_add.admin_product_update_signal.connect(self.populate_comboBox_6)
        #self.admin_inventory_add.admin_product_update_signal.connect(self.populate_table)

        barcode_regex = QRegExp(r"^\d{13}$")
        barcode_validator = QRegExpValidator(barcode_regex, self.lineEdit)
        self.lineEdit.setValidator(barcode_validator)

        self.populate_table()
        self.populate_table_2()

        self.lineEdit.textChanged.connect(self.check_barcode_length)

        self.tableWidget_2.itemSelectionChanged.connect(self.on_table_item_selected)
        self.tableWidget_3.itemSelectionChanged.connect(self.on_table_3_item_selected)

        self.int_validator = QIntValidator()
        self.lineEdit_8.setValidator(self.int_validator)

        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)

    def populate_table_2(self):
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                query = """
                    SELECT 
                        Order_ID,
                        Customer_Name,
                        Order_Type,
                        Payment_Status,
                        Priority_Order
                    FROM `order`
                    WHERE Order_Type = 'Add-ons only' AND Payment_Status = 'Pending'
                    ORDER BY Priority_Order DESC, Order_ID ASC
                """
                cursor.execute(query)
                records_2 = cursor.fetchall()
                self.display_records_2(records_2)
                self.tableWidget_3.setColumnWidth(3, 60)
                self.tableWidget_3.setColumnWidth(4, 120)

        finally:
            if conn.is_connected():
                cursor.close()

    def display_records_2(self, records_2):
        column_names = [
            "Order ID",
            "Customer Name",
            "Order Type",
            "Payment Status",
            "Priority Order"
        ]

        if records_2:
            self.tableWidget_3.setRowCount(len(records_2))
            self.tableWidget_3.setColumnCount(len(column_names))

            for j, name in enumerate(column_names):
                item = QTableWidgetItem(name)
                self.tableWidget_3.setHorizontalHeaderItem(j, item)

            for i, row in enumerate(records_2):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))  # Always convert to string
                    self.tableWidget_3.setItem(i, j, item)

                    # Apply conditional formatting for the "Priority Order" column
                    if column_names[j] == "Priority Order" and col == "Priority":
                        item.setBackground(QtGui.QColor(255, 215, 0))  # Gold color for priority

            header = self.tableWidget_3.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def on_table_3_item_selected(self):
        selected_items = self.tableWidget_3.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            order_id = self.tableWidget_3.item(selected_row, 0).text()  # Assuming 'Order ID' is in the first column
            self.lineEdit_2.setText(order_id)

    def on_table_item_selected(self):
        selected_items = self.tableWidget_2.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            product_name = self.tableWidget_2.item(selected_row, 0).text()  # Assuming 'Product Name' is in the first column
            self.lineEdit_3.setText(product_name)

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.date.setText(formattedDateTime)

    def check_barcode_length(self):
        if len(self.lineEdit.text()) == 13:
            self.scan_barcode()


    def scan_barcode(self):
        barcode = self.lineEdit.text()
        if not self.lineEdit.hasAcceptableInput():
            QMessageBox.warning(self, "Invalid Barcode", "The barcode must be 13 digits long and contain only numbers.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT product_id FROM inventory WHERE barcode = %s;", (barcode,))
            product_id = cursor.fetchone()

            if product_id:
                cursor.execute("SELECT name FROM product WHERE product_id = %s;", (product_id[0],))
                product_data = cursor.fetchone()

                if product_data:
                    product_name = product_data[0]  # Extract the string from the tuple
                    self.lineEdit_3.setText(product_name)  # Set the text of lineEdit_3
                else:
                    QMessageBox.warning(self, "Product Not Found", "Product data not found for the given barcode.")
            else:
                QMessageBox.warning(self, "Barcode Not Found", "No product found for the entered barcode.")

        except Exception as e:
            print(f"Error occurred while scanning barcode: {e}")

        finally:
            if conn.is_connected():
                cursor.close()

    def populate_table(self):
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                query = """
                    SELECT 
                        product.Name,
                        product.Category,
                        product.Quantity,
                        inventory.Selling_Cost as Price,
                        product.Threshold_Value,
                        product.Expiry_Date,
                        CASE
                            WHEN product.Quantity = 0 THEN 'Out of Stock'
                            WHEN product.Quantity <= product.Threshold_Value THEN 'Low Stock'
                            ELSE 'In Stock'
                        END as Inventory_Status
                    FROM product
                    JOIN inventory ON product.Product_ID = inventory.Product_ID
                    WHERE product.Status = 'Active'
                    AND product.Category IN ('Beverage', 'Food')
                """
                cursor.execute(query)
                records = cursor.fetchall()
                self.display_records(records)

        except Exception as e:
            print("Error occurred while populating table:", e)

        finally:
            if conn.is_connected():
                cursor.close()

    def display_records(self, records):
        column_names = [
            "Name",
            "Category",
            "Quantity",
            "Price",
            "Threshold Value",
            "Expiry Date",
            "Inventory Status"
        ]

        if records:
            self.tableWidget_2.setRowCount(len(records))
            self.tableWidget_2.setColumnCount(len(column_names))

            for j, name in enumerate(column_names):
                item = QTableWidgetItem(name)
                self.tableWidget_2.setHorizontalHeaderItem(j, item)

            for i, row in enumerate(records):
                for j, col in enumerate(row):
                    item = QTableWidgetItem("-" if col is None else str(col))
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Make cell selectable
                    # Color coding for Inventory Status
                    if j == 6:  # Assuming Inventory Status is the last column
                        if col == 'Out of Stock':
                            item.setBackground(QtGui.QColor(255, 99, 71))  # Light red
                        elif col == 'Low Stock':
                            item.setBackground(QtGui.QColor(255, 165, 0))  # Light orange
                        elif col == 'In Stock':
                            item.setBackground(QtGui.QColor(144, 238, 144))  # Light green

                    self.tableWidget_2.setItem(i, j, item)

            # Set column widths
            # self.tableWidget_2.setColumnWidth(0, 200)  # Name column width
            # self.tableWidget_2.setColumnWidth(1, 70)  # Category column width
            # self.tableWidget_2.setColumnWidth(2, 60)  # Quantity column width
            # self.tableWidget_2.setColumnWidth(3, 50)  # Price column width
            # self.tableWidget_2.setColumnWidth(4, 90)  # Threshold Value column width
            # self.tableWidget_2.setColumnWidth(5, 90)  # Expiry Date column width
            # self.tableWidget_2.setColumnWidth(6, 100)  # Inventory Status column width
            # header.tableWidget_2(QtWidgets.QHeaderView.Stretch)
            header = self.tableWidget_2.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def save_add_on(self):
        order_id = self.lineEdit_2.text()
        product_name = self.lineEdit_3.text()
        quantity = self.lineEdit_8.text()

        # Store the original style sheet of lineEdit_8
        original_style_lineEdit_8 = self.lineEdit_8.styleSheet()

        if not quantity.isdigit() or int(quantity) <= 0:
            self.lineEdit_8.setStyleSheet(original_style_lineEdit_8 + "border: 1px solid red;")
            QMessageBox.warning(self, "Invalid Input", "Error: Required Input/Quantity must be a positive integer.")
            return

        # Reset the style sheet to the original if the quantity is valid
        self.lineEdit_8.setStyleSheet(original_style_lineEdit_8 + "border: 1px solid green;")

        quantity = int(quantity)

        try:
            cursor = conn.cursor()

            # Get the product_id and current quantity for the selected product_name
            cursor.execute("SELECT Product_ID, Quantity FROM `product` WHERE Name = %s AND Status = 'Active'",
                           (product_name,))
            product_record = cursor.fetchone()
            if not product_record:
                QMessageBox.warning(self, "Invalid Product", "Selected product is not available.")
                return

            product_id, current_quantity = product_record
            if current_quantity < quantity:
                QMessageBox.warning(self, "Insufficient Stock", f"Only {current_quantity} units available in stock.")
                return

            # Check if the order_id already exists in the add_on table
            cursor.execute("SELECT Product_Details FROM `add_on` WHERE Order_ID = %s", (order_id,))
            existing_record = cursor.fetchone()

            if existing_record:
                # Order_ID exists, update the Product_Details JSON
                product_details = json.loads(existing_record[0])

                # Check if the product_id already exists in the product_details
                updated = False
                for item in product_details:
                    if item['product_id'] == product_id:
                        item['quantity'] += quantity
                        updated = True
                        break

                if not updated:
                    product_details.append({"product_id": product_id, "quantity": quantity})

                cursor.execute(
                    "UPDATE `add_on` SET Product_Details = %s WHERE Order_ID = %s",
                    (json.dumps(product_details), order_id)
                )

            else:
                # Order_ID does not exist, insert a new record
                product_details = [{"product_id": product_id, "quantity": quantity}]
                cursor.execute(
                    "INSERT INTO `add_on` (Order_ID, Product_Details) VALUES (%s, %s)",
                    (order_id, json.dumps(product_details))
                )

            # Deduct the quantity from the product table
            new_quantity = current_quantity - quantity
            cursor.execute(
                "UPDATE `product` SET Quantity = %s WHERE Product_ID = %s",
                (new_quantity, product_id)
            )

            conn.commit()
            QMessageBox.information(self, "Success", "Add-on saved successfully!")
            self.clear()

            # Refresh the table to reflect updated quantities
            self.populate_table()

        except Exception as e:
            conn.rollback()
            QMessageBox.critical(self, "Error", f"An error occurred while saving the add-on: {e}")

        finally:
            if conn.is_connected():
                cursor.close()


    def clear(self):
        self.lineEdit_8.clear()
        self.lineEdit.clear()
        self.lineEdit_8.setStyleSheet("")