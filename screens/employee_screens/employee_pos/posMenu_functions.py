from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from PyQt5.QtCore import QDateTime, QTimer

# Assuming these imports are part of your project structure
from screens.employee_screens.employee_pos.posMenu import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from screens.admin_screens.admin_inventory.inventoryAddProduct_functions import adminInventoryAddProduct

import json

class posMenu(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    checkout_signal = QtCore.pyqtSignal()
    modify_signal = QtCore.pyqtSignal()
    order_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.backBTN.clicked.connect(self.goBack)
        self.checkoutBTN.clicked.connect(self.goCheckout)
        self.modifyBTN.clicked.connect(self.goModify)
        self.orderBTN.clicked.connect(self.goOrder)
        self.pushButton_8.clicked.connect(self.save_add_on)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        self.admin_inventory_add = adminInventoryAddProduct()
        self.admin_inventory_add.admin_product_update_signal.connect(self.populate_comboBox_6)
        self.admin_inventory_add.admin_product_update_signal.connect(self.populate_table)

        self.populate_table()

        self.populate_comboBox_5()
        self.populate_comboBox_6()

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.date.setText(formattedDateTime)

    def goBack(self):
        self.back_signal.emit()

    def goCheckout(self):
        self.checkout_signal.emit()

    def goModify(self):
        self.modify_signal.emit()

    def goOrder(self):
        self.order_signal.emit()

    def populate_comboBox_5(self):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT Order_ID FROM `order` WHERE Payment_Status = 'Pending'")
            order_ids = cursor.fetchall()

            self.comboBox_5.clear()
            for order_id in order_ids:
                self.comboBox_5.addItem(str(order_id[0]))

        except Exception as e:
            print(f"Error occurred while populating comboBox_5: {e}")

        finally:
            if conn.is_connected():
                cursor.close()

    def populate_comboBox_6(self):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT Name FROM `product` WHERE Status = 'Active'")
            product_names = cursor.fetchall()

            self.comboBox_6.clear()
            for name in product_names:
                self.comboBox_6.addItem(name[0])

        except Exception as e:
            print(f"Error occurred while populating comboBox_6: {e}")

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
                        inventory.Selling_Cost as Price
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
            "Price"
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
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Make cell non-clickable

                    self.tableWidget_2.setItem(i, j, item)

            # Set column widths
            self.tableWidget_2.setColumnWidth(0, 200)  # Name column width
            self.tableWidget_2.setColumnWidth(1, 150)  # Category column width
            self.tableWidget_2.setColumnWidth(2, 100)  # Quantity column width
            self.tableWidget_2.setColumnWidth(3, 100)  # Selling Cost column width

        else:
            print("No records found for products with status 'Active' and category 'Beverage' or 'Food'.")

    def save_add_on(self):
        order_id = self.comboBox_5.currentText()
        product_name = self.comboBox_6.currentText()
        quantity = self.lineEdit_8.text()

        if not quantity.isdigit() or int(quantity) <= 0:
            QMessageBox.warning(self, "Invalid Input", "Quantity must be a positive integer.")
            return

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

            # Refresh the table to reflect updated quantities
            self.populate_table()

        except Exception as e:
            conn.rollback()
            QMessageBox.critical(self, "Error", f"An error occurred while saving the add-on: {e}")

        finally:
            if conn.is_connected():
                cursor.close()