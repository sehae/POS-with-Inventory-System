from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QMainWindow

from screens.employee_screens.employee_pos.posMenu_functions import posMenu
from screens.employee_screens.employee_pos.posOrderdetails import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn


class posOrderdetails(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    checkout_signal = QtCore.pyqtSignal()
    modify_signal = QtCore.pyqtSignal()
    menu_signal = QtCore.pyqtSignal()
    transaction_generated_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.backBTN.clicked.connect(self.goBack)
        self.checkoutBTN.clicked.connect(self.goCheckout)
        self.modifyBTN.clicked.connect(self.goModify)
        self.menuBTN.clicked.connect(self.goMenu)
        self.pushButton_6.clicked.connect(self.saveOrder)  # Connect saveOrder function to pushButton_6
        self.pushButton.clicked.connect(self.cancel_order)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        # Populate comboBox_2 with package names
        self.populate_comboBox_2()

        # Populate comboBox_3 with soup variations
        self.populate_comboBox_3()

        # Populate comboBox_7 with order ids
        self.populate_comboBox_7()

        # Populate comboBox_4 with order types
        self.populate_comboBox_4()

    def populate_comboBox_4(self):
        try:
            # Clear existing items
            self.comboBox_4.clear()

            # Add specific values
            self.comboBox_4.addItems(["Package", "Add-ons only"])

        except Exception as e:
            print(f"Error occurred while populating comboBox_4: {e}")

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

    def goMenu(self):
        self.menu_signal.emit()

    def populate_comboBox_2(self):
        try:
            # Clear existing items
            self.comboBox_2.clear()

            # Add blank/null option
            self.comboBox_2.addItem("")  # Add a blank item

            # Add specific values
            self.comboBox_2.addItems(["Hotpot", "Grill", "Hotpot and Grill"])

        except Exception as e:
            print(f"Error occurred while populating comboBox_2: {e}")

    def populate_comboBox_3(self):
        try:
            # Clear existing items
            self.comboBox_3.clear()

            # Add blank/null option
            self.comboBox_3.addItem("")  # Add a blank item

            # Add specific values
            self.comboBox_3.addItems(["Mala soup", "Plain soup", "Suan la soup", "Tomato soup"])

        except Exception as e:
            print(f"Error occurred while populating comboBox_3: {e}")

    def populate_comboBox_7(self):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT Order_ID FROM `order` WHERE Payment_Status = 'Pending'")
            order_ids = cursor.fetchall()

            self.comboBox_7.clear()
            for order_id in order_ids:
                self.comboBox_7.addItem(str(order_id[0]))

        except Exception as e:
            print(f"Error occurred while populating comboBox_7: {e}")

        finally:
            if conn.is_connected():
                cursor.close()

    def cancel_order(self):
        order_id = self.comboBox_7.currentText()
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
                self.populate_comboBox_7()  # Refresh the combo box

            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Error occurred while cancelling the order: {e}")

            finally:
                if conn.is_connected():
                    cursor.close()
        else:
            QMessageBox.information(self, "Cancelled", "Cancellation operation cancelled by user.")


    def saveOrder(self):
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

                # Get input values


                customer_name = self.lineEdit_9.text().strip()
                package_name = self.comboBox_2.currentText()
                guest_capacity = self.lineEdit_7.text().strip()
                order_type = self.comboBox_4.currentText()
                soup_variation = self.comboBox_3.currentText()

                if order_type == "Add-ons only":
                    package_name = None
                    guest_capacity = None
                    soup_variation = None
                else:
                    package_name = str(package_name)
                    guest_capacity = guest_capacity.strip()
                    guest_capacity = int(guest_capacity) if guest_capacity else None
                    soup_variation = str(soup_variation)

                # Construct the insert query with proper handling of NULL for Guest_Pax
                insert_query = f"""
                                INSERT INTO `order` (Order_ID, Date, Time, Package_ID, Payment_Status, 
                                                     Guest_Pax, Customer_Name, Soup_Variation, Order_Type)
                                VALUES (%s, %s, TIME_FORMAT(NOW(), '%H:%i'), 
                                        (SELECT Package_ID FROM package WHERE Package_Name = %s), 
                                        %s, %s, %s, %s, %s)
                            """
                cursor.execute(insert_query, (new_order_id, current_date, package_name, 'Pending', guest_capacity, customer_name, soup_variation, order_type))
                conn.commit()

                QMessageBox.information(self, "Success", "Order saved successfully.")
                self.transaction_generated_signal.emit()

                self.populate_comboBox_7()

                # Clear input fields after successful save
                self.lineEdit_9.clear()
                self.lineEdit_7.clear()
                self.comboBox_2.setCurrentIndex(-1)
                self.comboBox_3.setCurrentIndex(-1)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred while saving order: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()
