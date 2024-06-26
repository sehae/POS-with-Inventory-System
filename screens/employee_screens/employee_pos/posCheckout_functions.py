from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
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
        self.pushButton_5.clicked.connect(self.apply_discount)
        self.pushButton_2.clicked.connect(self.receipt_generation)
        self.pushButton.clicked.connect(self.set_leftover_level)

        self.populate_comboBox()

        self.populate_comboBox_4()

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

        self.lineEdit.setValidator(QDoubleValidator(0.00, 99999.99, 2))
        self.lineEdit.returnPressed.connect(self.add_cash_amount)

        self.lineEdit_2.returnPressed.connect(self.add_referenceid)

        self.penalty_fee = 0

    def receipt_generation(self):
        order_id = self.comboBox.currentText()
        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        try:
            cursor = conn.cursor()

            # Calculate pinaka_total_amount again to ensure accuracy
            cursor.execute("""
                SELECT 
                    o.Package_ID, o.Guest_Pax, p.Package_Price, o.Order_Type, o.Cash_Amount
                FROM 
                    `order` o
                LEFT JOIN 
                    `package` p ON o.Package_ID = p.Package_ID
                WHERE 
                    o.Order_ID = %s AND o.Payment_Status = 'Pending'
            """, (order_id,))
            order_details = cursor.fetchone()

            if not order_details:
                QMessageBox.warning(self, "Data Error", "No data found for the selected order.")
                return

            package_id, guest_pax, package_price, order_type, cash_amount = order_details

            package_total_amount = 0
            if order_type == "Package":
                package_total_amount = float(package_price) * guest_pax if package_price else 0

            # Fetch add-ons details
            cursor.execute("SELECT Product_Details FROM `add_on` WHERE Order_ID = %s", (order_id,))
            add_on_details = cursor.fetchone()

            add_ons_total_amount = 0
            add_ons = json.loads(add_on_details[0]) if add_on_details else []
            for add_on in add_ons:
                product_id = add_on['product_id']
                quantity = add_on['quantity']

                cursor.execute("""
                    SELECT i.Selling_Cost
                    FROM `product` p
                    JOIN `inventory` i ON p.Product_ID = i.Product_ID
                    WHERE p.Product_ID = %s
                """, (product_id,))
                product_details = cursor.fetchone()
                if product_details:
                    selling_cost = product_details[0]
                    total_amount = float(selling_cost) * quantity
                    add_ons_total_amount += total_amount

            subtotal_amount = package_total_amount + add_ons_total_amount

            # Apply discount if any
            discount_amount = 0
            discount_type = None
            cursor.execute("SELECT Discount_Type FROM `order` WHERE Order_ID = %s", (order_id,))
            discount_type = cursor.fetchone()[0]

            if discount_type == "Senior/PWD":
                discount_amount = 0.20 * subtotal_amount

            discounted_subtotal = subtotal_amount - discount_amount
            vat_amount = 0.12 * discounted_subtotal

            pinaka_total_amount = round(discounted_subtotal + vat_amount + float(self.penalty_fee), 2)
            formatted_total_amount = "{:.2f}".format(pinaka_total_amount)

            # Update order table with total_amount and Payment_Status
            cursor.execute("""
                UPDATE `order`
                SET total_amount = %s, Payment_Status = 'Completed', Time_Status = 'Completed'
                WHERE Order_ID = %s
            """, (formatted_total_amount, order_id))
            conn.commit()

            QMessageBox.information(self, "Checkout", "Checkout is completed")

            # Clear UI elements
            self.comboBox.setCurrentIndex(-1)
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Error occurred while checking out: {e}")
        finally:
            cursor.close()

    def add_referenceid(self):
        reference_id = self.lineEdit_2.text()
        order_id = self.comboBox.currentText()
        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                        UPDATE `order`
                        SET reference_id = %s, payment_method = 'GCash'
                        WHERE Order_ID = %s
                    """, (reference_id, order_id))
            conn.commit()
            QMessageBox.information(self, "Payment Method Set", "Reference ID has been saved.")
            self.check_order_details()  # Refresh the order details to show the GCash Reference ID
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Error occurred while setting payment method as GCash: {e}")
        finally:
            cursor.close()

    def add_cash_amount(self):
        cash_amount = self.lineEdit.text()
        order_id = self.comboBox.currentText()
        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                        UPDATE `order`
                        SET cash_amount = %s, payment_method = 'Cash'
                        WHERE Order_ID = %s
                    """, (cash_amount, order_id))
            conn.commit()
            QMessageBox.information(self, "Cash Amount Applied", "Cash Amount has been added.")
            self.check_order_details()  # Refresh the order details to show the discount
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Error occurred while applying discount: {e}")
        finally:
            cursor.close()

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

    def apply_discount(self):
        order_id = self.comboBox.currentText()
        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE `order`
                SET Discount_Type = 'Senior/PWD'
                WHERE Order_ID = %s
            """, (order_id,))
            conn.commit()
            QMessageBox.information(self, "Discount Applied", "Senior/PWD discount has been applied.")
            self.check_order_details()  # Refresh the order details to show the discount
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Error occurred while applying discount: {e}")
        finally:
            cursor.close()

    def set_cash_payment(self):
        order_id = self.comboBox.currentText()
        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        cash_amount_text = self.lineEdit.text()
        if not cash_amount_text:
            QMessageBox.warning(self, "Input Error", "Please enter the cash amount.")
            return

        try:
            cash_amount = round(float(cash_amount_text), 2)
            if cash_amount <= 0:
                raise ValueError("Cash amount must be greater than 0.")
        except ValueError as ve:
            QMessageBox.warning(self, "Input Error", f"Invalid cash amount: {ve}")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE `order`
                SET Payment_Method = 'Cash', Cash_Amount = %s
                WHERE Order_ID = %s
            """, (cash_amount, order_id))
            conn.commit()
            QMessageBox.information(self, "Payment Method Set", "Payment method has been set to Cash.")
            self.check_order_details()  # Refresh the order details to show the payment method
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Error occurred while setting payment method: {e}")
        finally:
            cursor.close()

    def check_order_details(self):
        order_id = self.comboBox.currentText()

        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        cash_amount_text = self.lineEdit.text()
        try:
            cash_amount = float(cash_amount_text) if cash_amount_text else 0.0
        except ValueError:
            cash_amount = 0.0

        try:
            cursor = conn.cursor()

            # Fetch customer name, package details, guest pax, order type, discount type, and cash amount from the order
            cursor.execute("""
                SELECT o.Customer_Name, o.Guest_Pax, p.Package_Name, p.Package_Price, o.Order_Type, o.Discount_Type
                FROM `order` o
                LEFT JOIN `package` p ON o.Package_ID = p.Package_ID
                WHERE o.Order_ID = %s AND o.Payment_Status = 'Pending'
            """, (order_id,))
            order_details = cursor.fetchone()
            if not order_details:
                QMessageBox.warning(self, "Data Error", "No data found for the selected order.")
                return

            customer_name, guest_pax, package_name, package_price, order_type, discount_type = order_details

            package_total_amount = 0
            if order_type == "Package":
                package_total_amount = float(package_price) * guest_pax if package_price else 0

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
                    total_amount = float(selling_cost) * quantity
                    add_ons_total_amount += total_amount
                    add_ons_rows.append((product_name, quantity, selling_cost, total_amount))

            subtotal_amount = package_total_amount + add_ons_total_amount

            discount_amount = 0

            if discount_type == "Senior/PWD":
                discount_amount = 0.20 * subtotal_amount

            reference_id = 0

            discounted_subtotal = subtotal_amount - discount_amount
            vat_amount = 0.12 * discounted_subtotal

            pinaka_total_amount = discounted_subtotal + vat_amount + float(self.penalty_fee)

            # Calculate change amount only if cash amount is entered
            change_amount = 0
            if cash_amount > 0:
                change_amount = cash_amount - pinaka_total_amount

            # Populate the table widget
            self.tableWidget.setRowCount(0)  # Clear existing rows
            self.tableWidget.setColumnCount(6)

            row = 0
            # Add customer name row
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(f"Customer Name: {customer_name}"))
            self.tableWidget.setSpan(row, 0, 1, 6)
            row += 1

            if order_type == "Package":
                # Add empty row
                self.tableWidget.insertRow(row)
                row += 1

                # Add package details header
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem("Package Details"))
                self.tableWidget.setSpan(row, 0, 1, 6)  # Span across all columns
                row += 1

                # Add package details column headers
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem("Package Type"))
                self.tableWidget.setItem(row, 2, QTableWidgetItem("Guest Pax"))
                self.tableWidget.setItem(row, 3, QTableWidgetItem("Price"))
                self.tableWidget.setItem(row, 5, QTableWidgetItem("Total"))
                row += 1

                # Add package details
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(package_name))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(guest_pax)))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{package_price:.2f}" if package_price else "0.00"))
                self.tableWidget.setItem(row, 5, QTableWidgetItem(f"{package_total_amount:.2f}"))
                row += 1

                # Only add add-ons section if there are add-ons
                if add_ons_rows:
                    # Add empty row before add-ons section
                    self.tableWidget.insertRow(row)
                    row += 1

                    # Add add-ons header
                    self.tableWidget.insertRow(row)
                    self.tableWidget.setItem(row, 0, QTableWidgetItem("Add-ons Details"))
                    self.tableWidget.setSpan(row, 0, 1, 6)  # Span across all columns
                    row += 1

                    # Add add-ons column headers
                    self.tableWidget.insertRow(row)
                    self.tableWidget.setItem(row, 0, QTableWidgetItem("Product Name"))
                    self.tableWidget.setItem(row, 2, QTableWidgetItem("Quantity"))
                    self.tableWidget.setItem(row, 3, QTableWidgetItem("Price"))
                    self.tableWidget.setItem(row, 5, QTableWidgetItem("Total"))
                    row += 1

                    # Add add-ons details
                    for product_name, quantity, selling_cost, total_amount in add_ons_rows:
                        self.tableWidget.insertRow(row)
                        self.tableWidget.setItem(row, 0, QTableWidgetItem(product_name))
                        self.tableWidget.setItem(row, 2, QTableWidgetItem(str(quantity)))
                        self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{selling_cost:.2f}"))
                        self.tableWidget.setItem(row, 5, QTableWidgetItem(f"{total_amount:.2f}"))
                        row += 1


            elif order_type == "Add-ons only" and add_ons_rows:
                # Add empty row
                self.tableWidget.insertRow(row)
                row += 1

                # Add add-ons header
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem("Add-ons"))
                self.tableWidget.setSpan(row, 0, 1, 6)  # Span across all columns
                row += 1

                # Add add-ons column headers
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem("Product Name"))
                self.tableWidget.setItem(row, 1, QTableWidgetItem("Quantity"))
                self.tableWidget.setItem(row, 2, QTableWidgetItem("Price"))
                self.tableWidget.setItem(row, 5, QTableWidgetItem("Total"))
                row += 1

                # Add add-ons details
                for product_name, quantity, selling_cost, total_amount in add_ons_rows:
                    self.tableWidget.insertRow(row)
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(product_name))
                    self.tableWidget.setItem(row, 1, QTableWidgetItem(str(quantity)))
                    self.tableWidget.setItem(row, 2, QTableWidgetItem(f"{selling_cost:.2f}"))
                    self.tableWidget.setItem(row, 5, QTableWidgetItem(f"{total_amount:.2f}"))
                    row += 1

            # Add empty row before total
            self.tableWidget.insertRow(row)
            row += 1

            # Add subtotal, discount, VAT, total, cash amount, and change amount rows
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem("Subtotal"))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(f"{subtotal_amount:.2f}"))
            row += 1

            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem("VAT (12%)"))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(f"{vat_amount:.2f}"))
            row += 1

            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem("Senior/PWD Discount"))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(f"{discount_amount:.2f}"))
            row += 1

            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem("Leftover Cost"))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(f"{self.penalty_fee:.2f}"))
            row += 1

            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem("Total"))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(f"{pinaka_total_amount:.2f}"))
            row += 1

            self.tableWidget.insertRow(row)
            row += 1

            if cash_amount > 0:
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem("Payment Method: Cash"))
                self.tableWidget.setSpan(row, 0, 1, 6)  # Span across all columns
                row += 1

                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem("Cash Amount"))
                self.tableWidget.setItem(row, 5, QTableWidgetItem(f"{cash_amount:.2f}"))
                row += 1

                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem("Change Amount"))
                self.tableWidget.setItem(row, 5, QTableWidgetItem(f"{change_amount:.2f}"))
                row += 1

            if reference_id > 0:
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem("Payment Method: GCash"))
                self.tableWidget.setSpan(row, 0, 1, 6)  # Span across all columns
                row += 1

                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem("Reference ID"))
                self.tableWidget.setItem(row, 5, QTableWidgetItem(f"{reference_id}"))
                row += 1



            self.adjust_column_widths()

            conn.commit()
            cursor.close()

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error in fetching data: {str(e)}")

    def populate_comboBox_4(self):
        items = ['1', '2', '3', '4', '5']
        self.comboBox_4.addItems(items)

    def adjust_column_widths(self):
        # Adjusting the width of the first column based on the content
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

    def apply_discount(self):
        order_id = self.comboBox.currentText()
        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE `order`
                SET Discount_Type = 'Senior/PWD'
                WHERE Order_ID = %s
            """, (order_id,))
            conn.commit()
            QMessageBox.information(self, "Discount Applied", "Senior/PWD discount has been applied.")
            self.check_order_details()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Error occurred while applying discount: {e}")
        finally:
            cursor.close()

    def set_leftover_level(self):
        order_id = self.comboBox.currentText()
        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        try:
            cursor = conn.cursor()

            # Get the selected leftover_id from comboBox_4
            leftover_id = self.comboBox_4.currentText()

            # Update the order with the selected leftover_id
            cursor.execute("""
                        UPDATE `order`
                        SET Leftover_ID = %s
                        WHERE Order_ID = %s
                    """, (leftover_id, order_id))
            conn.commit()

            # Retrieve the penalty_fee for the selected leftover_id
            cursor.execute("SELECT Penalty_Fee FROM `leftover` WHERE Leftover_ID = %s", (leftover_id,))
            result = cursor.fetchone()

            if result:
                self.penalty_fee = result[0]
            else:
                self.penalty_fee = 0

            # Update the order details display
            self.check_order_details()

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error updating leftover level: {str(e)}")
        finally:
            cursor.close()


