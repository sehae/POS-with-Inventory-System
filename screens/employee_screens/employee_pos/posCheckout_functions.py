from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import QMessageBox, QInputDialog,  QHeaderView
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from screens.employee_screens.employee_pos.posCheckout import Ui_MainWindow
from screens.employee_screens.employee_pos.posOrderdetails_functions import posOrderdetails
from server.local_server import conn
from screens.receipt.checkout_receipt_dialog import CheckoutReceiptDialog
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout

import json

from shared.navigation_signal import auth_back, pos_back
from validator.user_manager import userManager

from decimal import Decimal

user_manager = userManager()

class posCheckout(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    back_cashier_signal = QtCore.pyqtSignal()
    menu_signal = QtCore.pyqtSignal()
    modify_signal = QtCore.pyqtSignal()
    order_signal = QtCore.pyqtSignal()
    history_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user_manager = userManager()

        self.backBTN.clicked.connect(lambda: pos_back(self.user_manager, self.back_signal, self.back_cashier_signal))
        self.menuBTN.clicked.connect(self.goMenu)
        self.modifyBTN.clicked.connect(self.goModify)
        self.orderBTN.clicked.connect(self.goOrder)
        self.historyBTN_2.clicked.connect(self.goHistory)
        self.setBTN.clicked.connect(self.set_changes)
        self.checkoutBTN_3.clicked.connect(self.check_order_details) #Check order id details
        self.checkoutBTN_2.clicked.connect(self.save_order_details) #Pay now save to database

        self.pos_orderdetails = posOrderdetails()

        self.orderList_2.itemSelectionChanged.connect(self.on_orderid_selected)

        self.pwdBTN.clicked.connect(self.open_id_dialog)
        self.seniorBTN.clicked.connect(self.open_id_dialog)
        self.id_dialog = IDInputDialog()

        self.populate_table_2()

        self.populate_leftoverBOX()

        self.leftoverBOX.setCurrentIndex(1)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.timeout.connect(self.populate_table_2)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        # Setting font size for the entire table
        font = QtGui.QFont()
        font.setPointSize(8)  # Set the font size to 8 points
        self.orderList.setFont(font)

        # Make table grid invisible
        self.orderList.setShowGrid(False)

        self.orderList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.orderList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Hide row numbers
        self.orderList.verticalHeader().setVisible(False)
        self.orderList.horizontalHeader().setVisible(False)

        self.orderidFIELD.setReadOnly(True)

        self.amountFIELD.setValidator(QDoubleValidator(0.00, 99999.99, 2))

        # Temporary values to be placed in the table
        self.penalty_fee = 0
        self.cash_amount = None
        self.reference_id = None
        self.payment_method = None
        self.discount_type = None
        self.leftover_grams = None
        self.leftover_id = None

        # Temporary values to be saved in order details
        self.subtotal_amount = Decimal(0)
        self.vat_amount = Decimal(0)
        self.discount_amount = Decimal(0)
        self.change_amount = Decimal(0)
        self.package_total_amount = Decimal(0)
        self.add_ons_total_amount = Decimal(0)
        self.total_amount = Decimal(0)
        self.add_ons_rows = []

        self.regularBTN.clicked.connect(self.set_regular_discount)

        # Connect the leftoverBOX selection change to update the leftover details
        self.leftoverBOX.currentIndexChanged.connect(self.update_leftover)

    def update_leftover(self):
        leftover_mapping = {
            'None (for add ons only)': None,
            '0 grams': 1,
            '100 grams': 2,
            '200 grams': 3,
            '300 grams': 4,
            '400 grams': 5
        }
        selected_text = self.leftoverBOX.currentText()
        self.leftover_id = leftover_mapping.get(selected_text, None)

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT Penalty_Fee FROM leftover WHERE Leftover_ID = %s", (self.leftover_id,))
            result = cursor.fetchone()
            if result:
                self.penalty_fee = result[0]
            else:
                self.penalty_fee = 0
        except Exception as e:
            print(f"Error fetching penalty fee: {e}")
        finally:
            cursor.close()

        # Call the check_order_details function after getting the penalty fee
        self.check_order_details()

    def set_regular_discount(self):
        order_id = self.orderidFIELD.text()

        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        self.discount_type = 'Regular'

        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE `order` SET Discount_ID = NULL, Senior_Count = NULL WHERE order_id = %s",
                (order_id,)
            )

            conn.commit()
            QMessageBox.information(self, "Success", "Regular Discount saved successfully!")
            self.check_order_details()

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to save Discount ID: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def open_id_dialog(self):
        order_id = self.orderidFIELD.text()

        if not order_id:
            QMessageBox.warning(self, "No Selection", "Please select Order ID.")
            return

        if self.sender() == self.pwdBTN:
            self.id_dialog.setWindowTitle("Enter PWD ID")
        elif self.sender() == self.seniorBTN:
            self.id_dialog.setWindowTitle("Enter Senior ID")

        if self.id_dialog.exec_():
            entered_id = self.id_dialog.get_id()
            pax_id = self.id_dialog.get_pax()

            if entered_id:
                try:
                    cursor = conn.cursor()
                    self.discount_type = "PWD" if self.sender() == self.pwdBTN else "Senior"

                    # Assuming you have an order_id or a way to associate this ID with an order
                    # Replace 'order_id' with the actual identifier of your order
                    # Update the Discount_ID in your order table
                    cursor.execute(
                        "UPDATE `order` SET Discount_ID = %s, senior_count = %s WHERE order_id = %s",
                        (entered_id, pax_id, order_id)
                    )

                    conn.commit()
                    QMessageBox.information(self, "Success", "Discount ID saved successfully!")
                    self.check_order_details()

                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Failed to save Discount ID: {str(e)}")

                finally:
                    cursor.close()
            else:
                QMessageBox.warning(self, "Invalid ID", "Please enter a valid ID.")
    def on_orderid_selected(self):
        selected_items = self.orderList_2.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            order_id = self.orderList_2.item(selected_row, 0).text()  # Assuming 'Order ID' is in the first column
            self.orderidFIELD.setText(order_id)

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
                    WHERE Payment_Status = 'Pending'
                    ORDER BY Priority_Order DESC, Order_ID ASC
                """
                cursor.execute(query)
                records_2 = cursor.fetchall()
                self.display_records_2(records_2)
                self.orderList_2.setColumnWidth(3, 60)
                self.orderList_2.setColumnWidth(4, 120)

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
            self.orderList_2.setRowCount(len(records_2))
            self.orderList_2.setColumnCount(len(column_names))

            for j, name in enumerate(column_names):
                item = QTableWidgetItem(name)
                self.orderList_2.setHorizontalHeaderItem(j, item)

            for i, row in enumerate(records_2):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))  # Always convert to string
                    self.orderList_2.setItem(i, j, item)

                    # Apply conditional formatting for the "Priority Order" column
                    if column_names[j] == "Priority Order" and col == "Priority":
                        item.setBackground(QtGui.QColor(255, 215, 0))  # Gold color for priority

            header = self.orderList_2.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def update_fullname_label(self, firstname):
        self.cashierDISPLAY.setText(firstname)

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.label_11.setText(formattedDateTime)
        self.update_fullname_label(self.user_manager.get_first_name())

    def goHistory(self):
        self.history_signal.emit()

    def goBack(self):
        self.back_signal.emit()

    def goMenu(self):
        self.menu_signal.emit()

    def goModify(self):
        self.modify_signal.emit()

    def goOrder(self):
        self.order_signal.emit()

    def set_changes(self):
        cash_amount_text = self.amountFIELD.text()
        self.reference_id = self.referenceFIELD.text()

        try:
            self.cash_amount = Decimal(cash_amount_text) if cash_amount_text else None
        except ValueError:
            self.cash_amount = None

        # Determine payment method and reference ID based on input
        if not cash_amount_text:
            self.payment_method = 'GCash'
            self.cash_amount = None
        elif not self.reference_id:
            self.payment_method = 'Cash'
            self.reference_id = None
        else:
            # If both cash amount and reference ID are provided
            self.payment_method = None
            QMessageBox.warning(self, "Input Error", "Please provide either Cash Amount or Reference ID (GCash).")
            return


        # Trigger checking of order details based on the updated values
        self.check_order_details()

    #Populate combobox leftover
    def populate_leftoverBOX(self):
        items = ['None (for add ons only)', '0 grams', '100 grams', '200 grams', '300 grams', '400 grams']
        self.leftoverBOX.addItems(items)

    def check_order_details(self):
        order_id = self.orderidFIELD.text()
        cash_amount = self.cash_amount
        reference_id = self.reference_id
        penalty_fee = self.penalty_fee
        discount_type = self.discount_type
        payment_method = self.payment_method

        try:

            cursor = conn.cursor()

            cursor.execute("""
                SELECT o.Customer_Name, o.Guest_Pax, p.Package_Name, p.Package_Price, o.Order_Type, o.Senior_Count
                FROM `order` o
                LEFT JOIN package p ON o.Package_ID = p.Package_ID
                WHERE o.Order_ID = %s AND o.Payment_Status = 'Pending'
            """, (order_id,))

            order_details = cursor.fetchone()

            customer_name, guest_pax, package_name, package_price, order_type, senior_count = order_details

            # Handle senior_count being None
            senior_count = senior_count if senior_count is not None else 0

            # Set the retrieved values to the corresponding UI elements
            self.label_4.setText(order_id)
            self.customerFIELD.setText(customer_name)
            self.packageDISPLAY.setText(package_name)
            self.paymentmethodDISPLAY.setText(payment_method)
            self.referenceidDISPLAY.setText(reference_id)
            self.cashamountDISPLAY.setText(f"{cash_amount:.2f}" if cash_amount is not None else "0.00")

            package_total_amount = 0
            if order_type == "Package":
                package_total_amount = package_price * Decimal(guest_pax) if package_price else 0

            # Fetch add-ons details
            cursor.execute("SELECT Product_Details FROM add_on WHERE Order_ID = %s", (order_id,))
            add_on_details = cursor.fetchone()

            add_ons = json.loads(add_on_details[0]) if add_on_details else []

            self.add_ons_total_amount = 0
            self.add_ons_rows = []
            for add_on in add_ons:
                product_id = add_on['product_id']
                quantity = add_on['quantity']

                cursor.execute("""
                    SELECT p.Name, i.Selling_Cost
                    FROM product p
                    JOIN inventory i ON p.Product_ID = i.Product_ID
                    WHERE p.Product_ID = %s
                """, (product_id,))
                product_details = cursor.fetchone()
                if product_details:
                    product_name, selling_cost = product_details
                    total_amount = Decimal(selling_cost) * quantity
                    self.add_ons_total_amount += total_amount

                    # Only calculate discount amount separately without changing total_amount
                    if discount_type == "Senior" or discount_type == "PWD":
                        if senior_count > 0:
                            eligible_senior_discount = min(senior_count, quantity)
                            total_discount = Decimal("0.20") * (Decimal(selling_cost) * eligible_senior_discount)
                            discount_amount = total_discount
                        else:
                            discount_amount = 0
                    elif discount_type == "Regular":
                        discount_amount = 0
                    else:
                        discount_amount = 0

                    # Only add the row if product_name is not None or empty, quantity is not None,
                    # and selling_cost and total_amount are not 0.00
                    if product_name and quantity is not None and selling_cost != Decimal(
                            "0.00") and total_amount != Decimal("0.00"):
                        self.add_ons_rows.append((product_name, quantity, selling_cost, total_amount, discount_amount))

            # Check if order type is "Add-ons only" and there are no add-ons
            if order_type == "Add-ons only" and not self.add_ons_rows:
                QMessageBox.warning(self, "Input Error", "Get products first before checking out.")
                return

            subtotal_amount = Decimal(package_total_amount) + Decimal(self.add_ons_total_amount)

            total_discount_amount = sum(
                [item[4] for item in self.add_ons_rows])  # Sum all discount amounts from add-ons

            # If order type is Package and senior_count > 0, calculate discount for package
            if discount_type in ["Senior", "PWD"] and order_type == "Package" and senior_count > 0:
                eligible_senior_discount = min(senior_count, guest_pax)
                package_discount_amount = Decimal("0.20") * (package_price * Decimal(eligible_senior_discount))
                total_discount_amount += package_discount_amount

            # Calculate discounted subtotal
            discounted_subtotal = subtotal_amount - total_discount_amount

            pinaka_total_amount = discounted_subtotal + Decimal(self.penalty_fee)

            vat_amount = Decimal("0.12") * discounted_subtotal

            self.discount_amount = total_discount_amount

            # Calculate change amount only if cash amount is entered
            change_amount = 0
            if cash_amount is not None and cash_amount > 0:
                change_amount = cash_amount - pinaka_total_amount

            # Set the calculated values to the corresponding labels
            self.packageAmountDISPLAY.setText(f"{package_total_amount:.2f}")
            self.addonsAmountDISPLAY.setText(f"{self.add_ons_total_amount:.2f}")
            self.subtotalDISPLAY.setText(f"{subtotal_amount:.2f}")
            self.vatDISPLAY.setText(f"{vat_amount:.2f}")
            self.discountDISPLAY.setText(f"{total_discount_amount:.2f}")
            self.leftoverDISPLAY.setText(f"{self.penalty_fee:.2f}")
            self.totalamountDISPLAY.setText(f"{pinaka_total_amount:.2f}")
            self.changeDISPLAY.setText(f"{change_amount:.2f}")

            # Populate the table widget
            self.orderList.setRowCount(0)  # Clear existing rows
            self.orderList.setColumnCount(5)

            row = 0
            # Add customer name row
            self.orderList.insertRow(row)
            self.orderList.setItem(row, 0, QTableWidgetItem(f"Summary of order"))
            self.orderList.setSpan(row, 0, 1, 5)
            row += 1

            if order_type == "Package":
                # Add empty row
                self.orderList.insertRow(row)
                row += 1

                # Add package details header
                self.orderList.insertRow(row)
                self.orderList.setItem(row, 0, QTableWidgetItem("Package Details"))
                self.orderList.setSpan(row, 0, 1, 5)  # Span across all columns
                row += 1

                # Add package details column headers
                self.orderList.insertRow(row)
                self.orderList.setItem(row, 0, QTableWidgetItem("Package Type"))
                self.orderList.setItem(row, 2, QTableWidgetItem("Guest Pax"))
                self.orderList.setItem(row, 3, QTableWidgetItem("Price"))
                self.orderList.setItem(row, 4, QTableWidgetItem("Total"))
                row += 1

                # Add package details
                self.orderList.insertRow(row)
                self.orderList.setItem(row, 0, QTableWidgetItem(package_name))
                self.orderList.setItem(row, 2, QTableWidgetItem(str(guest_pax)))
                self.orderList.setItem(row, 3, QTableWidgetItem(f"{package_price:.2f}" if package_price else "0.00"))
                self.orderList.setItem(row, 4, QTableWidgetItem(f"{package_total_amount:.2f}"))
                row += 1

                # Only add add-ons section if there are add-ons
                if self.add_ons_rows:
                    # Add empty row before add-ons section
                    self.orderList.insertRow(row)
                    row += 1

                    # Add add-ons header
                    self.orderList.insertRow(row)
                    self.orderList.setItem(row, 0, QTableWidgetItem("Add-ons Details"))
                    self.orderList.setSpan(row, 0, 1, 5)  # Span across all columns
                    row += 1

                    # Add add-ons column headers
                    self.orderList.insertRow(row)
                    self.orderList.setItem(row, 0, QTableWidgetItem("Product Name"))
                    self.orderList.setItem(row, 2, QTableWidgetItem("Quantity"))
                    self.orderList.setItem(row, 3, QTableWidgetItem("Price"))
                    self.orderList.setItem(row, 4, QTableWidgetItem("Total"))
                    row += 1

                    # Add add-ons details
                    for product_name, quantity, selling_cost, total_amount, discount_amount in self.add_ons_rows:
                        self.orderList.insertRow(row)
                        self.orderList.setItem(row, 0, QTableWidgetItem(product_name))
                        self.orderList.setItem(row, 2, QTableWidgetItem(str(quantity)))
                        self.orderList.setItem(row, 3, QTableWidgetItem(f"{selling_cost:.2f}"))
                        self.orderList.setItem(row, 4, QTableWidgetItem(f"{total_amount:.2f}"))
                        row += 1

            elif order_type == "Add-ons only":
                # Add add-ons header
                self.orderList.insertRow(row)
                self.orderList.setItem(row, 0, QTableWidgetItem("Add-ons Details"))
                self.orderList.setSpan(row, 0, 1, 5)  # Span across all columns
                row += 1

                # Add add-ons column headers
                self.orderList.insertRow(row)
                self.orderList.setItem(row, 0, QTableWidgetItem("Product Name"))
                self.orderList.setItem(row, 2, QTableWidgetItem("Quantity"))
                self.orderList.setItem(row, 3, QTableWidgetItem("Price"))
                self.orderList.setItem(row, 4, QTableWidgetItem("Total"))
                row += 1

                # Add add-ons details
                for product_name, quantity, selling_cost, total_amount, discount_amount in self.add_ons_rows:
                    self.orderList.insertRow(row)
                    self.orderList.setItem(row, 0, QTableWidgetItem(product_name))
                    self.orderList.setItem(row, 2, QTableWidgetItem(str(quantity)))
                    self.orderList.setItem(row, 3, QTableWidgetItem(f"{selling_cost:.2f}"))
                    self.orderList.setItem(row, 4, QTableWidgetItem(f"{total_amount:.2f}"))
                    row += 1

            self.orderList.setColumnWidth(1, 100)
            self.orderList.setColumnWidth(2, 100)
            self.orderList.setColumnWidth(3, 50)
            self.adjust_column_widths()

            self.total_amount = Decimal(pinaka_total_amount).quantize(Decimal('0.00'))
            self.change_amount = Decimal(change_amount).quantize(Decimal('0.00'))
            self.package_total_amount = Decimal(package_total_amount).quantize(Decimal('0.00'))
            self.add_ons_total_amount = Decimal(self.add_ons_total_amount).quantize(Decimal('0.00'))
            self.vat_amount = Decimal(vat_amount).quantize(Decimal('0.00'))
            self.subtotal_amount = Decimal(subtotal_amount).quantize(Decimal('0.00'))

            conn.commit()
        except Exception as e:
            print(f"Error fetching order details: {e}")  # Handle exception more gracefully
        finally:
            cursor.close()

    def adjust_column_widths(self):
        header = self.orderList.horizontalHeader()
        # Set resize mode for all columns except column 4 (index 3)
        for col in range(self.orderList.columnCount()):
            if col != 1 and col != 2 and col != 3:
                header.setSectionResizeMode(col, QHeaderView.ResizeToContents)
            else:
                header.setSectionResizeMode(col, QHeaderView.Fixed)

    def save_order_details(self):
        order_id = self.orderidFIELD.text()

        # Check if either cash amount or reference ID is set
        if not self.cash_amount and not self.referenceFIELD.text():
            QMessageBox.warning(self, "Payment Details Required",
                                "Please set either the cash amount or the reference ID before checkout.")
            return

        # Check if change amount is negative
        if self.change_amount < 0:
            QMessageBox.warning(self, "Invalid Payment", "Change amount cannot be negative.")
            return

        try:
            self.print_receipt()

            cashier_name = self.user_manager.get_first_name()
            # Update the order table with relevant fields
            cursor = conn.cursor()

            # Insert or update order details in the database
            cursor.execute("""
                UPDATE `order` SET 
                Total_Amount = %s, Subtotal_Amount = %s, VAT_Amount = %s, Discount_Amount = %s, Change_Amount = %s, 
                Package_Total_Amount = %s, Add_Ons_Total_Amount = %s, Discount_Type = %s, Leftover_ID = %s, 
                Cash_Amount = %s, Reference_ID = %s, Payment_Method = %s, Payment_Status = 'Completed', 
                Cash_Register = %s, Time_Status = %s
                WHERE Order_ID = %s
            """, (self.total_amount, self.subtotal_amount, self.vat_amount, self.discount_amount, self.change_amount,
                  self.package_total_amount, self.add_ons_total_amount, self.discount_type, self.leftover_id,
                  self.cash_amount, self.reference_id, self.payment_method, cashier_name, 'Completed', order_id))

            conn.commit()

            self.reset_checkout()

        except Exception as e:
            print(f"Error updating order details: {e}")  # Debug statement
            QMessageBox.warning(self, "Error", f"Error in updating data: {str(e)}")
        finally:
            cursor.close()

    def print_receipt(self):
        order_id = self.orderidFIELD.text()

        try:
            cursor = conn.cursor()
            # Fetch basic order details
            cursor.execute("""
                SELECT o.Customer_Name, o.Guest_Pax, p.Package_Name, p.Package_Price, o.Order_Type
                FROM `order` o
                LEFT JOIN package p ON o.Package_ID = p.Package_ID
                WHERE o.Order_ID = %s
            """, (order_id,))
            order_details = cursor.fetchone()

            if not order_details:
                QMessageBox.warning(self, "Data Error", "No data found for the selected order.")
                return

            customer_name, guest_pax, package_name, package_price, order_type = order_details
            customer_name = customer_name if customer_name is not None else ''
            guest_pax = guest_pax if guest_pax is not None else 0
            package_price = float(package_price) if package_price else 0.00

            receipt_lines = [
                "MOON HEY HOTPOT AND GRILL",
                "848A Banawe St, Quezon City, 1114 Metro Manila",
                "Contact Number: 0917 123 4567",
                '=' * 48,
                "Sales Invoice",
                f"Date & Time: {QDateTime.currentDateTime().toString('MMMM d, yyyy, hh:mm:ss AP')}",
                f"Order ID: {order_id}",
                f"Customer Name: {customer_name}",
            ]

            if order_type == "Package":
                receipt_lines.extend([
                    "Package Details",
                    f"{'Package Type':<20}: {package_name}",
                    f"{'Guest Pax':<20}: {guest_pax}",
                    f"{'Price':<20}: {package_price:.2f}",
                ])

            # Fetch add-ons details from the JSON column in the add_on table
            cursor.execute("SELECT Product_Details FROM add_on WHERE Order_ID = %s", (order_id,))
            result = cursor.fetchone()
            add_ons_data = json.loads(result[0]) if result else []

            if add_ons_data:
                receipt_lines.append("Add-ons:")
                for add_on in add_ons_data:
                    product_id = add_on['product_id']
                    quantity = add_on['quantity']
                    cursor.execute("""
                        SELECT p.Name, i.Selling_Cost
                        FROM product p
                        JOIN inventory i ON p.Product_ID = i.Product_ID
                        WHERE p.Product_ID = %s
                    """, (product_id,))
                    product_info = cursor.fetchone()
                    if product_info:
                        product_name, selling_cost = product_info
                        receipt_lines.append(f"{product_name:<20} x {quantity:<3} @ {selling_cost:.2f} each")

            receipt_lines.extend([
                f"VAT (12%): {self.vat_amount:.2f}",
                f"Discount: {self.discount_amount:.2f}",
                f"Total Amount: {self.totalamountDISPLAY.text()}",
                '=' * 48
            ])

            receipt_text = '\n'.join(receipt_lines)

            # Show receipt in a dialog
            dialog = CheckoutReceiptDialog(receipt_text)
            dialog.exec_()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error generating receipt: {str(e)}")

    def reset_checkout(self):
        self.penalty_fee = 0
        self.cash_amount = None
        self.reference_id = None
        self.payment_method = None
        self.discount_type = None
        self.leftover_grams = None
        self.leftover_id = None

        self.amountFIELD.clear()
        self.referenceFIELD.clear()
        self.orderidFIELD.clear()

        self.leftoverBOX.setCurrentIndex(1)

        # Clear only the rows in the table widget
        self.orderList_2.setRowCount(0)
        self.orderList_2.clearContents()

        self.orderList.clearContents()
        self.orderList.setRowCount(0)

        self.label_4.setText('')
        self.customerFIELD.setText('')
        self.packageDISPLAY.setText('')
        self.paymentmethodDISPLAY.setText('')
        self.referenceidDISPLAY.setText('')
        self.cashamountDISPLAY.setText('')
        self.packageAmountDISPLAY.setText('')
        self.addonsAmountDISPLAY.setText('')
        self.subtotalDISPLAY.setText('')
        self.vatDISPLAY.setText('')
        self.discountDISPLAY.setText('')
        self.leftoverDISPLAY.setText('')
        self.totalamountDISPLAY.setText('')
        self.changeDISPLAY.setText('')

        self.subtotal_amount = Decimal(0)
        self.vat_amount = Decimal(0)
        self.discount_amount = Decimal(0)
        self.change_amount = Decimal(0)
        self.package_total_amount = Decimal(0)
        self.add_ons_total_amount = Decimal(0)
        self.total_amount = Decimal(0)
        self.add_ons_rows = []

class IDInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enter ID")
        self.id_input = QLineEdit()
        self.pax_input = QLineEdit()

        pax_validator = QIntValidator(1, 9)
        self.pax_input.setValidator(pax_validator)

        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Number of PWD/Senior applying for discount:"))
        layout.addWidget(self.pax_input)
        layout.addWidget(QLabel("Enter ID:"))
        layout.addWidget(self.id_input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.cancel_button)
        self.setLayout(layout)

        self.save_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def get_id(self):
        return self.id_input.text()

    def get_pax(self):
        return self.pax_input.text()