from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QDateTime, QTimer, Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from screens.employee_screens.employee_pos.posModify import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from screens.employee_screens.employee_pos.posOrderdetails_functions import posOrderdetails

class posModify(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    checkout_signal = QtCore.pyqtSignal()
    menu_signal = QtCore.pyqtSignal()
    order_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.backBTN.clicked.connect(self.goBack)
        self.checkoutBTN.clicked.connect(self.goCheckout)
        self.menuBTN.clicked.connect(self.goMenu)
        self.orderBTN.clicked.connect(self.goOrder)
        self.pushButton_8.clicked.connect(self.modifyOrder)

        self.pos_orderdetails = posOrderdetails()

        self.pos_orderdetails.transaction_generated_signal.connect(self.populate_table)
        self.pos_orderdetails.transaction_generated_signal.connect(self.populate_comboBox_5)

        # Create QTimer objects
        self.timer = QTimer()
        self.table_update_timer = QTimer()

        # Connect the timeout signal of the timers to the respective slots
        self.timer.timeout.connect(self.updateDateTime)
        self.table_update_timer.timeout.connect(self.populate_table)

        # Set the interval for the timers (in milliseconds)
        self.timer.start(1000)  # Update date and time every second
        self.table_update_timer.start(1000)  # Update table every second

        self.searchFIELD.returnPressed.connect(self.search_table)

        self.populate_table()
        self.populate_comboBox_5()
        self.populate_comboBox_6()
        self.populate_comboBox_7()

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
                           o.Soup_Variation, o.Guest_Pax, o.Priority_Order,
                           CASE
                               WHEN TIMESTAMPDIFF(MINUTE, CONCAT(o.Date, ' ', o.Time), NOW()) < 120 THEN 'Good'
                               ELSE 'Exceeding'
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
                                if col == "Good":
                                    item.setBackground(QtGui.QColor(144, 238, 144))  # Light green
                                elif col == "Exceeding":
                                    item.setBackground(QtGui.QColor(255, 99, 71))  # Light red

                            # Apply conditional formatting for the "Priority Order" column
                            if column_names[j] == "Priority Order" and col == "Priority":
                                item.setBackground(QtGui.QColor(255, 215, 0))  # Gold color for priority

                            self.tableWidget_2.setItem(i, j, item)

                    name_column_index = column_names.index("Customer Name")
                    self.tableWidget_2.setColumnWidth(name_column_index, 200)

                else:
                    print("No records found in the inventory table.")

        except Exception as e:
            print("Error occurred while populating table:", e)

        finally:
            if conn.is_connected():
                cursor.close()

    def populate_comboBox_5(self):
        try:
            cursor = conn.cursor()
            # Execute the query to retrieve Order_IDs based on the specified conditions
            query = """
                SELECT Order_ID 
                FROM `order` 
                WHERE Payment_Status = 'Pending' 
                  AND Order_Type = 'Package'
                  AND (Priority_Order = 'Non-Priority' OR Priority_Order = 'Priority')
            """
            cursor.execute(query)
            order_ids = cursor.fetchall()

            self.comboBox_5.clear()
            for order_id in order_ids:
                self.comboBox_5.addItem(str(order_id[0]))

        except Exception as e:
            print(f"Error occurred while populating comboBox_5: {e}")

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
            self.comboBox_7.addItem("")  # Add a blank item

            # Add specific values
            self.comboBox_7.addItems(["Mala soup", "Plain soup", "Suan la soup", "Tomato soup"])

        except Exception as e:
            print(f"Error occurred while populating comboBox_7: {e}")

    def modifyOrder(self):
        try:
            if conn.is_connected():
                cursor = conn.cursor()

                # Get input values
                order_id = self.comboBox_5.currentText()
                package_name = self.comboBox_6.currentText()
                guest_pax = self.lineEdit_8.text().strip()
                soup_variation = self.comboBox_7.currentText()

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
                self.populate_table()  # Refresh the table after modification

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred while modifying order: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

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
