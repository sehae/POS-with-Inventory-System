from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from screens.employee_screens.employee_inventory.inventory_Modify import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn

class inventoryModify(QMainWindow, Ui_MainWindow):
    barcode_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    inventory_table = QtCore.pyqtSignal()
    product_update_signal = QtCore.pyqtSignal()
    employee_update_signal = QtCore.pyqtSignal()


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_10.clicked.connect(self.navigate_barcode)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_3.clicked.connect(self.navigate_inventory)
        self.pushButton_4.clicked.connect(self.save_product)

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

        self.comboBox.addItems(["Ingredient", "Beverage"])

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.label_2.setText(formattedDateTime)

    def navigate_barcode(self):
        self.barcode_signal.emit()

    def navigate_inventory(self):
        self.inventory_table.emit()

    def back(self):
        self.back_signal.emit()

    def save_product(self):
        name = self.lineEdit_2.text()
        category = self.comboBox.currentText()
        quantity = self.lineEdit_4.text()
        expiry_date = self.lineEdit_3.text()
        threshold_value = self.lineEdit_5.text()

        # Check if any field is empty
        if not name or not category or not quantity or not expiry_date or not threshold_value:
            QMessageBox.warning(self, "Warning", "Please fill in all fields.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute(f"""
                UPDATE product 
                SET 
                    Quantity={quantity}, 
                    Threshold_Value={threshold_value}, 
                    Category='{category}', 
                    Expiry_Date='{expiry_date}', 
                    Availability = 
                        CASE 
                            WHEN {quantity} = 0 THEN 'Out of Stock' 
                            WHEN {quantity} <= {threshold_value} THEN 'Low Stock' 
                            ELSE 'In Stock' 
                        END 
                WHERE Name='{name}'
            """)
            conn.commit()
            QMessageBox.information(self, "Success", "Product updated successfully.")
            self.product_update_signal.emit()
            self.employee_update_signal.emit()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred: {str(e)}")
