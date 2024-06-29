from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow, QHeaderView
from PyQt5.QtCore import QDateTime, QTimer, QRegExp, Qt
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

        # Make table grid invisible
        self.orderList.setShowGrid(False)

        self.orderList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.orderList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Hide row numbers
        self.orderList.verticalHeader().setVisible(False)
        self.orderList.horizontalHeader().setVisible(False)

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

                if order_type == "Package":
                    # Add package details header row
                    self.orderList.insertRow(row)
                    self.orderList.setItem(row, 0, QTableWidgetItem(f"Package Details"))
                    self.orderList.setSpan(row, 0, 1, 4)
                    row += 1

                    # Add headers as next row in the table
                    self.orderList.insertRow(row)
                    self.orderList.setItem(row, 0, QTableWidgetItem("Package Name"))
                    self.orderList.setItem(row, 2, QTableWidgetItem("Price"))
                    self.orderList.setItem(row, 3, QTableWidgetItem("Quantity"))
                    row += 1

                    # Add package details
                    self.orderList.insertRow(row)
                    self.orderList.setItem(row, 0, QTableWidgetItem(package_name))
                    self.orderList.setItem(row, 2,
                                           QTableWidgetItem(f"{package_price:.2f}" if package_price else "0.00"))
                    self.orderList.setItem(row, 3, QTableWidgetItem(str(guest_pax)))
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
                            self.orderList.setItem(row, 3, QTableWidgetItem(str(quantity)))
                            row += 1

                    else:
                        QMessageBox.warning(self, "Data Error", "No add-ons found for this order.")

                elif order_type == "Add-ons only":
                    QMessageBox.warning(self, "Data Error", "No add-ons found for this order.")

            except Exception as e:
                print(f"Error fetching order details: {e}")  # Debug statement
                QMessageBox.warning(self, "Error", f"Error in fetching data: {str(e)}")
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

    def adjust_column_widths(self):
        header = self.orderList.horizontalHeader()
        # Set resize mode for all columns except column 4 (index 3)
        for col in range(self.orderList.columnCount()):
            if col != 1 and col != 2 and col != 3:
                header.setSectionResizeMode(col, QHeaderView.ResizeToContents)
            else:
                header.setSectionResizeMode(col, QHeaderView.Fixed)