from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QMainWindow

from screens.employee_screens.employee_pos.posMenu_functions import posMenu
from screens.employee_screens.employee_pos.posOrderdetails import Ui_MainWindow
from shared.navigation_signal import auth_back, pos_back
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from validator.user_manager import userManager


class posOrderdetails(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    back_cashier_signal = QtCore.pyqtSignal()
    checkout_signal = QtCore.pyqtSignal()
    modify_signal = QtCore.pyqtSignal()
    menu_signal = QtCore.pyqtSignal()
    transaction_generated_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user_manager = userManager()

        self.backBTN.clicked.connect(lambda: pos_back(self.user_manager, self.back_signal, self.back_cashier_signal))
        self.checkoutBTN.clicked.connect(self.goCheckout)
        self.modifyBTN.clicked.connect(self.goModify)
        self.menuBTN.clicked.connect(self.goMenu)
        self.pushButton_6.clicked.connect(self.saveOrder)  # Connect saveOrder function to pushButton_6

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
                guest_pax = self.lineEdit_7.text().strip()
                soup_variation = self.comboBox_3.currentText()

                # Insert the new order into the database
                insert_query = f"""
                    INSERT INTO `order` (Order_ID, Date, Time, Package_ID, Payment_Status, 
                                         Guest_Pax, Customer_Name, Soup_Variation)
                    VALUES ('{new_order_id}', '{current_date}', 
                            TIME_FORMAT(NOW(), '%H:%i'), 
                            (SELECT Package_ID FROM package WHERE Package_Name = '{package_name}'), 
                            'Pending', 
                            '{guest_pax}', 
                            '{customer_name}', 
                            '{soup_variation}')
                """
                cursor.execute(insert_query)
                conn.commit()

                QMessageBox.information(self, "Success", "Order saved successfully.")
                self.transaction_generated_signal.emit()

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

    def populate_comboBox_2(self):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT Package_Name FROM package")
            packages = cursor.fetchall()

            self.comboBox_2.clear()
            for package in packages:
                self.comboBox_2.addItem(package[0])

        except Exception as e:
            print(f"Error occurred while populating comboBox_2: {e}")

        finally:
            if conn.is_connected():
                cursor.close()

    def populate_comboBox_3(self):
        try:
            # Clear existing items
            self.comboBox_3.clear()

            # Add blank/null option
            self.comboBox_3.addItem("")  # Add a blank item

            # Add specific values
            self.comboBox_3.addItems(["Mala soup", "Plain soup", "Suan la soup", "Tomato soup"])

        except Exception as e:
            print(f"Error occurred while populating comboBox_7: {e}")
