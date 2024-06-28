from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QMainWindow
from screens.admin_screens.admin_inventory.inventorySupplier import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn

class adminSupplier(QMainWindow, Ui_MainWindow):
    add_signal = QtCore.pyqtSignal()
    modify_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    view_signal = QtCore.pyqtSignal()
    supplier_generated_signal = QtCore.pyqtSignal()
    supplier_updated_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.navigate_add)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_10.clicked.connect(self.navigate_modify)
        self.pushButton_11.clicked.connect(self.navigate_view)
        self.pushButton_8.clicked.connect(self.add_supplier)
        self.pushButton_9.clicked.connect(self.confirm_clear_fields)
        self.pushButton_6.clicked.connect(self.modify_supplier)
        self.pushButton_7.clicked.connect(self.confirm_clear_fields)

        self.populate_table()
        self.populate_comboBox()
        self.populate_comboBox_2()

        # Create a QTimer object
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.timeout.connect(self.updateDateTimeAndTable)

        self.timer.start(1000)  # Update every second

        # Connect the search field
        self.searchFIELD.returnPressed.connect(self.search_table)

    def updateDateTimeAndTable(self):
        self.updateDateTime()
        self.populate_table()

    def populate_comboBox_2(self):
        items = ["Active", "Disabled"]
        self.comboBox_2.addItems(items)

    def navigate_modify(self):
        self.modify_signal.emit()

    def navigate_add(self):
        self.add_signal.emit()

    def navigate_view(self):
        self.view_signal.emit()

    def updateDateTime(self):
        currentDateTime = QDateTime.currentDateTime()
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")
        self.label_2.setText(formattedDateTime)

    def back(self):
        self.back_signal.emit()
        

    def populate_table(self):
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                query = """
                    SELECT 
                        Supplier_Name,
                        Contact_Number,
                        Email,
                        Address
                    FROM supplier
                    WHERE Status = 'Active'
                """
                cursor.execute(query)
                records = cursor.fetchall()
                self.display_records(records)

        except Exception as e:
            print("Error occurred while populating table:", e)

        finally:
            if conn.is_connected():
                cursor.close()
                
    def display_records(self, records):
        column_names = [
            "Name",
            "Contact number",
            "Email",
            "Address"
        ]

        if records:
            self.tableWidget.setRowCount(len(records))
            self.tableWidget.setColumnCount(len(column_names))

            for j, name in enumerate(column_names):
                item = QTableWidgetItem(name)
                self.tableWidget.setHorizontalHeaderItem(j, item)

            for i, row in enumerate(records):
                for j, col in enumerate(row):
                    item = QTableWidgetItem("-" if col is None else str(col))
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Make cell non-clickable

                    self.tableWidget.setItem(i, j, item)

            # Set column widths
            self.tableWidget.setColumnWidth(0, 200)  # Name column width
            self.tableWidget.setColumnWidth(1, 200)  # Contact number column width
            self.tableWidget.setColumnWidth(2, 200)  # Email column width
            self.tableWidget.setColumnWidth(3, 250)  # Address Cost column width

        else:
            print("No records found for Active suppliers.")


    def search_table(self):
        search_text = self.searchFIELD.text().lower()

        for i in range(self.tableWidget.rowCount()):
            match_found = False
            for j in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(i, j)
                if item and search_text in item.text().lower():
                    match_found = True
                    break
            self.tableWidget.setRowHidden(i, not match_found)

    def add_supplier(self):
        name = self.lineEdit_13.text()
        contact_number = self.lineEdit_10.text()
        email = self.lineEdit_11.text()
        address = self.lineEdit_12.text()
        status = 'Active'

        # Validate inputs
        if not self.validate_inputs(name, contact_number, email, address):
            return

        try:
            cursor = conn.cursor()

            # Insert into supplier table
            supplier_query = """
                INSERT INTO supplier (Supplier_Name, Contact_Number, Email, Address, Status) 
                VALUES (%s, %s, %s, %s, %s)
            """

            supplier_values = (name, contact_number, email, address, status)
            cursor.execute(supplier_query, supplier_values)

            conn.commit()
            QMessageBox.information(self, "Success", "Supplier added successfully.")

            self.populate_comboBox()
            self.clear_fields()
            self.supplier_generated_signal.emit()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def validate_inputs(self, name, contact_number, email, address):
        # Flag to check if all required inputs are valid
        valid = True

        if not name:
            self.lineEdit_13.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_13.setStyleSheet("border: 1px solid green;")

        if not contact_number:
            self.lineEdit_10.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_10.setStyleSheet("border: 1px solid green;")

        if not email:
            self.lineEdit_11.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_11.setStyleSheet("border: 1px solid green;")

        if not address:
            self.lineEdit_12.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_12.setStyleSheet("border: 1px solid green;")


        if not valid:
            QMessageBox.warning(self, "Warning", "Please fill in all fields correctly.")

        return valid

    def clear_fields(self):
        # Clear all input fields and reset styles
        self.lineEdit_13.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.lineEdit_8.clear()
        self.lineEdit_7.clear()
        self.lineEdit_9.clear()
        self.reset_styles()
        self.comboBox.setCurrentIndex(-1)
        self.comboBox_2.setCurrentIndex(-1)

    def reset_styles(self):
        self.lineEdit_13.setStyleSheet("")
        self.lineEdit_10.setStyleSheet("")
        self.lineEdit_11.setStyleSheet("")
        self.lineEdit_12.setStyleSheet("")
        self.comboBox.setStyleSheet("")
        self.lineEdit_7.setStyleSheet("")
        self.lineEdit_8.setStyleSheet("")
        self.lineEdit_9.setStyleSheet("")

    def confirm_clear_fields(self):
        reply = QMessageBox.question(self, 'Warning', 'This will discard all input from the fields. Are you sure?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.clear_fields()

    def populate_comboBox(self):
        try:
            if conn.is_connected():
                cursor = conn.cursor()

                # Execute the query to retrieve supplier names
                query = "SELECT Supplier_Name FROM supplier"
                cursor.execute(query)

                # Fetch all the supplier names
                supplier_names = cursor.fetchall()

                # Clear the comboBox_2 before adding new items
                self.comboBox.clear()

                # Add each supplier name to the comboBox_2
                for name in supplier_names:
                    self.comboBox.addItem(name[0])

            else:
                print("No connection to the database.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred while populating comboBox_2: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def modify_supplier(self):
        name1 = self.comboBox.currentText()
        contact_number1 = self.lineEdit_7.text()
        email1 = self.lineEdit_8.text()
        address1 = self.lineEdit_9.text()
        status1 = self.comboBox_2.currentText()

        if not self.validate_inputs1(name1, contact_number1, email1, address1):
            return

        try:
            cursor = conn.cursor()

            cursor.execute("SELECT Supplier_ID FROM supplier WHERE Supplier_Name = %s", (name1,))
            supplier_id = cursor.fetchone()[0]

            supplier_query1 = """
                    UPDATE supplier
                    SET Contact_number = %s, Email = %s, Address = %s, Status = %s
                    WHERE Supplier_id = %s
                """
            supplier_values1 = (contact_number1, email1, address1, status1, supplier_id)
            cursor.execute(supplier_query1, supplier_values1)

            conn.commit()
            QMessageBox.information(self, "Success", "Supplier updated successfully.")

            self.supplier_updated_signal.emit()
            self.clear_fields()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def validate_inputs1(self, name1, contact_number1, email1, address1):
        # Flag to check if all required inputs are valid
        valid1 = True


        if not name1:
            self.comboBox.setStyleSheet("border: 1px solid red;")
            valid1 = False
        else:
            self.comboBox.setStyleSheet("border: 1px solid green;")

        if not contact_number1:
            self.lineEdit_7.setStyleSheet("border: 1px solid red;")
            valid1 = False
        else:
            self.lineEdit_7.setStyleSheet("border: 1px solid green;")

        if not email1:
            self.lineEdit_8.setStyleSheet("border: 1px solid red;")
            valid1 = False
        else:
            self.lineEdit_8.setStyleSheet("border: 1px solid green;")

        if not address1:
            self.lineEdit_9.setStyleSheet("border: 1px solid red;")
            valid1 = False
        else:
            self.lineEdit_9.setStyleSheet("border: 1px solid green;")


        if not valid1:
            QMessageBox.warning(self, "Warning", "Please fill in all fields correctly.")

        return valid1
