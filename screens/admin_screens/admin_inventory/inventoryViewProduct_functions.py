from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QMainWindow
from screens.admin_screens.admin_inventory.inventoryViewProduct import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from screens.admin_screens.admin_inventory.inventoryModify_functions import adminInventoryModifyProduct
from screens.admin_screens.admin_inventory.inventoryAddProduct_functions import adminInventoryAddProduct
from screens.employee_screens.employee_inventory.inventory_Modify_functions import inventoryModify
from validator.user_manager import userManager

user_manager = userManager()

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

        # Employee modifications display
        self.inventory_modify = inventoryModify()
        self.inventory_modify.employee_update_signal.connect(self.populate_table)

        self.populate_table()

        # Create a QTimer object
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)  # Update every second

        # Connect the search field
        self.searchFIELD.returnPressed.connect(self.search_table)

    def navigate_modify(self):
        self.modify_signal.emit()

    def navigate_add(self):
        self.add_signal.emit()

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
                        product.Name,
                        product.Category,
                        product.Quantity,
                        product.Threshold_Value,
                        inventory.Buying_Cost,
                        inventory.Selling_Cost,
                        supplier.Supplier_Name,
                        product.Expiry_Date,
                        product.Status,
                        product.Availability
                    FROM inventory
                    JOIN product ON inventory.Product_ID = product.Product_ID
                    JOIN supplier ON inventory.Supplier_ID = supplier.Supplier_ID
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
            "Category",
            "Quantity",
            "Threshold Value",
            "Buying Cost",
            "Selling Cost",
            "Supplier Name",
            "Expiry Date",
            "Status",
            "Availability"
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
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Make cell non-clickable

                    # Apply conditional formatting for the "Availability" column
                    if column_names[j] == "Availability":
                        if col == "In Stock":
                            item.setBackground(QtGui.QColor(144, 238, 144))  # Light green
                        elif col == "Low Stock":
                            item.setBackground(QtGui.QColor(255, 165, 0))   # Light orange
                        elif col == "Out of Stock":
                            item.setBackground(QtGui.QColor(255, 99, 71))   # Light red

                    self.tableWidget.setItem(i, j, item)

            supplier_name_column_index = column_names.index("Supplier Name")
            self.tableWidget.setColumnWidth(supplier_name_column_index, 200)

            name_column_index = column_names.index("Name")
            self.tableWidget.setColumnWidth(name_column_index, 200)

        else:
            print("No records found in the inventory, product, and supplier tables.")

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
