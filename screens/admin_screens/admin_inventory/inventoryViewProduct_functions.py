from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from screens.admin_screens.admin_inventory.inventoryViewProduct import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from screens.admin_screens.admin_inventory.inventoryModify_functions import adminInventoryModifyProduct
from screens.admin_screens.admin_inventory.inventoryAddProduct_functions import adminInventoryAddProduct
from screens.employee_screens.employee_inventory.inventory_Modify_functions import inventoryModify

class adminInventoryViewProduct(QMainWindow, Ui_MainWindow):
    add_signal = QtCore.pyqtSignal()
    modify_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    admin_product_update_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.navigate_add)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_10.clicked.connect(self.navigate_modify)

        self.admin_inventory_modify = adminInventoryModifyProduct()

        self.admin_inventory_modify.product_update_signal.connect(self.populate_table)

        self.admin_inventory = adminInventoryAddProduct()

        self.admin_inventory.product_update_signal.connect(self.populate_table)

        #Employee modifications display
        self.inventory_modify = inventoryModify()

        self.inventory_modify.employee_update_signal.connect(self.populate_table)

        self.populate_table()

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

    def navigate_modify(self):
        self.modify_signal.emit()

    def navigate_add(self):
        self.add_signal.emit()

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.label_2.setText(formattedDateTime)

    def back(self):
        self.back_signal.emit()

    def populate_table(self):
        try:
            if conn.is_connected():
                cursor = conn.cursor()

                # Execute the query to retrieve data
                query = """
                    SELECT 
                        product.Name,
                        product.Category,
                        product.Quantity,
                        product.Expiry_Date,
                        product.Threshold_Value,
                        inventory.Buying_Cost,
                        inventory.Selling_Cost,
                        supplier.Supplier_Name,
                        product.Status
                    FROM inventory
                    JOIN product ON inventory.Product_ID = product.Product_ID
                    JOIN supplier ON inventory.Supplier_ID = supplier.Supplier_ID
                """
                cursor.execute(query)

                # Column names to be displayed
                column_names = [
                    "Name",
                    "Category",
                    "Quantity",
                    "Expiry Date",
                    "Threshold Value",
                    "Buying Cost",
                    "Selling Cost",
                    "Supplier Name",
                    "Status"
                ]

                # Fetch all the records
                records = cursor.fetchall()

                if records:  # Check if records is not empty
                    # Set the number of rows and columns in the table widget
                    self.tableWidget.setRowCount(len(records))
                    self.tableWidget.setColumnCount(len(column_names))

                    # Populate the column names as horizontal headers
                    for j, name in enumerate(column_names):
                        item = QTableWidgetItem(name)
                        self.tableWidget.setHorizontalHeaderItem(j, item)

                    # Populate the table widget with data
                    for i, row in enumerate(records):
                        for j, col in enumerate(row):
                            if col is None:
                                item = QTableWidgetItem("-")
                            else:
                                item = QTableWidgetItem(str(col))
                            self.tableWidget.setItem(i, j, item)

                    # Set the width for specific columns
                    supplier_name_column_index = column_names.index("Supplier Name")
                    self.tableWidget.setColumnWidth(supplier_name_column_index, 200)

                    name_column_index = column_names.index("Name")
                    self.tableWidget.setColumnWidth(name_column_index, 200)

                else:
                    print("No records found in the inventory, product, and supplier tables.")

        except Exception as e:
            print("Error occurred while populating table:", e)

        finally:
            if conn.is_connected():
                cursor.close()
