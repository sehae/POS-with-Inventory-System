from PyQt5.QtCore import QDateTime, QTimer

from database.DB_Queries import SEARCH_USER, FETCH_USER_INFO, CHANGE_USER_TYPE, CHANGE_DEPARTMENT, DISABLE_USER
from maintenance.user_logs import user_log
from shared.imports import *
from screens.admin_screens.admin_maintenance.maintenanceEDIT import Ui_MainWindow
from styles.loginStyles import ERROR_LBL_HIDDEN, ERROR_LBL_VISIBLE
from validator.user_manager import userManager


class adminMaintenanceEDIT(QMainWindow, Ui_MainWindow):
    add_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.active_button_style = ACTIVE_BUTTON_STYLE
        self.inactive_button_style = INACTIVE_BUTTON_STYLE

        self.saveBTN.clicked.connect(self.edit_user)
        self.adduserBTN.clicked.connect(self.add_user)
        self.backBTN.clicked.connect(self.back)
        self.searchFIELD.returnPressed.connect(self.search_user)
        self.staffBTN.clicked.connect(self.activate_staff)
        self.adminBTN.clicked.connect(self.activate_admin)
        self.cashierBTN.clicked.connect(self.activate_cashier)
        self.kitchenBTN.clicked.connect(self.activate_kitchen)
        self.userlogsBTN.clicked.connect(self.show_rightcontent)
        self.deactBTN.clicked.connect(self.deactivate_user)
        self.discardBTN.clicked.connect(self.discard)
        self.rightcontent.hide()
        self.edituserCONTENT.hide()
        self.userRESULTS.hide()
        self.userRESULTS.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
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
        self.dateDISPLAY.setText(formattedDateTime)

    def add_user(self):
        self.add_signal.emit()

    def back(self):
        self.back_signal.emit()

    def edit_user(self):
        email = self.emailDISPLAY.text()
        department = self.get_active_department()

        cursor = conn.cursor()

        # Change the user's role to admin
        if self.adminBTN.styleSheet() == self.active_button_style:
            try:
                cursor.execute(CHANGE_USER_TYPE, ('Admin', email,))
                conn.commit()
                cursor.close()
                print(f"User {email} changed to Admin successfully.")
                self.log_edit(11, f"of user {email} to Admin")
                print(f"Successfully Logged user action.")
            except Exception as e:
                print(f"An error occurred: {e}")

        # Change the user's role to staff
        elif self.staffBTN.styleSheet() == self.active_button_style:
            try:
                cursor.execute(CHANGE_USER_TYPE, ('Employee', email,))
                cursor.execute(CHANGE_DEPARTMENT, (department, email,))
                conn.commit()
                cursor.close()
                print(f"User {email} changed to Staff and {department} successfully.")
                self.log_edit(11, f"of user {email} to Staff and {department}")
                print(f"Successfully Logged user action.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("No role selected")

    def get_active_department(self):
        if self.cashierBTN.styleSheet() == self.active_button_style:
            return 'Cashier'
        elif self.kitchenBTN.styleSheet() == self.active_button_style:
            return 'Kitchen'
        else:
            return None

    # Search Module
    def search_user(self):
        try:
            search_text = self.searchFIELD.text()
            cursor = conn.cursor()

            cursor.execute(SEARCH_USER, ('%'+search_text+'%', '%'+search_text+'%', '%'+search_text+'%'))
            results = cursor.fetchall()

            # If there are no results, update the errorLBL and return
            if not results:
                self.errorLBL.setText("No results found.")
                self.errorLBL.setStyleSheet(ERROR_LBL_VISIBLE)
                return

            # Clear the table before adding new data
            self.userRESULTS.setRowCount(len(results))
            self.userRESULTS.setColumnCount(4)

            row_position = 0

            for result in results:
                # Define the column names
                column_names = ["First Name", "Last Name", "Email", "Department"]

                # Set the column names
                self.userRESULTS.setHorizontalHeaderLabels(column_names)

                # Create a QTableWidgetItem for each field
                first_name_item = QtWidgets.QTableWidgetItem(result[0])
                last_name_item = QtWidgets.QTableWidgetItem(result[1])
                email_item = QtWidgets.QTableWidgetItem(result[2])
                department_item = QtWidgets.QTableWidgetItem(result[3])

                # Make the cells not editable
                first_name_item.setFlags(first_name_item.flags() & ~QtCore.Qt.ItemIsEditable)
                last_name_item.setFlags(last_name_item.flags() & ~QtCore.Qt.ItemIsEditable)
                email_item.setFlags(email_item.flags() & ~QtCore.Qt.ItemIsEditable)
                department_item.setFlags(department_item.flags() & ~QtCore.Qt.ItemIsEditable)

                # Add the items to the table
                self.userRESULTS.setItem(row_position, 0, first_name_item)
                self.userRESULTS.setItem(row_position, 1, last_name_item)
                self.userRESULTS.setItem(row_position, 2, email_item)
                self.userRESULTS.setItem(row_position, 3, department_item)

                row_position += 1
                self.resize_table_to_contents()
                self.userRESULTS.show()
                self.edituserCONTENT.hide()
                self.errorLBL.setStyleSheet(ERROR_LBL_HIDDEN)

                if result[3] == 'Kitchen':
                    self.activate_kitchen()
                elif result[3] == 'Cashier':
                    self.activate_cashier()
                elif result[3] == 'Admin':
                    self.admin_style()

            # Connect the cellClicked signal to a slot function
            self.userRESULTS.cellClicked.connect(self.cell_clicked)

        except Exception as e:
            print(f"An error occurred: {e}")

    def cell_clicked(self, row):
        # Get the data of the whole row
        row_data = [self.userRESULTS.item(row, col).text() for col in range(self.userRESULTS.columnCount())]
        print(f"You clicked on row {row}. The row contains: {row_data}")

        # Show the edituserCONTENT and update the display with the row data
        self.edituserCONTENT.show()
        self.searchFIELD.clear()
        self.userRESULTS.hide()
        self.nameDISPLAY.setText(f"{row_data[0]} {row_data[1]}")
        self.emailDISPLAY.setText(row_data[2])

        # Set the user role based on the department
        self.set_user_role(row_data[3])

    def resize_table_to_contents(self):
        self.userRESULTS.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        height = self.userRESULTS.horizontalHeader().height()  # height of column header

        for i in range(self.userRESULTS.rowCount()):
            height += self.userRESULTS.rowHeight(i)  # add each row's height

        self.userRESULTS.setFixedHeight(height)

    # End of Search Module

    def activate_staff(self):
        self.staffBTN.setStyleSheet(self.active_button_style)
        self.adminBTN.setStyleSheet(self.inactive_button_style)

        self.restrictionBUTTONGRP.setEnabled(True)
        self.cashierBTN.setStyleSheet(self.active_button_style)
        self.kitchenBTN.setStyleSheet(self.inactive_button_style)

    def activate_admin(self):
        returnValue = confirmation_dialog("Are you sure you want to make this user as an admin?")
        if returnValue == QMessageBox.Ok:
            self.adminBTN.setStyleSheet(self.active_button_style)
            self.staffBTN.setStyleSheet(self.inactive_button_style)

            self.restrictionBUTTONGRP.setEnabled(False)
            self.cashierBTN.setStyleSheet(self.inactive_button_style)
            self.kitchenBTN.setStyleSheet(self.inactive_button_style)

    def admin_style(self):
        self.adminBTN.setStyleSheet(self.active_button_style)
        self.staffBTN.setStyleSheet(self.inactive_button_style)

    def activate_cashier(self):
        self.staffBTN.setStyleSheet(self.active_button_style)
        self.adminBTN.setStyleSheet(self.inactive_button_style)

        self.cashierBTN.setStyleSheet(self.active_button_style)
        self.kitchenBTN.setStyleSheet(self.inactive_button_style)

    def activate_kitchen(self):
        self.staffBTN.setStyleSheet(self.active_button_style)
        self.adminBTN.setStyleSheet(self.inactive_button_style)

        self.kitchenBTN.setStyleSheet(self.active_button_style)
        self.cashierBTN.setStyleSheet(self.inactive_button_style)

    def deactivate_user(self):
        returnValue = confirmation_dialog("Are you sure you want to deactivate this user?")
        if returnValue == QMessageBox.Ok:
            email = self.emailDISPLAY.text()
            cursor = conn.cursor()

            cursor.execute(DISABLE_USER, (email,))
            # Commit the changes
            conn.commit()
            cursor.close()
            self.log_edit(13, "{email}")

            # Hide content and clear search field
            self.rightcontent.hide()
            self.edituserCONTENT.hide()
            self.searchFIELD.clear()
            print(f"{email} deactivated")

            create_dialog_box(f"User {email} has been successfully deactivated.", "User Deactivated")

    def set_user_role(self, role):
        # Reset all buttons to inactive style
        self.staffBTN.setStyleSheet(self.inactive_button_style)
        self.adminBTN.setStyleSheet(self.inactive_button_style)
        self.cashierBTN.setStyleSheet(self.inactive_button_style)
        self.kitchenBTN.setStyleSheet(self.inactive_button_style)

        # Disable the restriction button group by default
        self.restrictionBUTTONGRP.setEnabled(False)

        # Set the style and restrictions based on the role
        if role == 'Admin':
            self.adminBTN.setStyleSheet(self.active_button_style)
        elif role == 'Cashier':
            self.restrictionBUTTONGRP.setEnabled(True)
            self.staffBTN.setStyleSheet(self.active_button_style)
            self.cashierBTN.setStyleSheet(self.active_button_style)
        elif role == 'Kitchen':
            self.restrictionBUTTONGRP.setEnabled(True)
            self.staffBTN.setStyleSheet(self.active_button_style)
            self.kitchenBTN.setStyleSheet(self.active_button_style)

    def show_rightcontent(self):
        self.rightcontent.show()

    def discard(self):
        self.rightcontent.hide()
        self.edituserCONTENT.hide()
        self.searchFIELD.clear()

    def log_edit(self, user_action, specific_action):
        user_manager = userManager._instance
        current_id = user_manager.get_current_user_id()
        current_username = user_manager.get_current_username()
        user_log(current_id, user_action, current_username, specific_action)