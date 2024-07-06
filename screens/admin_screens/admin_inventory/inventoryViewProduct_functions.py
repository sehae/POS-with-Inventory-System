from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QDialog, QApplication, QDialog, QMainWindow
from PyQt5.QtCore import QDateTime, QTimer, Qt, QDate, QEvent, QObject
from PyQt5.QtWidgets import QMainWindow
from screens.admin_screens.admin_inventory.inventoryViewProduct import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from screens.employee_screens.employee_inventory.inventory_Modify_functions import inventoryModify
from screens.admin_screens.admin_inventory.barcode_functions import BarcodeDialog
from screens.admin_screens.admin_inventory.inventorySupplier_functions import adminSupplier
from modules.inventory.barcode_generator import generate_barcode
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from validator.user_manager import userManager

user_manager = userManager()

class adminInventoryViewProduct(QMainWindow, Ui_MainWindow):
    add_signal = QtCore.pyqtSignal()
    modify_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    supplier_signal = QtCore.pyqtSignal()
    admin_product_update_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.back)
        self.pushButton_12.clicked.connect(self.navigate_supplier)
        self.pushButton_4.clicked.connect(self.open_add_dialog)
        self.pushButton_5.clicked.connect(self.open_modify_dialog)

        # Employee modifications display
        self.inventory_modify = inventoryModify()
        self.inventory_modify.employee_update_signal.connect(self.populate_table)

        self.populate_table()

        # Create a QTimer object
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.timeout.connect(self.updateDateTimeAndTable)

        self.timer.start(1000)  # Update every second

        self.tableWidget.itemSelectionChanged.connect(self.on_table_item_selected)

        # Connect the search field
        self.searchFIELD.returnPressed.connect(self.search_table)

        # Initialize dialog1 here
        self.dialog1 = ModifyDialog()
        self.dialog1.setWindowTitle('Modify Product')

    def on_table_item_selected(self):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            product_id = self.tableWidget.item(selected_row, 0).text()
            product_name = self.tableWidget.item(selected_row, 1).text()
            category = self.tableWidget.item(selected_row, 4).text()
            buying_cost = self.tableWidget.item(selected_row, 7).text()
            selling_cost = self.tableWidget.item(selected_row, 8).text()
            status = self.tableWidget.item(selected_row, 11).text()

            # Convert '-' to '0.00' if necessary
            if buying_cost == '-':
                buying_cost = '0.00'
            if selling_cost == '-':
                selling_cost = '0.00'

            # Set values in ModifyDialog fields
            self.dialog1.label.setText(product_id)
            self.dialog1.label_2.setText(product_name)
            self.dialog1.comboBox_2.setCurrentIndex(self.dialog1.comboBox_2.findText(category))
            self.dialog1.lineEdit_5.setText(buying_cost)
            self.dialog1.lineEdit_4.setText(selling_cost)
            self.dialog1.comboBox.setCurrentIndex(self.dialog1.comboBox.findText(status))
        else:
            QMessageBox.warning(self, 'Warning', 'Please select an item to modify.')

    def open_modify_dialog(self):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            self.dialog1.exec_()
        else:
            QMessageBox.warning(self, 'Error', 'Please select an item to modify.')


    def open_add_dialog(self):
        self.dialog = AddDialog()
        self.dialog.setWindowTitle('Add Product')
        self.dialog.product_update_signal.connect(self.populate_table)
        self.dialog.exec_()

    def updateDateTimeAndTable(self):
        self.updateDateTime()
        self.populate_table()

    def navigate_modify(self):
        self.modify_signal.emit()

    def navigate_add(self):
        self.add_signal.emit()

    def updateDateTime(self):
        currentDateTime = QDateTime.currentDateTime()
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")
        self.label_2.setText(formattedDateTime)

    def navigate_supplier(self):
        self.supplier_signal.emit()

    def back(self):
        self.back_signal.emit()

    def populate_table(self):
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                query = """
                    SELECT 
                        product.Product_ID,
                        product.Name,
                        product.Date,
                        product.Time,
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
            "Product ID",
            "Name",
            "Date",
            "Time",
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



class AddDialog(QDialog):
    product_update_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.barcode_dialog = None

        self.pushButton_4.clicked.connect(self.add_product)
        self.pushButton_5.clicked.connect(self.confirm_clear_fields)

        # Add items to comboBox
        self.comboBox.addItems(["Ingredient", "Beverage"])
        self.comboBox.setCurrentIndex(-1)  # No initial selection

        # Call populateComboBox to fill comboBox_2 with supplier names
        self.populateComboBox()
        self.comboBox_2.setCurrentIndex(-1)  # No initial selection

        # Set the default expiry date to 2024/01/01
        default_date = QDate(2024, 1, 1)
        self.dateEdit.setDate(default_date)

        # Integer only in quantity and threshold value
        int_validator = QIntValidator()
        self.lineEdit_4.setValidator(int_validator)
        self.lineEdit_7.setValidator(int_validator)

        self.admin_supplier = adminSupplier()
        self.admin_supplier.supplier_generated_signal.connect(self.populateComboBox)
        self.admin_supplier.supplier_updated_signal.connect(self.populateComboBox)

        # Apply QDoubleValidator to buying_cost and selling_cost fields
        double_validator = QDoubleValidator(0.00, 9999.99, 2)
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.lineEdit_3.setValidator(double_validator)
        self.lineEdit_5.setValidator(double_validator)

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(614, 652)
        self.widget_2 = QtWidgets.QWidget(self)
        self.widget_2.setGeometry(QtCore.QRect(30, 20, 568, 603))
        self.widget_2.setObjectName("widget_2")
        self.formLayout = QtWidgets.QFormLayout(self.widget_2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(25)
        self.formLayout.setObjectName("formLayout")

        self.label_4 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)

        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setMinimumSize(QtCore.QSize(400, 35))
        self.comboBox.setMaximumSize(QtCore.QSize(400, 35))
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)

        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)

        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)

        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)

        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)

        self.comboBox_2 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_2.setMinimumSize(QtCore.QSize(400, 35))
        self.comboBox_2.setMaximumSize(QtCore.QSize(400, 35))
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)

        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_11)

        self.dateEdit = QtWidgets.QDateEdit(self.widget_2)
        self.dateEdit.setMinimumSize(QtCore.QSize(400, 35))
        self.dateEdit.setMaximumSize(QtCore.QSize(400, 35))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2024, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.dateEdit)

        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_12)

        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)

        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "    background-color: #67B99A;\n"
                                        "    color: white;\n"
                                        "    border: 2px solid #67B99A;\n"
                                        "    padding: 8px 16px;\n"
                                        "    border-radius: 15px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #5CAE8B;\n"
                                        "    border: 2px solid #5CAE8B;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #4D9C7F;\n"
                                        "    border: 2px solid #4D9C7F;\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_5.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
                                        "    background-color: white;\n"
                                        "    border: 2px solid #67B99A;\n"
                                        "    color: black;\n"
                                        "    padding: 8px 16px;\n"
                                        "    border-radius: 15px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border: 2px solid #4D926D;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #F0F0F0;\n"
                                        "    border: 2px solid #265C42;\n"
                                        "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.widget_3)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Add Product"))
        self.label_5.setText(_translate("Dialog", "Product Name"))
        self.label_6.setText(_translate("Dialog", "Category"))
        self.label_7.setText(_translate("Dialog", "Quantity"))
        self.label_8.setText(_translate("Dialog", "Buying Cost"))
        self.label_9.setText(_translate("Dialog", "Selling Cost"))
        self.label_10.setText(_translate("Dialog", "Supplier"))
        self.label_11.setText(_translate("Dialog", "Expiry Date"))
        self.dateEdit.setDisplayFormat(_translate("Dialog", "yyyy/MM/dd"))
        self.label_12.setText(_translate("Dialog", "Threshold Value"))
        self.pushButton_4.setText(_translate("Dialog", "Add Product"))
        self.pushButton_5.setText(_translate("Dialog", "Discard"))

    def add_product(self):
        # Get the values entered by the user
        name = self.lineEdit_2.text()
        category = self.comboBox.currentText()
        quantity = self.lineEdit_4.text()
        buying_cost = self.lineEdit_3.text()
        selling_cost = self.lineEdit_5.text()
        supplier_name = self.comboBox_2.currentText()
        expiry_date = self.dateEdit.date().toString('yyyy-MM-dd')
        threshold_value = self.lineEdit_7.text()

        # Validate inputs
        if not self.validate_inputs(name, category, quantity, buying_cost, selling_cost, supplier_name,
                                    threshold_value):
            return

        try:
            cursor = conn.cursor()

            # Calculate availability based on quantity and threshold value
            if int(quantity) == 0:
                availability = 'Out of Stock'
            elif int(quantity) <= int(threshold_value):
                availability = 'Low Stock'
            else:
                availability = 'In Stock'

            # Fetch the latest Product_ID for the current date
            cursor.execute("SELECT MAX(Product_ID) FROM product")
            latest_product_id = cursor.fetchone()[0]

            if latest_product_id:
                # Extract numeric part and increment
                numeric_part = latest_product_id[3:]  # Assuming Product_ID format is PRDNNN
                product_number = int(numeric_part)
                new_product_number = product_number + 1
                next_product_number = f"{new_product_number:03d}"
            else:
                # If no previous products, start from 001
                next_product_number = "001"

            # Construct new Product_ID
            new_product_id = f"PRD{next_product_number}"

            # Get the value of supplier id where supplier name gathered by the user
            cursor.execute("SELECT Supplier_ID FROM supplier WHERE Supplier_Name = %s", (supplier_name,))
            supplier_result = cursor.fetchone()

            if supplier_result is None:
                QMessageBox.critical(self, "Error", "Supplier not found.")
                return

            supplier_id = supplier_result[0]

            # Get current date in yyyy-MM-dd format
            current_date = QDateTime.currentDateTime().toString("yyyy-MM-dd")

            # Get current time in HH:mm format
            current_time = QDateTime.currentDateTime().toString("HH:mm")

            # Insert into product table
            product_query = """
                INSERT INTO product (Product_ID, Name, Original_Quantity, Quantity, Category, Expiry_Date, Threshold_Value, Availability, Status, Date, Time) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'Active', %s, %s)
            """
            product_values = (
            new_product_id, name, quantity, quantity, category, expiry_date, threshold_value, availability,
            current_date, current_time)
            cursor.execute(product_query, product_values)

            barcode_str = generate_barcode(name)

            # Insert into inventory table
            if category == "Ingredient":
                inventory_query = """
                    INSERT INTO inventory (Supplier_ID, Product_ID, Buying_Cost, Barcode) 
                    VALUES (%s, %s, %s, %s)
                """
                inventory_values = (supplier_id, new_product_id, buying_cost, barcode_str)
            else:
                inventory_query = """
                    INSERT INTO inventory (Supplier_ID, Product_ID, Buying_Cost, Selling_Cost, Barcode) 
                    VALUES (%s, %s, %s, %s, %s)
                """
                inventory_values = (supplier_id, new_product_id, buying_cost, selling_cost or None, barcode_str)

            cursor.execute(inventory_query, inventory_values)

            conn.commit()
            QMessageBox.information(self, "Success", "Product added successfully.")
            self.product_update_signal.emit()
            self.open_barcode()

            self.clear_fields()  # Clear fields after successful addition

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def validate_inputs(self, name, category, quantity, buying_cost, selling_cost, supplier_name, threshold_value):
        # Flag to check if all required inputs are valid
        valid = True

        if not name:
            self.lineEdit_2.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_2.setStyleSheet("border: 1px solid green;")

        if category not in ["Ingredient", "Beverage"]:
            self.comboBox.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox.setStyleSheet("border: 1px solid green;")

        if not quantity:
            self.lineEdit_4.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_4.setStyleSheet("border: 1px solid green;")

        if not buying_cost:
            self.lineEdit_3.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            try:
                buying_cost_float = float(buying_cost)
                if round(buying_cost_float % 1, 2) == 0.00:
                    self.lineEdit_3.setStyleSheet("border: 1px solid green;")
                else:
                    raise ValueError("Buying cost must have exactly two decimal places.")
            except ValueError:
                self.lineEdit_3.setStyleSheet("border: 1px solid red;")
                valid = False

        if category == "Ingredient":
            if selling_cost:
                self.lineEdit_5.setStyleSheet("border: 1px solid red;")
                valid = False
                QMessageBox.warning(self, "Warning", "Selling price should not be provided for Ingredients.")
            else:
                self.lineEdit_5.setStyleSheet("border: 1px solid green;")
        else:
            if not selling_cost:
                self.lineEdit_5.setStyleSheet("border: 1px solid red;")
                valid = False
            else:
                try:
                    selling_cost_float = float(selling_cost)
                    if round(selling_cost_float % 1, 2) == 0.00:
                        self.lineEdit_5.setStyleSheet("border: 1px solid green;")
                    else:
                        raise ValueError("Selling cost must have exactly two decimal places.")
                except ValueError:
                    self.lineEdit_5.setStyleSheet("border: 1px solid red;")
                    valid = False

        if not supplier_name:
            self.comboBox_2.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_2.setStyleSheet("border: 1px solid green;")

        if not threshold_value:
            self.lineEdit_7.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_7.setStyleSheet("border: 1px solid green;")

        if not valid:
            QMessageBox.warning(self, "Warning", "Please fill in all fields correctly.")

        return valid

    def confirm_clear_fields(self):
        reply = QMessageBox.question(self, 'Warning', 'This will discard all input from the fields. Are you sure?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.clear_fields()

    def clear_fields(self):
        # Clear all input fields and reset styles
        self.lineEdit_2.clear()
        self.comboBox.setCurrentIndex(-1)
        self.lineEdit_4.clear()
        self.lineEdit_3.clear()
        self.lineEdit_5.clear()
        self.comboBox_2.setCurrentIndex(-1)
        self.dateEdit.setDate(QDate(2024, 1, 1))
        self.lineEdit_7.clear()
        self.reset_styles()

    def reset_styles(self):
        self.lineEdit_2.setStyleSheet("")
        self.comboBox.setStyleSheet("")
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_5.setStyleSheet("")
        self.comboBox_2.setStyleSheet("")
        self.dateEdit.setStyleSheet("")
        self.lineEdit_7.setStyleSheet("")

    def populateComboBox(self):
        try:
            if conn.is_connected():
                cursor = conn.cursor()

                # Execute the query to retrieve supplier names
                query = "SELECT Supplier_Name FROM supplier WHERE Status = 'Active'"
                cursor.execute(query)

                # Fetch all the supplier names
                supplier_names = cursor.fetchall()

                # Clear the comboBox_2 before adding new items
                self.comboBox_2.clear()

                # Add each supplier name to the comboBox_2
                for name in supplier_names:
                    self.comboBox_2.addItem(name[0])

            else:
                print("No connection to the database.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred while populating comboBox_2: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def open_barcode(self):
        self.barcode_dialog = BarcodeDialog()
        self.barcode_dialog.show()

class ModifyDialog(QDialog):
    product_update_signal = QtCore.pyqtSignal()
    admin_product_update_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_4.clicked.connect(self.save_product)
        self.pushButton_5.clicked.connect(self.confirm_clear_fields)  # Connect clear but\ton

        self.comboBox_2.addItems(["Ingredient", "Beverage"])
        self.comboBox_2.setCurrentIndex(-1)  # No initial selection
        self.comboBox.setCurrentIndex(-1)  # No initial selection

        # Apply QDoubleValidator to buying_cost and selling_cost fields
        double_validator = QDoubleValidator(0.00, 9999.99, 2)
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.lineEdit_5.setValidator(double_validator)
        self.lineEdit_4.setValidator(double_validator)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 528)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(30, 30, 636, 501))
        self.widget_2.setObjectName("widget_2")
        self.formLayout = QtWidgets.QFormLayout(self.widget_2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(25)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_2.setMinimumSize(QtCore.QSize(400, 35))
        self.comboBox_2.setMaximumSize(QtCore.QSize(400, 35))
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setMinimumSize(QtCore.QSize(400, 35))
        self.comboBox.setMaximumSize(QtCore.QSize(400, 35))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "    background-color: #67B99A;\n"
                                        "    color: white;\n"
                                        "    border: 2px solid #67B99A;\n"
                                        "    padding: 8px 16px;\n"
                                        "    border-radius: 15px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #5CAE8B;\n"
                                        "    border: 2px solid #5CAE8B;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #4D9C7F;\n"
                                        "    border: 2px solid #4D9C7F;\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_5.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
                                        "    background-color: white;\n"
                                        "    border: 2px solid #67B99A;\n"
                                        "    color: black;\n"
                                        "    padding: 8px 16px;\n"
                                        "    border-radius: 15px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border: 2px solid #4D926D;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #F0F0F0;\n"
                                        "    border: 2px solid #265C42;\n"
                                        "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.widget_3)
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMinimumSize(QtCore.QSize(400, 35))
        self.label.setMaximumSize(QtCore.QSize(400, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(400, 35))
        self.label_2.setMaximumSize(QtCore.QSize(400, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_2)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.label_4.setText(_translate("Dialog", "Modify Product"))
        self.label_5.setText(_translate("Dialog", "Product Name"))
        self.label_6.setText(_translate("Dialog", "Category"))
        self.label_9.setText(_translate("Dialog", "Buying Cost"))
        self.label_7.setText(_translate("Dialog", "Selling Cost"))
        self.label_8.setText(_translate("Dialog", "Status"))
        self.comboBox.setItemText(0, _translate("Dialog", "Active"))
        self.comboBox.setItemText(1, _translate("Dialog", "Disabled"))
        self.pushButton_4.setText(_translate("Dialog", "Update Product"))
        self.pushButton_5.setText(_translate("Dialog", "Discard"))
        self.label_10.setText(_translate("Dialog", "Product ID"))

    def save_product(self):
        name = self.label_2.text()
        category = self.comboBox_2.currentText()
        buying_cost = self.lineEdit_5.text()
        selling_cost = self.lineEdit_4.text()
        status = self.comboBox.currentText()

        if not self.validate_inputs(category, buying_cost, selling_cost, status):
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

    def validate_inputs(self, category, buying_cost, selling_cost, status):
        valid = True


        if category not in ["Ingredient", "Beverage"]:
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
        self.comboBox_2.setCurrentIndex(-1)
        self.label_2.setText("")
        self.label.setText("")
        self.lineEdit_5.clear()
        self.lineEdit_4.clear()
        self.comboBox.setCurrentIndex(-1)
        self.reset_styles()

    def reset_styles(self):
        self.comboBox_2.setStyleSheet("")
        self.lineEdit_5.setStyleSheet("")
        self.lineEdit_4.setStyleSheet("")
        self.comboBox.setStyleSheet("")