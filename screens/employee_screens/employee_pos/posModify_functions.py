from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QDateTime, QTimer, Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from screens.employee_screens.employee_pos.posModify import Ui_MainWindow
from shared.navigation_signal import auth_back, pos_back
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from screens.employee_screens.employee_pos.posOrderdetails_functions import posOrderdetails
from validator.user_manager import userManager
from PyQt5.QtGui import QIntValidator

class posModify(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    back_cashier_signal = QtCore.pyqtSignal()
    checkout_signal = QtCore.pyqtSignal()
    menu_signal = QtCore.pyqtSignal()
    order_signal = QtCore.pyqtSignal()
    history_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user_manager = userManager()

        self.backBTN.clicked.connect(lambda: pos_back(self.user_manager, self.back_signal, self.back_cashier_signal))
        self.checkoutBTN.clicked.connect(self.goCheckout)
        self.menuBTN.clicked.connect(self.goMenu)
        self.orderBTN.clicked.connect(self.goOrder)
        self.pushButton_8.clicked.connect(self.modifyOrder)
        self.historyBTN_3.clicked.connect(self.history_signal.emit)

        self.pos_orderdetails = posOrderdetails()

        self.pos_orderdetails.transaction_generated_signal.connect(self.populate_table)

        # Create QTimer objects
        self.timer = QTimer()

        # Connect the timeout signal of the timers to the respective slots
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.timeout.connect(self.populate_table)

        # Set the interval for the timers (in milliseconds)
        self.timer.start(1000)  # Update date and time every second

        self.searchFIELD.returnPressed.connect(self.search_table)

        self.populate_table()
        self.populate_comboBox_6()
        self.populate_comboBox_7()

        self.comboBox_6.setCurrentIndex(-1)

        self.int_validator = QIntValidator()
        self.lineEdit_8.setValidator(self.int_validator)

        self.lineEdit.setReadOnly(True)

        self.tableWidget_2.itemSelectionChanged.connect(self.on_table_item_selected)


    def on_table_item_selected(self):
        selected_items = self.tableWidget_2.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            order_id = self.tableWidget_2.item(selected_row, 0).text()  # Assuming 'Order ID' is in the first column
            package_name = self.tableWidget_2.item(selected_row, 4).text()
            guest_pax = self.tableWidget_2.item(selected_row, 6).text()
            soup_variation = self.tableWidget_2.item(selected_row, 5).text()

            if soup_variation == '-':
                soup_variation = "None"

            # Set order ID
            self.lineEdit.setText(order_id)

            # Set comboBox_6 to package_name
            package_index = self.comboBox_6.findText(package_name)
            if package_index >= 0:
                self.comboBox_6.setCurrentIndex(package_index)

            # Set comboBox_7 to soup_variation
            soup_index = self.comboBox_7.findText(soup_variation)
            if soup_index >= 0:
                self.comboBox_7.setCurrentIndex(soup_index)

            # Set guest_pax
            self.lineEdit_8.setText(guest_pax)

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

    def goMenu(self):
        self.menu_signal.emit()

    def goOrder(self):
        self.order_signal.emit()

    def populate_table(self):
        try:
            if conn.is_connected():
                cursor = conn.cursor()

                # Execute the query to retrieve data for specific columns including Priority_Order
                query = """
                    SELECT o.Order_ID, o.Date, o.Time, o.Customer_Name, p.Package_Name, 
                           CASE WHEN o.Soup_Variation = 'None' THEN '-' ELSE o.Soup_Variation END AS Soup_Variation, 
                           CASE WHEN o.Guest_Pax = 'None' THEN '-' ELSE o.Guest_Pax END AS Guest_Pax, 
                           o.Priority_Order,
                           CASE
                               WHEN TIMESTAMPDIFF(MINUTE, CONCAT(o.Date, ' ', o.Time), NOW()) < 30 THEN 'Last 30 Minutes'
                               WHEN TIMESTAMPDIFF(MINUTE, CONCAT(o.Date, ' ', o.Time), NOW()) < 60 THEN 'Last 1 Hour'
                               WHEN TIMESTAMPDIFF(MINUTE, CONCAT(o.Date, ' ', o.Time), NOW()) < 120 THEN '2 Hours Left'
                               ELSE 'More Than 2 Hours'
                           END AS Time_Status
                    FROM `order` o
                    JOIN `package` p ON o.Package_ID = p.Package_ID
                    WHERE o.Payment_Status = 'Pending'
                    ORDER BY o.Priority_Order DESC, o.Order_ID ASC
                """
                cursor.execute(query)

                # Fetch column names
                column_names = [i[0].replace('_', ' ') for i in cursor.description]  # Replace '_' with ' '

                # Fetch all the records
                self.records = cursor.fetchall()

                self.tableWidget_2.clearContents()

                if self.records:  # Check if records is not empty
                    # Set the number of rows and columns in the table widget
                    self.tableWidget_2.setRowCount(len(self.records))
                    self.tableWidget_2.setColumnCount(len(column_names))

                    # Populate the column names
                    for j, name in enumerate(column_names):
                        item = QTableWidgetItem(name)
                        self.tableWidget_2.setHorizontalHeaderItem(j, item)

                    # Populate the table widget with data
                    for i, row in enumerate(self.records):
                        for j, col in enumerate(row):
                            item = QTableWidgetItem(str(col))
                            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Make cell non-clickable

                            # Apply conditional formatting for the "Time Status" column
                            if column_names[j] == "Time Status":
                                if col == "2 Hours Left":
                                    item.setBackground(QtGui.QColor(144, 238, 144))  # Light green
                                elif col == "More Than 2 Hours":
                                    item.setBackground(QtGui.QColor(255, 99, 71))  # Light red
                                elif col == "Last 30 Minutes":
                                    item.setBackground(QtGui.QColor(255, 215, 0))  # Yellow for last 30 minutes
                                elif col == "Last 1 Hour":
                                    item.setBackground(QtGui.QColor(154, 205, 50))  # Yellow green for last 1 hour

                            # Apply conditional formatting for the "Priority Order" column
                            if column_names[j] == "Priority Order" and col == "Priority":
                                item.setBackground(QtGui.QColor(255, 215, 0))  # Gold color for priority

                            # Replace 'None' strings with '-'
                            if col == 'None' or col == '':
                                item.setText('-')

                            self.tableWidget_2.setItem(i, j, item)

                    header = self.tableWidget_2.horizontalHeader()
                    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                    header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                    header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                    header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
                    header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)

        except Exception as e:
            print("Error occurred while populating table:", e)

        finally:
            if conn.is_connected():
                cursor.close()

    def populate_comboBox_6(self):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT Package_Name FROM `package`")
            package_names = cursor.fetchall()

            self.comboBox_6.clear()
            for package_name in package_names:
                self.comboBox_6.addItem(package_name[0])

        except Exception as e:
            print(f"Error occurred while populating comboBox_6: {e}")

        finally:
            if conn.is_connected():
                cursor.close()

    def populate_comboBox_7(self):
        try:
            # Clear existing items
            self.comboBox_7.clear()

            # Add blank/null option
            self.comboBox_7.addItem("None")  # Add a blank item

            # Add specific values
            self.comboBox_7.addItems(["Mala soup", "Plain soup", "Suan la soup", "Tomato soup"])

        except Exception as e:
            print(f"Error occurred while populating comboBox_7: {e}")

    def modifyOrder(self):
        # Get input values
        order_id = self.lineEdit.text()
        package_name = self.comboBox_6.currentText()
        guest_pax = self.lineEdit_8.text().strip()
        soup_variation = self.comboBox_7.currentText()

        valid = True

        # Validate package_name
        if not package_name:
            self.comboBox_6.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_6.setStyleSheet("border: 1px solid green;")

        # Validate guest_pax
        if not guest_pax:
            self.lineEdit_8.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_8.setStyleSheet("border: 1px solid green;")

        if package_name != 'Grill' and not soup_variation:
            self.comboBox_7.setStyleSheet("border: 1px solid red;")
            valid = False
        elif package_name == 'Grill' and soup_variation != "None":
            QMessageBox.critical(self, "Error", "Grill package cannot have soup variation. Set it to None.")
            self.comboBox_7.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_7.setStyleSheet("border: 1px solid green;")

        # If validation fails, show an error message and return
        if not valid:
            QMessageBox.critical(self, "Error", "Please fill in all required fields.")
            return
        try:
            if conn.is_connected():
                cursor = conn.cursor()

                if soup_variation == "None":
                    soup_variation = None

                # Fetch Package_ID based on selected Package_Name
                cursor.execute(f"SELECT Package_ID FROM `package` WHERE Package_Name = '{package_name}'")
                package_id = cursor.fetchone()[0]

                # Update the order in the database
                update_query = f"""
                    UPDATE `order`
                    SET Package_ID = {package_id}, Guest_Pax = '{guest_pax}', 
                        Soup_Variation = '{soup_variation}'
                    WHERE Order_ID = '{order_id}'
                """
                cursor.execute(update_query)
                conn.commit()

                QMessageBox.information(self, "Success", "Order modified successfully.")
                self.clear()  # Clear input fields and styles after successful modification
                self.populate_table()  # Refresh the table after modification

        except Exception as e:
            print(f"Error occurred while modifying: {e}")
        finally:
            if conn.is_connected():
                cursor.close()

    def clear(self):
        self.lineEdit.clear()
        self.comboBox_6.setCurrentIndex(-1)
        self.comboBox_7.setCurrentIndex(-1)
        self.lineEdit_8.clear()
        self.comboBox_6.setStyleSheet("")
        self.comboBox_7.setStyleSheet("")
        self.lineEdit_8.setStyleSheet("")

    def search_table(self):
        search_text = self.searchFIELD.text().lower()

        for i in range(self.tableWidget_2.rowCount()):
            match_found = False
            for j in range(self.tableWidget_2.columnCount()):
                item = self.tableWidget_2.item(i, j)
                if item and search_text in item.text().lower():
                    match_found = True
                    break
            self.tableWidget_2.setRowHidden(i, not match_found)
