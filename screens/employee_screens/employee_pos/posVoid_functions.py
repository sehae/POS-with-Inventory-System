from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QRegExpValidator, QFont
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from PyQt5.QtCore import QDateTime, QTimer, Qt
from screens.employee_screens.employee_pos.posVoid import Ui_MainWindow
from shared.navigation_signal import auth_back, pos_back
from server.local_server import conn
from validator.user_manager import userManager
from screens.employee_screens.employee_pos.posOrderdetails_functions import posOrderdetails
from decimal import Decimal
import json

class posVoid(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    back_cashier_signal = QtCore.pyqtSignal()
    checkout_signal = QtCore.pyqtSignal()
    modify_signal = QtCore.pyqtSignal()
    order_signal = QtCore.pyqtSignal()
    menu_signal = QtCore.pyqtSignal()
    history_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user_manager = userManager()

        self.backBTN.clicked.connect(lambda: pos_back(self.user_manager, self.back_signal, self.back_cashier_signal))
        self.checkoutBTN.clicked.connect(self.checkout_signal.emit)
        self.modifyBTN.clicked.connect(self.modify_signal.emit)
        self.orderBTN.clicked.connect(self.order_signal.emit)
        self.menuBTN.clicked.connect(self.menu_signal.emit)
        self.historyBTN_2.clicked.connect(self.history_signal.emit)
        self.checkBTN.clicked.connect(self.check_order_details)
        self.saveBTN.clicked.connect(self.save_order_changes)  # Connect saveBTN to save_order_changes

        self.pos_orderdetails = posOrderdetails()

        self.pos_orderdetails.transaction_generated_signal.connect(self.populate_comboBox)
        self.pos_orderdetails.update_combobox_signal.connect(self.populate_comboBox)

        self.populate_comboBox()

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        # Setting font size for the entire table
        font = QtGui.QFont()
        font.setPointSize(8)  # Set the font size to 8 points
        self.orderList.setFont(font)

        # Hide row numbers
        self.orderList.horizontalHeader().setVisible(False)

        # Connect signals for voiding items
        self.orderList.cellChanged.connect(self.validate_quantity_input)

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.date.setText(formattedDateTime)

    def populate_comboBox(self):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT Order_ID FROM `order` WHERE Payment_Status = 'Pending'")
            order_ids = cursor.fetchall()

            self.orderidBOX.clear()
            for order_id in order_ids:
                self.orderidBOX.addItem(str(order_id[0]))

        except Exception as e:
            print(f"Error occurred while populating orderidBOX: {e}")

        finally:
            if conn.is_connected():
                cursor.close()

    def check_order_details(self):
        order_id = self.orderidBOX.currentText()

        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT o.Customer_Name, o.Guest_Pax, p.Package_Name, p.Package_Price, o.Order_Type
                FROM `order` o
                LEFT JOIN `package` p ON o.Package_ID = p.Package_ID
                WHERE o.Order_ID = %s AND o.Payment_Status = 'Pending'
            """, (order_id,))
            order_details = cursor.fetchone()

            if not order_details:
                QMessageBox.warning(self, "Data Error", "No data found for the selected order.")
                return

            customer_name, guest_pax, package_name, package_price, order_type = order_details

            # Check if the order type is "Add-ons only"
            if order_type != "Add-ons only":
                QMessageBox.warning(self, "Order Type Error", "Only 'Add-ons only' orders are allowed.")
                return

            # Clear any existing rows and columns
            self.orderList.clearContents()
            self.orderList.setRowCount(0)
            self.orderList.setColumnCount(4)

            row = 0
            # Add order details header row
            self.orderList.insertRow(row)
            self.orderList.setItem(row, 0, QTableWidgetItem(f"Order Details"))
            self.orderList.setSpan(row, 0, 1, 4)
            row += 1

            # Add empty row
            self.orderList.insertRow(row)
            row += 1

            # Add add-on details header row
            self.orderList.insertRow(row)
            self.orderList.setItem(row, 0, QTableWidgetItem(f"Add-on Details"))
            self.orderList.setSpan(row, 0, 1, 4)
            row += 1

            # Fetch add-ons details
            cursor.execute("SELECT Product_Details FROM `add_on` WHERE Order_ID = %s", (order_id,))
            add_on_details = cursor.fetchone()

            if add_on_details:
                add_ons = json.loads(add_on_details[0])

                add_ons_rows = []
                for add_on in add_ons:
                    product_id = add_on['product_id']
                    quantity = add_on['quantity']

                    cursor.execute("""
                        SELECT p.Name, i.Selling_Cost
                        FROM `product` p
                        JOIN `inventory` i ON p.Product_ID = i.Product_ID
                        WHERE p.Product_ID = %s
                    """, (product_id,))
                    product_details = cursor.fetchone()
                    if product_details:
                        product_name, selling_cost = product_details
                        add_ons_rows.append((product_name, selling_cost, quantity))

                # Add headers for add-ons as a new row
                self.orderList.insertRow(row)
                self.orderList.setItem(row, 0, QTableWidgetItem("Product Name"))
                self.orderList.setItem(row, 2, QTableWidgetItem("Price"))
                self.orderList.setItem(row, 3, QTableWidgetItem("Quantity"))
                row += 1

                # Populate the table widget
                for product_name, selling_cost, quantity in add_ons_rows:
                    self.orderList.insertRow(row)
                    self.orderList.setItem(row, 0, QTableWidgetItem(product_name))
                    self.orderList.setItem(row, 2, QTableWidgetItem(f"{selling_cost:.2f}"))
                    quantity_item = QTableWidgetItem(str(quantity))
                    if product_name == "Product Name":  # Check if this is the header row
                        quantity_item.setFlags(quantity_item.flags() & ~Qt.ItemIsEditable)
                    self.orderList.setItem(row, 3, quantity_item)
                    row += 1

            else:
                QMessageBox.warning(self, "Data Error", "No add-ons found for this order.")

        except Exception as e:
            print(f"Error fetching order details: {e}")  # Debug statement
            QMessageBox.warning(self, "Error", f"Error in fetching data: {str(e)}")
        finally:
            cursor.close()

    def validate_quantity_input(self, row, column):
        if column == 3:  # Only proceed if the quantity column was changed
            item = self.orderList.item(row, column)
            if item and item.flags() & Qt.ItemIsEditable:  # Only proceed if the item is editable
                quantity_text = item.text()
                if not quantity_text.isdigit():
                    QMessageBox.warning(self, "Input Error", "Please enter a valid integer quantity.")
                    item.setText("0")  # Reset to default value
                else:
                    self.update_add_on_quantity(row)

    def update_add_on_quantity(self, row):
        try:
            cursor = conn.cursor()
            product_name = self.orderList.item(row, 0).text()
            new_quantity_item = self.orderList.item(row, 3)

            # Check if the new quantity item is valid
            if not new_quantity_item or not new_quantity_item.text().isdigit():
                QMessageBox.warning(self, "Input Error", "Please enter a valid integer quantity.")
                return

            new_quantity = int(new_quantity_item.text())

            # Fetch add-on details for the current order
            cursor.execute("""
                SELECT ao.Product_Details
                FROM `add_on` ao
                WHERE ao.Order_ID = %s
            """, (self.orderidBOX.currentText(),))
            result = cursor.fetchone()

            if result:
                product_details = result[0]
                add_ons = json.loads(product_details)

                for add_on in add_ons:
                    if add_on['product_id'] == self.get_product_id_by_name(product_name):
                        if new_quantity <= 0:
                            add_ons.remove(add_on)
                        else:
                            add_on['quantity'] = new_quantity

                updated_product_details = json.dumps(add_ons)
                cursor.execute("""
                    UPDATE `add_on`
                    SET Product_Details = %s
                    WHERE Order_ID = %s
                """, (updated_product_details, self.orderidBOX.currentText()))

                conn.commit()
                QMessageBox.information(self, "Update Successful", "Product quantity updated successfully.")
            else:
                QMessageBox.warning(self, "Data Error", "Product details not found.")

        except Exception as e:
            print(f"Error updating product quantity: {e}")
            QMessageBox.warning(self, "Error", f"Error updating quantity: {str(e)}")
        finally:
            cursor.close()

    def save_order_changes(self):
        order_id = self.orderidBOX.currentText()

        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        try:
            cursor = conn.cursor()

            add_ons = []
            row_count = self.orderList.rowCount()
            for row in range(row_count):
                product_name_item = self.orderList.item(row, 0)
                quantity_item = self.orderList.item(row, 3)

                if product_name_item and quantity_item:
                    product_name = product_name_item.text()
                    quantity = int(quantity_item.text())

                    cursor.execute("""
                        SELECT p.Product_ID
                        FROM `product` p
                        WHERE p.Name = %s
                    """, (product_name,))
                    result = cursor.fetchone()

                    if result:
                        product_id = result[0]
                        add_ons.append({'product_id': product_id, 'quantity': quantity})

            updated_product_details = json.dumps(add_ons)
            cursor.execute("""
                UPDATE `add_on`
                SET Product_Details = %s
                WHERE Order_ID = %s
            """, (updated_product_details, order_id))

            conn.commit()
            QMessageBox.information(self, "Save Successful", "Order changes saved successfully.")

        except Exception as e:
            print(f"Error saving order changes: {e}")
            QMessageBox.warning(self, "Error", f"Error saving changes: {str(e)}")
        finally:
            cursor.close()

    def get_product_id_by_name(self, product_name):
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.Product_ID
            FROM `product` p
            WHERE p.Name = %s
        """, (product_name,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else None
