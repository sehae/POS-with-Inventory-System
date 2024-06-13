from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QMainWindow
from screens.admin_screens.admin_inventory.inventoryModify import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn

class adminInventoryModifyProduct(QMainWindow, Ui_MainWindow):
    add_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    view_signal = QtCore.pyqtSignal()
    product_update_signal = QtCore.pyqtSignal()
    admin_product_update_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.navigate_add)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_11.clicked.connect(self.navigate_view)
        self.pushButton_4.clicked.connect(self.save_product)

        self.comboBox_2.addItems(["Ingredient", "Beverage"])

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

    def navigate_view(self):
        self.view_signal.emit()

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

    def save_product(self):
        name = self.lineEdit_2.text()
        category = self.comboBox_2.currentText()
        selling_cost = self.lineEdit_4.text()
        status = self.comboBox.currentText()

        # Check if any field is empty
        if not name or not category or not selling_cost or not status:
            QMessageBox.warning(self, "Warning", "Please fill in all fields.")
            return

        try:
            cursor = conn.cursor()

            # Update product table
            product_query = """
                UPDATE product 
                SET Name = %s, Category = %s, Status = %s
                WHERE Name = %s
            """
            product_values = (name, category, status, name)
            cursor.execute(product_query, product_values)

            # Fetch Product_ID based on the updated name
            cursor.execute("SELECT Product_ID FROM product WHERE Name = %s", (name,))
            product_id = cursor.fetchone()[0]

            # Update selling cost in inventory table based on Product_ID
            inventory_query = """
                UPDATE inventory 
                SET Selling_Cost = %s
                WHERE Product_ID = %s
            """
            inventory_values = (selling_cost, product_id)
            cursor.execute(inventory_query, inventory_values)

            conn.commit()
            QMessageBox.information(self, "Success", "Product updated successfully.")
            self.product_update_signal.emit()
            self.admin_product_update_signal.emit()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred: {str(e)}")

