from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow, QRadioButton, QButtonGroup, QApplication, QDialog
from screens.employee_screens.employee_pos.posOrderdetails import Ui_MainWindow
from shared.navigation_signal import auth_back, pos_back
from server.local_server import conn
from screens.receipt.receipt_dialog import ReceiptDialog
from PyQt5.QtCore import QTime
from PyQt5.QtGui import QIntValidator, QRegularExpressionValidator
from PyQt5.QtCore import QRegularExpression
from validator.user_manager import userManager

user_manager = userManager()

class posOrderdetails(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    back_cashier_signal = QtCore.pyqtSignal()
    checkout_signal = QtCore.pyqtSignal()
    modify_signal = QtCore.pyqtSignal()
    menu_signal = QtCore.pyqtSignal()
    transaction_generated_signal = QtCore.pyqtSignal()
    update_combobox_signal = QtCore.pyqtSignal()
    history_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user_manager = userManager()

        self.backBTN.clicked.connect(lambda: pos_back(self.user_manager, self.back_signal, self.back_cashier_signal))
        self.checkoutBTN.clicked.connect(self.goCheckout)
        self.modifyBTN.clicked.connect(self.goModify)
        self.menuBTN.clicked.connect(self.goMenu)
        self.historyBTN.clicked.connect(self.goHistory)
        self.pushButton.clicked.connect(self.cancel_order)
        self.pushButton_2.clicked.connect(self.start_timer)
        self.pushButton_3.clicked.connect(self.print_receipt)
        self.generateBtn.clicked.connect(self.open_generate_dialog)
        self.generateBtn_2.clicked.connect(self.open_addon_dialog)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.timeout.connect(self.populate_table)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        # Connect the selection change signal of the table widget
        self.tableWidget.itemSelectionChanged.connect(self.on_table_selection_changed)

        # Populate the table initially
        self.populate_table()

    def open_addon_dialog(self):
        self.dialog1 = AddonsDialog()
        self.dialog1.exec_()

    def open_generate_dialog(self):
        self.dialog = AddOrderDialog()
        self.dialog.exec_()

    def goHistory(self):
        self.history_signal.emit()

    def goBack(self):
        self.back_signal.emit()

    def goCheckout(self):
        self.checkout_signal.emit()

    def goModify(self):
        self.modify_signal.emit()

    def goMenu(self):
        self.menu_signal.emit()

    def populate_table(self):
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                query = """
                    SELECT 
                        Order_ID,
                        Customer_Name,
                        Order_Type,
                        Guest_Pax,
                        Payment_Status,
                        Priority_Order
                    FROM `order`
                    WHERE (Payment_Status = 'Waiting for Receipt' OR Payment_Status = 'Waiting for Timer'
                    OR (Order_Type = 'Add-ons only' AND Payment_Status = 'Pending'))
                    AND Payment_Status != 'Cancelled'
                    ORDER BY Priority_Order DESC, Order_ID ASC
                """
                cursor.execute(query)
                records = cursor.fetchall()

                # Clear only the rows in the table widget
                self.tableWidget.setRowCount(0)

                self.display_records(records)

                header = self.tableWidget.horizontalHeader()
                header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        except Exception as e:
            print("Error occurred while populating table:", e)

        finally:
            if conn.is_connected():
                cursor.close()

    def display_records(self, records):
        column_names = [
            "Order ID",
            "Customer Name",
            "Order Type",
            "Guest Pax",
            "Payment Status",
            "Priority Order"
        ]

        if records:
            self.tableWidget.setRowCount(len(records))
            self.tableWidget.setColumnCount(len(column_names))

            for j, name in enumerate(column_names):
                item = QTableWidgetItem(name)
                self.tableWidget.setHorizontalHeaderItem(j, item)

            for i, row in enumerate(records):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))  # Always convert to string
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Make cell non-clickable
                    self.tableWidget.setItem(i, j, item)

                    # Apply conditional formatting for the "Priority Order" column
                    if column_names[j] == "Priority Order" and col == "Priority":
                        item.setBackground(QtGui.QColor(255, 215, 0))  # Gold color for priority

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.date.setText(formattedDateTime)

    def print_receipt(self):
        order_id = self.comboBox_7.text()

        try:
            cursor = conn.cursor()

            # Fetch order details based on order_id
            cursor.execute("""
                SELECT Payment_Status, Order_Type
                FROM `order`
                WHERE Order_ID = %s
            """, (order_id,))
            order_status = cursor.fetchone()

            if not order_status:
                QMessageBox.warning(self, "Error", f"No order found for Order ID: {order_id}")
                return

            payment_status = order_status[0]
            order_type = order_status[1]

            if order_type == 'Add-ons only':
                QMessageBox.warning(self, "Error", "Cannot print receipt for 'Add-ons only' orders.")
                return

            if order_type == 'Package' and (payment_status == 'Waiting for Timer' or payment_status == 'Pending'):
                QMessageBox.warning(self, "Error",
                                    "Receipt has already been sent to the kitchen for 'Package' orders with 'Waiting for Timer' or 'Pending' payment status.")
                return

            # Update the payment status to 'Waiting for Timer'
            cursor.execute("""
                UPDATE `order`
                SET Payment_Status = 'Waiting for Timer'
                WHERE Order_ID = %s
            """, (order_id,))
            conn.commit()

            # Fetch detailed order information
            cursor.execute("""
                SELECT Date, Customer_Name, Package_ID, Guest_Pax, Order_Type, 
                       Soup_Variation, Priority_Order
                FROM `order`
                WHERE Order_ID = %s
            """, (order_id,))
            order_details = cursor.fetchone()

            if order_details:
                # Unpack fetched values
                current_date = order_details[0]
                customer_name = order_details[1]
                package_id = order_details[2]
                guest_capacity = order_details[3]
                order_type = order_details[4]
                soup_variation = order_details[5]
                priority_order = order_details[6]

                # Get current time in HH:mm:ss format
                current_time = QTime.currentTime().toString(Qt.DefaultLocaleLongDate)

                # Get package name from package table
                package_name = self.get_package_name(cursor, package_id)

                # Construct the order details string including time
                order_details_text = f"""
                MOON HEY HOTPOT AND GRILL
                RESTAURANT
                OWNED BY: MOON HEY INC.
                848-A BANAWE STREET SIENNA
                QUEZON CITY - 00002 NCR,
                SECOND DISTRICT
                BILL

                OR#: {order_id}
                DATE/TIME: {current_date}  {current_time}
                CASHIER: {self.user_manager.get_first_name()}
                CUSTOMER NAME: {customer_name}

                DESCRIPTION
                PACKAGE: {package_name if package_name else "N/A"}
                PAX: {guest_capacity if guest_capacity else "N/A"}
                Order Type: {order_type}
                Soup Variation: {soup_variation if soup_variation else "N/A"}
                Priority Order: {priority_order}


                -------------------------------------------------------------
                -------------------------------------------------------------
                
                THIS DOCUMENT IS NOT VALID
                FOR CLAIM OF INPUT TAX








                """

                # Create and show the receipt dialog
                receipt_dialog = ReceiptDialog(order_details_text)
                receipt_dialog.exec_()

                self.populate_table()

            else:
                QMessageBox.warning(self, "Error", f"No order found for Order ID: {order_id}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred: {e}")

        finally:
            if cursor and conn.is_connected():
                cursor.close()

    def get_package_name(self, cursor, package_id):
        try:
            cursor.execute("SELECT Package_Name FROM package WHERE Package_ID = %s", (package_id,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return "N/A"
        except Exception as e:
            print(f"Error occurred while fetching package name: {e}")
            return "N/A"

    def cancel_order(self):
        order_id = self.comboBox_7.text()
        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        try:
            cursor = conn.cursor()

            # Check if the order type is 'Package' and payment status is 'Pending' or 'Waiting for Timer'
            cursor.execute("""
                SELECT Order_Type, Payment_Status
                FROM `order`
                WHERE Order_ID = %s
            """, (order_id,))
            order_info = cursor.fetchone()

            if order_info:
                order_type = order_info[0]
                payment_status = order_info[1]

                if order_type == 'Package':
                    if payment_status == 'Pending':
                        QMessageBox.warning(self, "Cancellation Error",
                                            "Package orders with 'Pending' status cannot be cancelled directly. They have already been prepared.")
                        return
                    elif payment_status == 'Waiting for Timer':
                        QMessageBox.warning(self, "Cancellation Error",
                                            "Package orders with 'Waiting for Timer' status cannot be cancelled directly. They have already been sent to the kitchen.")
                        return

                # Check if the order type is 'Add-ons only' and there are existing product details in add_on table
                elif order_type == 'Add-ons only':
                    cursor.execute("""
                        SELECT COUNT(*) 
                        FROM add_on 
                        WHERE Order_ID = %s
                    """, (order_id,))
                    add_on_count = cursor.fetchone()[0]

                    if add_on_count > 0:
                        QMessageBox.warning(self, "Cancellation Error",
                                            "'Add-ons only' orders with existing add-on products cannot be cancelled directly.")
                        return

            # Confirm cancellation with the user
            reply = QMessageBox.question(self, 'Confirm Cancel',
                                         f"Are you sure you want to cancel order ID {order_id}?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                # Perform the cancellation
                cursor.execute("UPDATE `order` SET Payment_Status = 'Cancelled' WHERE Order_ID = %s", (order_id,))
                conn.commit()

                QMessageBox.information(self, "Order Cancelled", "The order has been successfully cancelled.")

                self.comboBox_7.clear()
                self.populate_table()

            else:
                QMessageBox.information(self, "Cancelled", "Cancellation operation cancelled by user.")

        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Error occurred while cancelling the order: {e}")

        finally:
            if conn.is_connected():
                cursor.close()

    def start_timer(self):
        order_id = self.comboBox_7.text()
        if not order_id:
            QMessageBox.warning(self, "Input Error", "Please select an order ID.")
            return

        try:
            cursor = conn.cursor()

            # Fetch order details based on order_id
            cursor.execute("SELECT Order_Type, Payment_Status FROM `order` WHERE Order_ID = %s", (order_id,))
            order_details = cursor.fetchone()

            if order_details:
                order_type = order_details[0]
                payment_status = order_details[1]

                if order_type == 'Add-ons only':
                    QMessageBox.warning(self, "Timer Error", "Timer operation is for package order type only.")
                elif order_type == 'Package':
                    if payment_status == 'Pending' or payment_status == 'Waiting for Receipt':
                        QMessageBox.warning(self, "Send to Kitchen", "Please send this order to the kitchen first.")
                    else:
                        cursor.execute("UPDATE `order` SET Payment_Status = 'Pending' WHERE Order_ID = %s", (order_id,))
                        conn.commit()

                        QMessageBox.information(self, "Timer Started", "The order timer has been started successfully.")
                        self.transaction_generated_signal.emit()
                        self.comboBox_7.clear()

                else:
                    QMessageBox.warning(self, "Timer Error", "Unsupported order type for timer operation.")

            else:
                QMessageBox.warning(self, "Order Error", f"No order found for Order ID: {order_id}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def on_table_selection_changed(self):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            order_id = self.tableWidget.item(selected_row, 0).text()  # Assuming 'Order ID' is in the first column
            self.comboBox_7.setText(order_id)

class AddOrderDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setWindowTitle('Add Package Order')

        self.pushButton_6.clicked.connect(self.saveOrder)
        self.pushButton_7.clicked.connect(self.discard)

        # Populate comboBox_2 with package names
        self.populate_comboBox_2()

        # Populate comboBox_2 with soup names
        self.populate_comboBox_3()

        self.comboBox_2.setCurrentIndex(-1)
        self.comboBox_3.setCurrentIndex(-1)

        self.buttonGroup1 = QButtonGroup(self)
        self.buttonGroup1.addButton(self.radioButton_3, 2)
        self.buttonGroup1.addButton(self.radioButton_4, 3)

        self.radioButton_4.setChecked(True)

        self.int_validator = QIntValidator(1, 6)
        self.lineEdit_7.setValidator(self.int_validator)

        # Initialize QRegExpValidator for letter-only input
        regex = QRegularExpression("[a-zA-Z]+")  # Regular expression for letters only
        self.letter_validator = QRegularExpressionValidator(regex)
        self.lineEdit_9.setValidator(self.letter_validator)

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(620, 516)
        self.widget_4 = QtWidgets.QWidget(self)
        self.widget_4.setGeometry(QtCore.QRect(30, 0, 594, 501))
        self.widget_4.setObjectName("widget_4")
        self.label_15 = QtWidgets.QLabel(self.widget_4)
        self.label_15.setGeometry(QtCore.QRect(0, 439, 16, 16))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setGeometry(QtCore.QRect(140, 439, 447, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_6.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
                                        "    background-color: #67B99A;\n"
                                        "    color: white;\n"
                                        "    border: 2px solid #67B99A;\n"
                                        "    padding: 8px 16px;\n"
                                        "    border-radius: 15px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #5CAE8B;\n"
                                        "    border: 2px solid #5CAE8B;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #4D9C7F;\n"
                                        "    border: 2px solid #4D9C7F;\n"
                                        "}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_7.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
                                        "    background-color: white;\n"
                                        "    border: 2px solid #67B99A;\n"
                                        "    color: black;\n"
                                        "    padding: 8px 16px;\n"
                                        "    border-radius: 15px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border: 2px solid #4D926D;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #F0F0F0;\n"
                                        "    border: 2px solid #265C42;\n"
                                        "}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.layoutWidget = QtWidgets.QWidget(self.widget_4)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 536, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.label_14 = QtWidgets.QLabel(self.widget_4)
        self.label_14.setGeometry(QtCore.QRect(10, 110, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setGeometry(QtCore.QRect(10, 160, 76, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(140, 150, 400, 35))
        self.lineEdit_9.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_9.setStyleSheet("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_20 = QtWidgets.QLabel(self.widget_4)
        self.label_20.setGeometry(QtCore.QRect(10, 260, 67, 16))
        self.label_20.setObjectName("label_20")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 250, 400, 35))
        self.comboBox_2.setMinimumSize(QtCore.QSize(400, 35))
        self.comboBox_2.setMaximumSize(QtCore.QSize(400, 35))
        self.comboBox_2.setStyleSheet("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(140, 200, 400, 35))
        self.lineEdit_7.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_7.setStyleSheet("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_19 = QtWidgets.QLabel(self.widget_4)
        self.label_19.setGeometry(QtCore.QRect(10, 210, 49, 16))
        self.label_19.setObjectName("label_19")
        self.label_18 = QtWidgets.QLabel(self.widget_4)
        self.label_18.setGeometry(QtCore.QRect(10, 360, 34, 16))
        self.label_18.setObjectName("label_18")
        self.label_17 = QtWidgets.QLabel(self.widget_4)
        self.label_17.setGeometry(QtCore.QRect(10, 310, 69, 16))
        self.label_17.setObjectName("label_17")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_3.setGeometry(QtCore.QRect(140, 300, 400, 35))
        self.comboBox_3.setMinimumSize(QtCore.QSize(400, 35))
        self.comboBox_3.setMaximumSize(QtCore.QSize(400, 35))
        self.comboBox_3.setStyleSheet("")
        self.comboBox_3.setObjectName("comboBox_3")
        self.layoutWidget_3 = QtWidgets.QWidget(self.widget_4)
        self.layoutWidget_3.setGeometry(QtCore.QRect(140, 360, 181, 19))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_6.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_6.addWidget(self.radioButton_4)
        self.label = QtWidgets.QLabel(self.widget_4)
        self.label.setGeometry(QtCore.QRect(140, 100, 400, 35))
        self.label.setMinimumSize(QtCore.QSize(400, 35))
        self.label.setMaximumSize(QtCore.QSize(400, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_6.setText(_translate("Dialog", "Generate Order"))
        self.pushButton_7.setText(_translate("Dialog", "Discard"))
        self.label_5.setText(_translate("Dialog", "Order Details"))
        self.label_14.setText(_translate("Dialog", "Order Type"))
        self.label_10.setText(_translate("Dialog", "Customer Name"))
        self.label_20.setText(_translate("Dialog", "Package Type"))
        self.label_19.setText(_translate("Dialog", "Guest Pax"))
        self.label_18.setText(_translate("Dialog", "Priority"))
        self.label_17.setText(_translate("Dialog", "Soup Variation"))
        self.radioButton_3.setText(_translate("Dialog", "Priority"))
        self.radioButton_4.setText(_translate("Dialog", "Non-Priority"))
        self.label.setText(_translate("Dialog", "Package"))

    def discard(self):
        self.lineEdit_9.clear()
        self.lineEdit_7.clear()
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)

    def populate_comboBox_2(self):
        try:
            # Clear existing items
            self.comboBox_2.clear()

            # Add specific values
            self.comboBox_2.addItems(["Hotpot", "Grill", "Hotpot and Grill"])

        except Exception as e:
            print(f"Error occurred while populating comboBox_2: {e}")

    def populate_comboBox_3(self):
        try:
            # Clear existing items
            self.comboBox_3.clear()

            # Add blank/null option
            self.comboBox_3.addItem("None")  # Add a blank item

            # Add specific values
            self.comboBox_3.addItems(["Mala soup", "Plain soup", "Suan la soup", "Tomato soup"])

        except Exception as e:
            print(f"Error occurred while populating comboBox_3: {e}")

    def saveOrder(self):
        # Get input values
        customer_name = self.lineEdit_9.text().strip()
        order_type = self.label.text()
        priority_order = self.buttonGroup1.checkedButton().text()
        package_name = self.comboBox_2.currentText()
        guest_capacity = self.lineEdit_7.text().strip()
        soup_variation = self.comboBox_3.currentText()

        if soup_variation == 'None':
            soup_variation = None

        payment_status = "Waiting for Receipt"

        if not self.validate_package_inputs(customer_name, package_name, guest_capacity, soup_variation):
            return

        try:
            if conn.is_connected():
                cursor = conn.cursor()

                # Get current date in yyyy-MM-dd format
                current_date = QDateTime.currentDateTime().toString("yyyy-MM-dd")

                # Fetch the latest Order_ID for the current date
                cursor.execute(f"SELECT MAX(Order_ID) FROM `order` WHERE Date = '{current_date}'")
                latest_order_id = cursor.fetchone()[0]

                if latest_order_id:
                    # Extract numeric part and increment
                    numeric_part = latest_order_id[11:]  # Assuming Order_ID format is POSyyyyMMddNNN
                    order_number = int(numeric_part)
                    new_order_number = order_number + 1
                    next_order_number = f"{new_order_number:03d}"
                else:
                    # If no previous orders for the day, start from 001
                    next_order_number = "001"

                # Construct new Order_ID
                new_order_id = f"POS{current_date.replace('-', '')}{next_order_number}"

                # Construct the insert query with proper handling of NULL for Guest_Pax
                insert_query = f"""
                                 INSERT INTO `order` (Order_ID, Date, Time, Package_ID, Payment_Status, 
                                                      Guest_Pax, Customer_Name, Soup_Variation, Order_Type, Priority_Order)
                                 VALUES (%s, %s, TIME_FORMAT(NOW(), '%H:%i'), 
                                         (SELECT Package_ID FROM package WHERE Package_Name = %s), 
                                         %s, %s, %s, %s, %s, %s)
                             """
                cursor.execute(insert_query, (
                    new_order_id, current_date, package_name, payment_status, guest_capacity, customer_name,
                    soup_variation, order_type, priority_order))
                conn.commit()

                QMessageBox.information(self, "Success", "Order saved successfully.")

                # Clear input fields after successful save
                self.lineEdit_9.clear()
                self.lineEdit_7.clear()
                self.comboBox_2.setCurrentIndex(-1)
                self.comboBox_3.setCurrentIndex(-1)

                self.reset_styles()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred while saving order: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def reset_styles(self):
        self.lineEdit_9.setStyleSheet("")
        self.comboBox_2.setStyleSheet("")
        self.lineEdit_7.setStyleSheet("")
        self.comboBox_3.setStyleSheet("")

    def validate_package_inputs(self, customer_name, package_name, guest_capacity, soup_variation):
        valid = True

        if not customer_name:
            self.lineEdit_9.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_9.setStyleSheet("border: 1px solid green;")

        if not package_name:
            self.comboBox_2.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_2.setStyleSheet("border: 1px solid green;")

        if not guest_capacity:
            self.lineEdit_7.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_7.setStyleSheet("border: 1px solid green;")

        if package_name == "Grill":
            if soup_variation is not None:
                self.comboBox_3.setStyleSheet("border: 1px solid red;")
                valid = False
            else:
                self.comboBox_3.setStyleSheet("border: 1px solid green;")
        else:
            if not soup_variation or soup_variation == "None":
                self.comboBox_3.setStyleSheet("border: 1px solid red;")
                valid = False
            else:
                self.comboBox_3.setStyleSheet("border: 1px solid green;")

        if not valid:
            QMessageBox.warning(self, "Warning", "Please fill in all fields correctly.")

        return valid

class AddonsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setWindowTitle("Add 'Add-ons' Order")

        self.pushButton_6.clicked.connect(self.saveOrder)
        self.pushButton_7.clicked.connect(self.discard)

        self.buttonGroup1 = QButtonGroup(self)
        self.buttonGroup1.addButton(self.radioButton_3, 2)
        self.buttonGroup1.addButton(self.radioButton_4, 3)

        self.radioButton_4.setChecked(True)

        # Initialize QRegExpValidator for letter-only input
        regex = QRegularExpression("[a-zA-Z]+")  # Regular expression for letters only
        self.letter_validator = QRegularExpressionValidator(regex)
        self.lineEdit_9.setValidator(self.letter_validator)

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(617, 344)
        self.widget_4 = QtWidgets.QWidget(self)
        self.widget_4.setGeometry(QtCore.QRect(30, 0, 594, 501))
        self.widget_4.setObjectName("widget_4")
        self.label_15 = QtWidgets.QLabel(self.widget_4)
        self.label_15.setGeometry(QtCore.QRect(0, 439, 16, 16))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setGeometry(QtCore.QRect(140, 260, 447, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 0, 200, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_6.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
                                        "    background-color: #67B99A;\n"
                                        "    color: white;\n"
                                        "    border: 2px solid #67B99A;\n"
                                        "    padding: 8px 16px;\n"
                                        "    border-radius: 15px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #5CAE8B;\n"
                                        "    border: 2px solid #5CAE8B;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #4D9C7F;\n"
                                        "    border: 2px solid #4D9C7F;\n"
                                        "}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_7.setGeometry(QtCore.QRect(207, 0, 200, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_7.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
                                        "    background-color: white;\n"
                                        "    border: 2px solid #67B99A;\n"
                                        "    color: black;\n"
                                        "    padding: 8px 16px;\n"
                                        "    border-radius: 15px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border: 2px solid #4D926D;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #F0F0F0;\n"
                                        "    border: 2px solid #265C42;\n"
                                        "}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.layoutWidget = QtWidgets.QWidget(self.widget_4)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 536, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.label_14 = QtWidgets.QLabel(self.widget_4)
        self.label_14.setGeometry(QtCore.QRect(10, 110, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setGeometry(QtCore.QRect(10, 160, 76, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(140, 150, 400, 35))
        self.lineEdit_9.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_9.setStyleSheet("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_18 = QtWidgets.QLabel(self.widget_4)
        self.label_18.setGeometry(QtCore.QRect(10, 210, 34, 16))
        self.label_18.setObjectName("label_18")
        self.layoutWidget_3 = QtWidgets.QWidget(self.widget_4)
        self.layoutWidget_3.setGeometry(QtCore.QRect(140, 210, 181, 19))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_6.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_6.addWidget(self.radioButton_4)
        self.label = QtWidgets.QLabel(self.widget_4)
        self.label.setGeometry(QtCore.QRect(140, 100, 400, 35))
        self.label.setMinimumSize(QtCore.QSize(400, 35))
        self.label.setMaximumSize(QtCore.QSize(400, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_6.setText(_translate("Dialog", "Generate Order"))
        self.pushButton_7.setText(_translate("Dialog", "Discard"))
        self.label_5.setText(_translate("Dialog", "Order Details"))
        self.label_14.setText(_translate("Dialog", "Order Type"))
        self.label_10.setText(_translate("Dialog", "Customer Name"))
        self.label_18.setText(_translate("Dialog", "Priority"))
        self.radioButton_3.setText(_translate("Dialog", "Priority"))
        self.radioButton_4.setText(_translate("Dialog", "Non-Priority"))
        self.label.setText(_translate("Dialog", "Add-ons only"))

    def saveOrder(self):
        # Get input values
        customer_name = self.lineEdit_9.text().strip()
        order_type = self.label.text()
        priority_order = self.buttonGroup1.checkedButton().text()

        payment_status = "Pending"

        if not self.validate_package_inputs(customer_name):
            return

        try:
            if conn.is_connected():
                cursor = conn.cursor()

                # Get current date in yyyy-MM-dd format
                current_date = QDateTime.currentDateTime().toString("yyyy-MM-dd")

                # Fetch the latest Order_ID for the current date
                cursor.execute(f"SELECT MAX(Order_ID) FROM `order` WHERE Date = '{current_date}'")
                latest_order_id = cursor.fetchone()[0]

                if latest_order_id:
                    # Extract numeric part and increment
                    numeric_part = latest_order_id[11:]  # Assuming Order_ID format is POSyyyyMMddNNN
                    order_number = int(numeric_part)
                    new_order_number = order_number + 1
                    next_order_number = f"{new_order_number:03d}"
                else:
                    # If no previous orders for the day, start from 001
                    next_order_number = "001"

                # Construct new Order_ID
                new_order_id = f"POS{current_date.replace('-', '')}{next_order_number}"

                # Construct the insert query with proper handling of NULL for Guest_Pax
                insert_query = """
                               INSERT INTO `order` (Order_ID, Date, Time, Payment_Status, Customer_Name, 
                                                    Order_Type, Priority_Order)
                               VALUES (%s, %s, TIME_FORMAT(NOW(), '%H:%i'), %s, %s, %s, %s)
                               """
                cursor.execute(insert_query, (
                    new_order_id, current_date, payment_status, customer_name, order_type, priority_order))
                conn.commit()

                QMessageBox.information(self, "Success", "Order saved successfully.")

                # Clear input fields after successful save
                self.lineEdit_9.clear()

                self.reset_styles()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred while saving order: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def discard(self):
        self.lineEdit_9.clear()

    def reset_styles(self):
        self.lineEdit_9.setStyleSheet("")

    def validate_package_inputs(self, customer_name):
        valid = True

        if not customer_name:
            self.lineEdit_9.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_9.setStyleSheet("border: 1px solid green;")

        if not valid:
            QMessageBox.warning(self, "Warning", "Please fill in your name correctly.")

        return valid



