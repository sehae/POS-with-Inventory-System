from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow, QHeaderView
from PyQt5.QtCore import QDateTime, QTimer, QRegExp, Qt
from screens.employee_screens.employee_pos.posHistory import Ui_MainWindow
from shared.navigation_signal import auth_back, pos_back
from server.local_server import conn
from validator.user_manager import userManager

class posHistory(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    back_cashier_signal = QtCore.pyqtSignal()
    checkout_signal = QtCore.pyqtSignal()
    modify_signal = QtCore.pyqtSignal()
    order_signal = QtCore.pyqtSignal()
    menu_signal = QtCore.pyqtSignal()
    void_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user_manager = userManager()

        self.backBTN.clicked.connect(lambda: pos_back(self.user_manager, self.back_signal, self.back_cashier_signal))
        self.checkoutBTN.clicked.connect(self.checkout_signal.emit)
        self.modifyBTN.clicked.connect(self.modify_signal.emit)
        self.orderBTN.clicked.connect(self.order_signal.emit)
        self.menuBTN.clicked.connect(self.menu_signal.emit)
        self.voidBTN.clicked.connect(self.void_signal.emit)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.timeout.connect(self.updateDateTimeAndTable)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        # Connect the search field
        self.searchFIELD.returnPressed.connect(self.search_table)

    def updateDateTimeAndTable(self):
        self.updateDateTime()
        self.populate_table()

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.date.setText(formattedDateTime)

    def populate_table(self):
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                query = """
                    SELECT 
                        *
                    FROM `order`
                """
                cursor.execute(query)
                records = cursor.fetchall()
                self.display_records(records)

                self.tableWidget_2.setColumnWidth(0, 150)  # Adjust the index if necessary
        except Exception as e:
            print("Error occurred while populating table:", e)
        finally:
            if conn.is_connected():
                cursor.close()

    def display_records(self, records):
        column_names = [
            "Order\nID", "Date", "Time", "Total\nAmount", "Payment\nStatus", "Package\nID",
            "Leftover\nID", "Customer\nName", "Soup\nVariation", "Guest\nPax", "Time\nStatus",
            "Order\nType", "Payment\nMethod", "Cash\nAmount", "Reference\nID", "Discount\nType",
            "Priority\nOrder", "Subtotal\nAmount", "VAT\nAmount", "Discount\nAmount",
            "Change\nAmount", "Package\nTotal Amount", "Add-ons\nTotal Amount"
        ]

        if records:
            self.tableWidget_2.setRowCount(len(records))
            self.tableWidget_2.setColumnCount(len(column_names))

            for j, name in enumerate(column_names):
                item = QTableWidgetItem(name)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.tableWidget_2.setHorizontalHeaderItem(j, item)

            for i, row in enumerate(records):
                for j, col in enumerate(row):
                    item = QTableWidgetItem("-" if col is None else str(col))
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Make cell non-clickable
                    self.tableWidget_2.setItem(i, j, item)

            # Resize rows to fit contents
            self.tableWidget_2.resizeRowsToContents()

            # Stretch columns to fill available horizontal space
            self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

            # Optional: Adjust header alignment and wrap text in header cells
            self.tableWidget_2.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
            for i in range(len(column_names)):
                header_item = self.tableWidget_2.horizontalHeaderItem(i)
                header_item.setTextAlignment(Qt.AlignCenter | Qt.TextWordWrap)
        else:
            print("No records found in the order table.")

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
