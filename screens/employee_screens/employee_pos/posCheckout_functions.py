from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget
from screens.employee_screens.employee_pos.posCheckout import Ui_MainWindow
from screens.employee_screens.employee_pos.posOrderdetails_functions import posOrderdetails
from server.local_server import conn

import json

class posCheckout(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    menu_signal = QtCore.pyqtSignal()
    modify_signal = QtCore.pyqtSignal()
    order_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.backBTN.clicked.connect(self.goBack)
        self.menuBTN.clicked.connect(self.goMenu)
        self.modifyBTN.clicked.connect(self.goModify)
        self.orderBTN.clicked.connect(self.goOrder)
        self.pushButton_11.clicked.connect(self.discard)
        self.pushButton_10.clicked.connect(self.check_order_details)
        self.pushButton.clicked.connect(self.cancel_order)

        self.populate_comboBox()

        self.pos_orderdetails = posOrderdetails()

        self.pos_orderdetails.transaction_generated_signal.connect(self.populate_comboBox)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        # Setting font size for the entire table
        font = QtGui.QFont()
        font.setPointSize(15)  # Set the font size to 15 points
        self.tableWidget.setFont(font)

        # Make table grid invisible
        self.tableWidget.setShowGrid(False)

        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Hide row numbers
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.label_11.setText(formattedDateTime)

    def goBack(self):
        self.back_signal.emit()

    def goMenu(self):
        self.menu_signal.emit()

    def goModify(self):
        self.modify_signal.emit()

    def goOrder(self):
        self.order_signal.emit()

    def discard(self):
        self.comboBox.setCurrentIndex(-1)
        self.tableWidget.clearContents()  # Clear table contents when discard is used
        self.tableWidget.setRowCount(0)  # Remove all rows

    def populate_comboBox(self):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT Order_ID FROM `order` WHERE Payment_Status = 'Pending'")
            order_ids = cursor.fetchall()

            self.comboBox.clear()
            for order_id in order_ids:
                self.comboBox.addItem(str(order_id[0]))

        except Exception as e:
            print(f"Error occurred while populating comboBox_5: {e}")

        finally:
            if conn.is_connected():
                cursor.close()

    def check_order_details(self):
        order_id = self.comboBox.currentText()
        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        try:
            cursor = conn.cursor()

            # Fetch customer name, package details, and guest pax from the order
            cursor.execute("""
                SELECT o.Customer_Name, o.Guest_Pax, p.Package_Name, p.Package_Price
                FROM `order` o
                JOIN `package` p ON o.Package_ID = p.Package_ID
                WHERE o.Order_ID = %s AND o.Payment_Status = 'Pending'
            """, (order_id,))
            order_details = cursor.fetchone()
            if not order_details:
                QMessageBox.warning(self, "Data Error", "No data found for the selected order.")
                return

            customer_name, guest_pax, package_name, package_price = order_details

            # Calculate package total amount
            package_total_amount = package_price * guest_pax

            # Fetch add-ons details
            cursor.execute("SELECT Product_Details FROM `add_on` WHERE Order_ID = %s", (order_id,))
            add_on_details = cursor.fetchone()
            add_ons = json.loads(add_on_details[0]) if add_on_details else []

            add_ons_total_amount = 0
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
                    total_amount = selling_cost * quantity
                    add_ons_total_amount += total_amount
                    add_ons_rows.append((product_name, quantity, selling_cost, total_amount))

            subtotal_amount = package_total_amount + add_ons_total_amount

            # Populate the table widget
            self.tableWidget.setRowCount(0)  # Clear existing rows
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["Item", "Quantity", "Price", "Total Amount"])

            row = 0
            # Add customer name row
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(f"Customer Name: {customer_name}"))
            self.tableWidget.setSpan(row, 0, 1, 4)  # Span across all columns
            row += 1

            # Add empty row
            self.tableWidget.insertRow(row)
            row += 1

            # Add package details header
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem("Package Details"))
            self.tableWidget.setSpan(row, 0, 1, 4)  # Span across all columns
            row += 1

            # Add package details column headers
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem("Package Type"))
            self.tableWidget.setItem(row, 1, QTableWidgetItem("Guest Pax"))
            self.tableWidget.setItem(row, 2, QTableWidgetItem("Price"))
            self.tableWidget.setItem(row, 3, QTableWidgetItem("Total"))
            row += 1

            # Add package details
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(package_name))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(guest_pax)))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(f"{package_price:.2f}"))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{package_total_amount:.2f}"))
            row += 1

            # Add empty row before add-ons section
            self.tableWidget.insertRow(row)
            row += 1

            # Add add-ons header
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem("Add-ons"))
            self.tableWidget.setSpan(row, 0, 1, 4)  # Span across all columns
            row += 1

            # Add add-ons column headers
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem("Product Name"))
            self.tableWidget.setItem(row, 1, QTableWidgetItem("Quantity"))
            self.tableWidget.setItem(row, 2, QTableWidgetItem("Price"))
            self.tableWidget.setItem(row, 3, QTableWidgetItem("Total"))
            row += 1

            # Add add-ons details
            for product_name, quantity, selling_cost, total_amount in add_ons_rows:
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(product_name))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(quantity)))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(f"{selling_cost:.2f}"))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{total_amount:.2f}"))
                row += 1

            # Add empty row before add-ons section
            self.tableWidget.insertRow(row)
            row += 1

            # Add subtotal amount row
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 2, QTableWidgetItem("Subtotal"))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{subtotal_amount:.2f}"))

            # Manually adjust column widths
            self.tableWidget.setColumnWidth(0, 325)  # Adjust as needed
            self.tableWidget.setColumnWidth(1, 170)
            self.tableWidget.setColumnWidth(2, 150)
            self.tableWidget.setColumnWidth(3, 120)

        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Error occurred while fetching order details: {e}")

        finally:
            if conn.is_connected():
                cursor.close()

    def cancel_order(self):
        order_id = self.comboBox.currentText()
        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        # Confirm cancellation with the user
        reply = QMessageBox.question(self, 'Confirm Cancel', f"Are you sure you want to cancel order ID {order_id}?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                cursor = conn.cursor()
                cursor.execute("UPDATE `order` SET Payment_Status = 'Cancelled' WHERE Order_ID = %s", (order_id,))
                conn.commit()

                QMessageBox.information(self, "Order Cancelled", "The order has been successfully cancelled.")
                self.populate_comboBox()  # Refresh the combo box

            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Error occurred while cancelling the order: {e}")

            finally:
                if conn.is_connected():
                    cursor.close()
        else:
            QMessageBox.information(self, "Cancelled", "Cancellation operation cancelled by user.")