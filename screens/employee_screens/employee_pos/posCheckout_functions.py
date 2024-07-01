from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QMessageBox, QInputDialog,  QHeaderView
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from screens.employee_screens.employee_pos.posCheckout import Ui_MainWindow
from screens.employee_screens.employee_pos.posOrderdetails_functions import posOrderdetails
from server.local_server import conn
from screens.receipt.checkout_receipt_dialog import CheckoutReceiptDialog

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
        self.saveBTN.clicked.connect(self.save_changes)
        self.checkoutBTN_3.clicked.connect(self.check_order_details) #Check order id details
        self.checkoutBTN_2.clicked.connect(self.save_order_details) #Pay now save to database

        self.pos_orderdetails = posOrderdetails()

        self.pos_orderdetails.transaction_generated_signal.connect(self.populate_comboBox)
        self.pos_orderdetails.update_combobox_signal.connect(self.populate_comboBox)

        #Populate orderidBOX
        self.populate_comboBox()
        self.populate_discountBOX()
        self.populate_leftoverBOX()

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

        # Make table grid invisible
        self.orderList.setShowGrid(False)

        self.orderList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.orderList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Hide row numbers
        self.orderList.verticalHeader().setVisible(False)
        self.orderList.horizontalHeader().setVisible(False)

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

    def populate_discountBOX(self):
        items = ['Regular', 'PWD', 'Senior']
        self.discountBOX.addItems(items)

    def update_fullname_label(self, fullname):
        self.cashierDISPLAY.setText(fullname)

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.label_11.setText(formattedDateTime)
        self.update_fullname_label(self.user_manager.get_current_fullname())

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


    def save_changes(self):
        # Ensure order ID is selected
        order_id = self.orderidBOX.currentText()
        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return


        self.leftover_grams = self.leftoverBOX.currentText()
        self.discount_type = self.discountBOX.currentText()

        # Determine leftover_id based on leftover_grams
        leftover_mapping = {
            '': None,
            '0 grams': 1,
            '<= 100 grams': 2,
            '<= 200 grams': 3,
            '<= 300 grams': 4,
            '<= 400 grams': 5
        }
        self.leftover_id = leftover_mapping.get(self.leftover_grams, None)
        print(f"Leftover ID: {self.leftover_id}")  # Debug statement

        # Ensure order ID is selected
        order_id = self.orderidBOX.currentText()
        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        try:
            cursor = conn.cursor()

            # Retrieve the penalty_fee for the selected leftover_id
            cursor.execute("SELECT Penalty_Fee FROM `leftover` WHERE Leftover_ID = %s", (self.leftover_id,))
            result = cursor.fetchone()

            if result:
                self.penalty_fee = result[0]
            else:
                self.penalty_fee = 0

            self.check_order_details()

        except Exception as e:
            print(f"Error updating order details: {e}")
            QMessageBox.warning(self, "Error", f"Error in updating data: {str(e)}")
        finally:
            cursor.close()


    #Populate combobox leftover
    def populate_leftoverBOX(self):
        items = ['', '0 grams', '<= 100 grams', '<= 200 grams', '<= 300 grams', '<= 400 grams']
        self.leftoverBOX.addItems(items)

    def check_order_details(self):
        order_id = self.orderidBOX.currentText()
        cash_amount = self.cash_amount
        reference_id = self.reference_id
        penalty_fee = self.penalty_fee
        discount_type = self.discount_type
        payment_method = self.payment_method

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
            cursor.execute("SELECT Product_Details FROM `add_on` WHERE Order_ID = %s", (order_id,))
            add_on_details = cursor.fetchone()

            add_ons = json.loads(add_on_details[0]) if add_on_details else []

            self.add_ons_total_amount = 0
            self.add_ons_rows = []
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
                    total_amount = Decimal(selling_cost) * quantity
                    self.add_ons_total_amount += total_amount

                    # Only add the row if product_name is not None or empty, quantity is not None,
                    # and selling_cost and total_amount are not 0.00
                    if product_name and quantity is not None and selling_cost != Decimal(
                            "0.00") and total_amount != Decimal("0.00"):
                        self.add_ons_rows.append((product_name, quantity, selling_cost, total_amount))

            subtotal_amount = Decimal(package_total_amount) + Decimal(self.add_ons_total_amount)

            discount_amount = Decimal(0)

            if discount_type == "Senior" or discount_type == "PWD":
                discount_amount = Decimal("0.20") * subtotal_amount
            elif discount_type == "Regular":
                discount_amount = Decimal("0.00") * subtotal_amount

            # Calculate discounted subtotal
            discounted_subtotal = subtotal_amount - discount_amount

            vat_amount = Decimal("0.12") * discounted_subtotal

            pinaka_total_amount = discounted_subtotal + vat_amount + Decimal(self.penalty_fee)

            self.discount_amount = discount_amount

            # Calculate change amount only if cash amount is entered
            change_amount = 0
            if cash_amount is not None and cash_amount > 0:
                change_amount = cash_amount - pinaka_total_amount

            # Set the calculated values to the corresponding labels
            self.packageAmountDISPLAY.setText(f"{package_total_amount:.2f}")
            self.addonsAmountDISPLAY.setText(f"{self.add_ons_total_amount:.2f}")
            self.subtotalDISPLAY.setText(f"{subtotal_amount:.2f}")
            self.vatDISPLAY.setText(f"{vat_amount:.2f}")
            self.discountDISPLAY.setText(f"{discount_amount:.2f}")
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
                    for product_name, quantity, selling_cost, total_amount in self.add_ons_rows:
                        self.orderList.insertRow(row)
                        self.orderList.setItem(row, 0, QTableWidgetItem(product_name))
                        self.orderList.setItem(row, 2, QTableWidgetItem(str(quantity)))
                        self.orderList.setItem(row, 3, QTableWidgetItem(f"{selling_cost:.2f}"))
                        self.orderList.setItem(row, 4, QTableWidgetItem(f"{total_amount:.2f}"))
                        row += 1

            elif order_type == "Add-ons only" and self.add_ons_rows:
                # Add empty row
                self.orderList.insertRow(row)
                row += 1

                # Add add-ons header
                self.orderList.insertRow(row)
                self.orderList.setItem(row, 0, QTableWidgetItem("Add-ons"))
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
                for product_name, quantity, selling_cost, total_amount in self.add_ons_rows:
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
        order_id = self.orderidBOX.currentText()

        # Check if cash amount and reference ID are set
        if not self.cash_amount:
            QMessageBox.warning(self, "Payment Details Required", "Please set the cash amount before checkout.")
            return

        try:
            # Update the order table with relevant fields
            cursor = conn.cursor()
            # Insert or update order details in the database
            cursor.execute("""
                UPDATE `order` SET 
                Total_Amount = %s, Subtotal_Amount = %s, VAT_Amount = %s, Discount_Amount = %s, Change_Amount = %s, 
                Package_Total_Amount = %s, Add_Ons_Total_Amount = %s, Discount_Type = %s, Leftover_ID = %s, 
                Cash_Amount = %s, Reference_ID = %s, Payment_Method = %s, Payment_Status = 'Completed'
                WHERE Order_ID = %s
            """, (self.total_amount, self.subtotal_amount, self.vat_amount, self.discount_amount, self.change_amount,
                  self.package_total_amount, self.add_ons_total_amount, self.discount_type, self.leftover_id,
                  self.cash_amount, self.reference_id, self.payment_method, order_id))

            conn.commit()
            self.print_receipt()
            self.populate_comboBox()
        except Exception as e:
            print(f"Error updating order details: {e}")  # Debug statement
            QMessageBox.warning(self, "Error", f"Error in updating data: {str(e)}")
        finally:
            cursor.close()

    def print_receipt(self):
        order_id = self.orderidBOX.currentText()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT o.Customer_Name, o.Guest_Pax, p.Package_Name, p.Package_Price, o.Order_Type
                FROM `order` o
                LEFT JOIN `package` p ON o.Package_ID = p.Package_ID
                WHERE o.Order_ID = %s 
            """, (order_id,))
            order_details = cursor.fetchone()

            if not order_details:
                QMessageBox.warning(self, "Data Error", "No data found for the selected order.")
                return

            reference_id = self.reference_id if self.reference_id else ''

            customer_name, guest_pax, package_name, package_price, order_type = order_details

            receipt_text = f"""
                    Moonhey Hotpot and Grill 
            848A Banawe St, Quezon City, 1114 Metro Manila
                Contact Number: 0917 123 4567
                        Sales Invoice






    Date & Time: {self.label_11.text()}

    Order ID: {self.orderidBOX.currentText()}
    Customer Name: {customer_name}
    """

            if order_type == "Package":
                receipt_text += f"""
    Package Details
    {"Package Type":<15} {"Guest Pax":<11} {"Price":<10} {"Total":>10}
    {self.packageDISPLAY.text():<17} {guest_pax:<13} {self.packageAmountDISPLAY.text():<10} {package_price:>10.2f}
    """

            elif order_type == 'Add-ons only':
                receipt_text += f"""
    Add-ons Details
    {"Product Name":<15} {"Quantity":<10} {"Price":<10} {"Total":>10}
    """

                # Append each add-on row to the receipt text
                for product_name, quantity, selling_cost, total_amount in self.add_ons_rows:
                    receipt_text += f"{product_name:<15} {quantity:<10} {selling_cost:.2f} {total_amount:.2f}\n"

            receipt_text += f"""
    {"VAT (12%):":} {self.vat_amount:.2f}
    {"Discount (" + self.discount_type + "):":} {self.discount_amount:.2f}
    {"Leftover Cost:":} {self.penalty_fee:>.2f}
    {"Payment Method:":} {self.payment_method}
    {"Cash Amount:":} {self.cash_amount}
    {"Change Amount:":} {self.change_amount}
    
    {"Total Amount:":} {self.totalamountDISPLAY.text():}
    """

            # Show receipt in dialog
            dialog = CheckoutReceiptDialog(receipt_text)
            dialog.exec_()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error generating receipt: {str(e)}")

