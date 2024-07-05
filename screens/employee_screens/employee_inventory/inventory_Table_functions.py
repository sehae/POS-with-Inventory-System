from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QDateTime, QTimer, Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from screens.employee_screens.employee_inventory.inventory_Table import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from validator.user_manager import userManager

user_manager = userManager()

class inventoryTable(QMainWindow, Ui_MainWindow):
    modify_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.navigate_modify)
        self.pushButton.clicked.connect(self.back)

        self.populate_table()

        # Connect search field
        self.searchFIELD.returnPressed.connect(self.search_table)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        self.timer.timeout.connect(self.updateDateTimeAndTable)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        # Connect the fullname_updated signal to the slot
        user_manager.fullname_updated.connect(self.update_fullname_label)

        # Set initial fullname if already set
        if user_manager.get_current_fullname():
            self.update_fullname_label(user_manager.get_current_fullname())

    def updateDateTimeAndTable(self):
        self.updateDateTime()
        self.populate_table()

    def update_fullname_label(self, fullname):
        self.label_3.setText(fullname)  # Update the label with the fullname

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

    def populate_table(self):
        try:
            if conn.is_connected():
                cursor = conn.cursor()

                # Execute the query to retrieve data for specific columns
                query = """
                    SELECT Name, Quantity, Threshold_Value, Expiry_Date, Category,
                        CASE
                            WHEN Quantity = 0 THEN 'Out of Stock'
                            WHEN Quantity <= Threshold_Value THEN 'Low Stock'
                            ELSE 'In Stock'
                        END AS Availability
                    FROM product
                    WHERE Status = 'active'
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

                            # Apply conditional formatting for the "Availability" column
                            if column_names[j] == "Availability":
                                if col == "In Stock":
                                    item.setBackground(QtGui.QColor(144, 238, 144))  # Light green
                                elif col == "Low Stock":
                                    item.setBackground(QtGui.QColor(255, 165, 0))   # Light orange
                                elif col == "Out of Stock":
                                    item.setBackground(QtGui.QColor(255, 99, 71))   # Light red

                            self.tableWidget_2.setItem(i, j, item)

                    name_column_index = column_names.index("Name")
                    self.tableWidget_2.setColumnWidth(name_column_index, 200)

        except Exception as e:
            print("Error occurred while populating table:", e)

        finally:
            if conn.is_connected():
                cursor.close()

    def search_table(self):
        search_text = self.searchFIELD.text().lower()
        filtered_records = [row for row in self.records if search_text in str(row).lower()]

        self.tableWidget_2.setRowCount(len(filtered_records))

        for i, row in enumerate(filtered_records):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Make cell non-clickable

                # Apply conditional formatting for the "Availability" column
                if self.tableWidget_2.horizontalHeaderItem(j).text() == "Availability":
                    if col == "In Stock":
                        item.setBackground(QtGui.QColor(144, 238, 144))  # Light green
                    elif col == "Low Stock":
                        item.setBackground(QtGui.QColor(255, 165, 0))   # Light orange
                    elif col == "Out of Stock":
                        item.setBackground(QtGui.QColor(255, 99, 71))   # Light red

                self.tableWidget_2.setItem(i, j, item)
