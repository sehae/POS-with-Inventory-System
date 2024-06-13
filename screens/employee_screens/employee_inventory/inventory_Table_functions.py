from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from screens.employee_screens.employee_inventory.inventory_Table import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from screens.employee_screens.employee_inventory.inventory_Modify_functions import inventoryModify
from screens.admin_screens.admin_inventory.inventoryModify_functions import adminInventoryModifyProduct
from screens.admin_screens.admin_inventory.inventoryAddProduct_functions import adminInventoryAddProduct

class inventoryTable(QMainWindow, Ui_MainWindow):
    modify_signal = QtCore.pyqtSignal()
    barcode_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.navigate_modify)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_10.clicked.connect(self.navigate_barcode)

        self.inventory_modify = inventoryModify()
        self.admin_inventory_modify = adminInventoryModifyProduct()
        self.admin_inventory_add = adminInventoryAddProduct()

        self.inventory_modify.product_update_signal.connect(self.populate_table)
        self.admin_inventory_modify.admin_product_update_signal.connect(self.populate_table)
        self.admin_inventory_add.admin_product_update_signal.connect(self.populate_table)

        self.populate_table()

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.label_2.setText(formattedDateTime)

    def navigate_modify(self):
        self.modify_signal.emit()

    def back(self):
        self.back_signal.emit()

    def navigate_barcode(self):
        self.barcode_signal.emit()

    def populate_table(self):
        try:
            if conn.is_connected():
                cursor = conn.cursor()

                # Execute the query to retrieve data for specific columns
                cursor.execute("SELECT Name, Quantity, Threshold_Value, Expiry_Date, Category, \
                                CASE \
                                    WHEN Quantity = 0 THEN 'Out of Stock' \
                                    WHEN Quantity <= Threshold_Value THEN 'Low Stock' \
                                    ELSE 'In Stock' \
                                END AS Availability \
                                FROM product")

                # Fetch column names
                column_names = [i[0].replace('_', ' ') for i in cursor.description]  # Replace '_' with ' '

                # Fetch all the records
                records = cursor.fetchall()

                if records:  # Check if records is not empty
                    # Set the number of rows and columns in the table widget
                    self.tableWidget_2.setRowCount(len(records))
                    self.tableWidget_2.setColumnCount(len(column_names))

                    # Populate the column names
                    for j, name in enumerate(column_names):
                        item = QTableWidgetItem(name)
                        self.tableWidget_2.setHorizontalHeaderItem(j, item)

                    # Populate the table widget with data
                    for i, row in enumerate(records):
                        for j, col in enumerate(row):
                            item = QTableWidgetItem(str(col))
                            self.tableWidget_2.setItem(i, j, item)

                else:
                    print("No records found in the inventory table.")

        except Exception as e:
            print("Error occurred while populating table:", e)

        finally:
            if conn.is_connected():
                cursor.close()
