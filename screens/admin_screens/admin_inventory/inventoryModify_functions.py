from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from PyQt5.QtCore import QDateTime, QTimer, pyqtSignal
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from screens.admin_screens.admin_inventory.inventoryModify import Ui_MainWindow
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
        self.pushButton_5.clicked.connect(self.confirm_clear_fields)  # Connect clear button

        self.comboBox_3.setCurrentIndex(-1)  # No initial selection
        self.comboBox_2.addItems(["Ingredient", "Beverage", "Food", "Miscellaneous"])
        self.comboBox_2.setCurrentIndex(-1)  # No initial selection
        self.comboBox.setCurrentIndex(-1)  # No initial selection

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)  # Update every second

        self.populate_comboBox_3()
        self.product_update_signal.connect(self.populate_comboBox_3)
        self.admin_product_update_signal.connect(self.populate_comboBox_3)

        # Apply QDoubleValidator to buying_cost and selling_cost fields
        double_validator = QDoubleValidator(0.00, 9999.99, 2)
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.lineEdit_5.setValidator(double_validator)
        self.lineEdit_4.setValidator(double_validator)

    def navigate_view(self):
        self.view_signal.emit()

    def navigate_add(self):
        self.add_signal.emit()

    def updateDateTime(self):
        currentDateTime = QDateTime.currentDateTime()
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")
        self.label_2.setText(formattedDateTime)

    def back(self):
        self.back_signal.emit()

    def save_product(self):
        name = self.comboBox_3.currentText()
        category = self.comboBox_2.currentText()
        buying_cost = self.lineEdit_5.text()
        selling_cost = self.lineEdit_4.text()
        status = self.comboBox.currentText()

        if not self.validate_inputs(name, category, buying_cost, selling_cost, status):
            return

        # Ensure buying cost and selling cost have exactly two decimals
        try:
            if buying_cost:
                buying_cost = '{:.2f}'.format(float(buying_cost))
            else:
                buying_cost = None

            if selling_cost:
                selling_cost = '{:.2f}'.format(float(selling_cost))
            else:
                selling_cost = None
        except ValueError:
            QMessageBox.warning(self, "Warning", "Invalid input for buying cost or selling cost.")
            return

        try:
            cursor = conn.cursor()

            product_query = """
                UPDATE product 
                SET Name = %s, Category = %s, Status = %s
                WHERE Name = %s
            """
            product_values = (name, category, status, name)
            cursor.execute(product_query, product_values)

            cursor.execute("SELECT Product_ID FROM product WHERE Name = %s", (name,))
            product_id = cursor.fetchone()[0]

            inventory_query = """
                UPDATE inventory 
                SET Buying_cost = %s, Selling_Cost = %s
                WHERE Product_ID = %s
            """
            inventory_values = (buying_cost, selling_cost, product_id)
            cursor.execute(inventory_query, inventory_values)

            conn.commit()
            QMessageBox.information(self, "Success", "Product updated successfully.")
            self.product_update_signal.emit()
            self.admin_product_update_signal.emit()

            self.clear_fields()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def validate_inputs(self, name, category, buying_cost, selling_cost, status):
        valid = True

        if not name:
            self.comboBox_3.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_3.setStyleSheet("border: 1px solid green;")

        if category not in ["Ingredient", "Beverage", "Food", "Miscellaneous"]:
            self.comboBox_2.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_2.setStyleSheet("border: 1px solid green;")

        if status not in ["Active", "Disabled"]:
            self.comboBox.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox.setStyleSheet("border: 1px solid green;")

        # Check buying cost
        if buying_cost:
            try:
                buying_cost_float = float(buying_cost)
                if not (buying_cost_float.is_integer() or round(buying_cost_float % 1, 2) == 0.00):
                    raise ValueError("Buying cost must have exactly two decimal places.")
                self.lineEdit_5.setStyleSheet("border: 1px solid green;")
            except ValueError:
                self.lineEdit_5.setStyleSheet("border: 1px solid red;")
                valid = False
        else:
            self.lineEdit_5.setStyleSheet("border: 1px solid green;")

        # Check selling cost
        if selling_cost:
            try:
                selling_cost_float = float(selling_cost)
                if not (selling_cost_float.is_integer() or round(selling_cost_float % 1, 2) == 0.00):
                    raise ValueError("Selling cost must have exactly two decimal places.")
                self.lineEdit_4.setStyleSheet("border: 1px solid green;")
            except ValueError:
                self.lineEdit_4.setStyleSheet("border: 1px solid red;")
                valid = False
        else:
            self.lineEdit_4.setStyleSheet("border: 1px solid green;")

        if not valid:
            QMessageBox.warning(self, "Warning", "Please fill in all fields correctly.")

        return valid

    def confirm_clear_fields(self):
        reply = QMessageBox.question(self, 'Warning', 'This will discard all input from the fields. Are you sure?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.clear_fields()

    def clear_fields(self):
        self.comboBox_3.setCurrentIndex(-1)
        self.comboBox_2.setCurrentIndex(-1)
        self.lineEdit_5.clear()
        self.lineEdit_4.clear()
        self.comboBox.setCurrentIndex(-1)
        self.reset_styles()

    def reset_styles(self):
        self.comboBox_3.setStyleSheet("")
        self.comboBox_2.setStyleSheet("")
        self.lineEdit_5.setStyleSheet("")
        self.lineEdit_4.setStyleSheet("")
        self.comboBox.setStyleSheet("")

    def populate_comboBox_3(self):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT Name FROM product")
            product_names = cursor.fetchall()

            self.comboBox_3.clear()
            for name in product_names:
                self.comboBox_3.addItem(name[0])

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred while populating comboBox_3: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()
