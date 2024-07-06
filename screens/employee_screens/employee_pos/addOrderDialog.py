# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addOrderDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class AddOrderDialog(object):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_6.clicked.connect(self.saveOrder)
        self.pushButton_7.clicked.connect(self.discard)

        # Connect the selection change signal of the table widget
        self.tableWidget.itemSelectionChanged.connect(self.on_table_selection_changed)

        # Populate comboBox_2 with package names
        self.populate_comboBox_2()

        # Populate comboBox_2 with soup names
        self.populate_comboBox_3()

        self.comboBox_2.setCurrentIndex(-1)
        self.comboBox_3.setCurrentIndex(-1)

        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.addButton(self.radioButton, 0)
        self.buttonGroup.addButton(self.radioButton_2, 1)

        self.buttonGroup1 = QButtonGroup(self)
        self.buttonGroup1.addButton(self.radioButton_3, 2)
        self.buttonGroup1.addButton(self.radioButton_4, 3)

        self.radioButton.setChecked(True)
        self.radioButton_3.setChecked(True)

        self.int_validator = QIntValidator()
        self.lineEdit_7.setValidator(self.int_validator)

        # Initialize QRegExpValidator for letter-only input
        regex = QRegularExpression("[a-zA-Z]+")  # Regular expression for letters only
        self.letter_validator = QRegularExpressionValidator(regex)
        self.lineEdit_9.setValidator(self.letter_validator)

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(620, 516)
        self.widget_4 = QtWidgets.QWidget(self)
        self.widget_4.setGeometry(QtCore.QRect(30, 0, 594, 501))
        self.widget_4.setObjectName("widget_4")
        self.label_15 = QtWidgets.QLabel(self.widget_4)
        self.label_15.setGeometry(QtCore.QRect(0, 439, 16, 16))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setGeometry(QtCore.QRect(140, 439, 447, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_6.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
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
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_7.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
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
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.layoutWidget = QtWidgets.QWidget(self.widget_4)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 536, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.label_14 = QtWidgets.QLabel(self.widget_4)
        self.label_14.setGeometry(QtCore.QRect(10, 110, 55, 16))
        self.label_14.setObjectName("label_14")
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setGeometry(QtCore.QRect(10, 160, 76, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(140, 150, 400, 35))
        self.lineEdit_9.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_9.setStyleSheet("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_20 = QtWidgets.QLabel(self.widget_4)
        self.label_20.setGeometry(QtCore.QRect(10, 260, 67, 16))
        self.label_20.setObjectName("label_20")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 250, 400, 35))
        self.comboBox_2.setMinimumSize(QtCore.QSize(400, 35))
        self.comboBox_2.setMaximumSize(QtCore.QSize(400, 35))
        self.comboBox_2.setStyleSheet("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(140, 200, 400, 35))
        self.lineEdit_7.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_7.setStyleSheet("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_19 = QtWidgets.QLabel(self.widget_4)
        self.label_19.setGeometry(QtCore.QRect(10, 210, 49, 16))
        self.label_19.setObjectName("label_19")
        self.label_18 = QtWidgets.QLabel(self.widget_4)
        self.label_18.setGeometry(QtCore.QRect(10, 360, 34, 16))
        self.label_18.setObjectName("label_18")
        self.label_17 = QtWidgets.QLabel(self.widget_4)
        self.label_17.setGeometry(QtCore.QRect(10, 310, 69, 16))
        self.label_17.setObjectName("label_17")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_3.setGeometry(QtCore.QRect(140, 300, 400, 35))
        self.comboBox_3.setMinimumSize(QtCore.QSize(400, 35))
        self.comboBox_3.setMaximumSize(QtCore.QSize(400, 35))
        self.comboBox_3.setStyleSheet("")
        self.comboBox_3.setObjectName("comboBox_3")
        self.layoutWidget_2 = QtWidgets.QWidget(self.widget_4)
        self.layoutWidget_2.setGeometry(QtCore.QRect(140, 110, 172, 19))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_5.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_5.addWidget(self.radioButton_2)
        self.layoutWidget_3 = QtWidgets.QWidget(self.widget_4)
        self.layoutWidget_3.setGeometry(QtCore.QRect(140, 360, 181, 19))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_6.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_6.addWidget(self.radioButton_4)

        self.retranslateUi()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_6.setText(_translate("Dialog", "Generate Order"))
        self.pushButton_7.setText(_translate("Dialog", "Discard"))
        self.label_5.setText(_translate("Dialog", "Order Details"))
        self.label_14.setText(_translate("Dialog", "Order Type"))
        self.label_10.setText(_translate("Dialog", "Customer Name"))
        self.label_20.setText(_translate("Dialog", "Package Type"))
        self.label_19.setText(_translate("Dialog", "Guest Pax"))
        self.label_18.setText(_translate("Dialog", "Priority"))
        self.label_17.setText(_translate("Dialog", "Soup Variation"))
        self.radioButton.setText(_translate("Dialog", "Package"))
        self.radioButton_2.setText(_translate("Dialog", "Add-ons only"))
        self.radioButton_3.setText(_translate("Dialog", "Priority"))
        self.radioButton_4.setText(_translate("Dialog", "Non-Priority"))

    def discard(self):
        self.lineEdit_9.clear()
        self.lineEdit_7.clear()
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)

    def populate_comboBox_2(self):
        try:
            # Clear existing items
            self.comboBox_2.clear()

            # Add blank/null option
            self.comboBox_2.addItem("None")  # Add a blank item

            # Add specific values
            self.comboBox_2.addItems(["Hotpot", "Grill", "Hotpot and Grill"])

        except Exception as e:
            print(f"Error occurred while populating comboBox_2: {e}")

    def populate_comboBox_3(self):
        try:
            # Clear existing items
            self.comboBox_3.clear()

            # Add blank/null option
            self.comboBox_3.addItem("None")  # Add a blank item

            # Add specific values
            self.comboBox_3.addItems(["Mala soup", "Plain soup", "Suan la soup", "Tomato soup"])

        except Exception as e:
            print(f"Error occurred while populating comboBox_3: {e}")

    def saveOrder(self):
        # Get input values
        customer_name = self.lineEdit_9.text().strip()
        order_type = self.buttonGroup.checkedButton().text()
        priority_order = self.buttonGroup1.checkedButton().text()
        package_name = self.comboBox_2.currentText()
        guest_capacity = self.lineEdit_7.text().strip()
        soup_variation = self.comboBox_3.currentText()

        if soup_variation == '':
            soup_variation = None

        if order_type == "Package":
            payment_status = "Waiting for Receipt"

            if not self.validate_package_inputs(customer_name, package_name, guest_capacity, soup_variation):
                return

        elif order_type == "Add-ons only":
            payment_status = "Pending"
            guest_capacity = None

            if not self.validate_addon_inputs(customer_name, package_name, guest_capacity, soup_variation):
                return

        try:
            if conn.is_connected():
                cursor = conn.cursor()

                # Get current date in yyyy-MM-dd format
                current_date = QDateTime.currentDateTime().toString("yyyy-MM-dd")

                # Fetch the latest Order_ID for the current date
                cursor.execute(f"SELECT MAX(Order_ID) FROM `order` WHERE Date = '{current_date}'")
                latest_order_id = cursor.fetchone()[0]

                if latest_order_id:
                    # Extract numeric part and increment
                    numeric_part = latest_order_id[11:]  # Assuming Order_ID format is POSyyyyMMddNNN
                    order_number = int(numeric_part)
                    new_order_number = order_number + 1
                    next_order_number = f"{new_order_number:03d}"
                else:
                    # If no previous orders for the day, start from 001
                    next_order_number = "001"

                # Construct new Order_ID
                new_order_id = f"POS{current_date.replace('-', '')}{next_order_number}"

                # Construct the insert query with proper handling of NULL for Guest_Pax
                insert_query = f"""
                                 INSERT INTO `order` (Order_ID, Date, Time, Package_ID, Payment_Status, 
                                                      Guest_Pax, Customer_Name, Soup_Variation, Order_Type, Payment_Method, Priority_Order)
                                 VALUES (%s, %s, TIME_FORMAT(NOW(), '%H:%i'), 
                                         (SELECT Package_ID FROM package WHERE Package_Name = %s), 
                                         %s, %s, %s, %s, %s, %s, %s)
                             """
                cursor.execute(insert_query, (
                    new_order_id, current_date, package_name, payment_status, guest_capacity, customer_name,
                    soup_variation, order_type, 'Pending', priority_order))
                conn.commit()

                QMessageBox.information(self, "Success", "Order saved successfully.")

                self.update_combobox_signal.emit()

                # Clear input fields after successful save
                self.lineEdit_9.clear()
                self.lineEdit_7.clear()
                self.comboBox_7.clear()
                self.comboBox_2.setCurrentIndex(-1)
                self.comboBox_3.setCurrentIndex(-1)

                self.populate_table()
                self.reset_styles()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred while saving order: {str(e)}")

        finally:
            if conn.is_connected():
                cursor.close()

    def reset_styles(self):
        self.lineEdit_9.setStyleSheet("")
        self.comboBox_2.setStyleSheet("")
        self.lineEdit_7.setStyleSheet("")
        self.comboBox_3.setStyleSheet("")

    def validate_package_inputs(self, customer_name, package_name, guest_capacity, soup_variation):
        valid = True

        if not customer_name:
            self.lineEdit_9.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_9.setStyleSheet("border: 1px solid green;")

        if not package_name or package_name == "None":
            self.comboBox_2.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_2.setStyleSheet("border: 1px solid green;")

        if not guest_capacity:
            self.lineEdit_7.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_7.setStyleSheet("border: 1px solid green;")

        if not soup_variation or (soup_variation == 'None' and package_name != "Grill"):
            self.comboBox_3.setStyleSheet("border: 1px solid red;")
            valid = False
        elif package_name == "Grill" and soup_variation != "None":
            self.comboBox_3.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_3.setStyleSheet("border: 1px solid green;")

        if not valid:
            QMessageBox.warning(self, "Warning", "Please fill in all fields correctly for Package type order.")

        return valid

    def validate_addon_inputs(self, customer_name, package_name, guest_capacity, soup_variation):
        valid = True

        if not customer_name:
            self.lineEdit_9.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_9.setStyleSheet("border: 1px solid green;")

        if package_name != "None":
            self.comboBox_2.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_2.setStyleSheet("border: 1px solid green;")

        if guest_capacity:
            self.lineEdit_7.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.lineEdit_7.setStyleSheet("border: 1px solid green;")

        if soup_variation != "None":
            self.comboBox_3.setStyleSheet("border: 1px solid red;")
            valid = False
        else:
            self.comboBox_3.setStyleSheet("border: 1px solid green;")

        if not valid:
            QMessageBox.warning(self, "Warning",
                                "Provide customer name and empty the other fields for Add-ons only order.")

        return valid