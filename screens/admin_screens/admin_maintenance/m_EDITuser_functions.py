from PyQt5.QtWidgets import QMessageBox

from screens.admin_screens.admin_maintenance.maintenanceEDIT import Ui_MainWindow
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from setup.connector import conn


class adminMaintenanceEDIT(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.active_button_style = ACTIVE_BUTTON_STYLE
        self.inactive_button_style = INACTIVE_BUTTON_STYLE

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.saveBTN.clicked.connect(self.edit_user)
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

    def edit_user(self):
        email = self.emailDISPLAY.text()
        department = self.get_active_department()

        cursor = conn.cursor()

        # Check if the user is an admin
        if self.adminBTN.styleSheet() == self.active_button_style:
            try:
                cursor.execute(
                    "SELECT * FROM admin WHERE email = %s",
                    (email,)
                )
                result = cursor.fetchone()

                if result is None:
                    # If user doesn't have data in the admin table
                    cursor.execute(
                        "INSERT INTO admin (first_name, last_name, contact_number, email) SELECT first_name, last_name, contact_number, email FROM employee WHERE email = %s AND is_active = True",
                        (email,)
                    )
                else:
                    cursor.execute(
                        "UPDATE admin SET is_active = True WHERE email = %s",
                        (email,)
                    )

                cursor.execute(
                    "UPDATE employee SET is_active = False WHERE email = %s",
                    (email,)
                )

                conn.commit()
                print(f"{email} moved to admin table")
            except Exception as e:
                print(f"An error occurred: {e}")

        # Check if the user is a staff
        elif self.staffBTN.styleSheet() == self.active_button_style:
            try:
                cursor.execute(
                    "SELECT * FROM employee WHERE email = %s",
                    (email,)
                )
                result = cursor.fetchone()

                if result is None:
                    cursor.execute(
                        "INSERT INTO employee (first_name, last_name, contact_number, email, department) SELECT first_name, last_name, contact_number, email, %s FROM admin WHERE email = %s AND is_active = True",
                        (department, email,)
                    )
                else:
                    cursor.execute(
                        "UPDATE employee SET is_active = True, department = %s WHERE email = %s",
                        (department, email,)
                    )

                cursor.execute(
                    "UPDATE admin SET is_active = False WHERE email = %s",
                    (email,)
                )

                conn.commit()
                print(f"{email} moved to employee table")
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

    def search_user(self):
        try:
            search_text = self.searchFIELD.text()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT first_name, last_name, email, department FROM employee WHERE (last_name LIKE %s OR first_name LIKE %s OR email LIKE %s) AND is_active = True",
                (search_text, search_text, search_text)
            )
            results = cursor.fetchall()

            if results:
                for result in results:
                    self.edituserCONTENT.show()
                    self.nameDISPLAY.setText(f"{result[0]} {result[1]}")
                    self.emailDISPLAY.setText(result[2])
                    self.activate_staff()
                    if result[3] == 'Kitchen':
                        self.activate_kitchen()
                    elif result[3] == 'Cashier':
                        self.activate_cashier()
                return

            cursor.execute(
                "SELECT first_name, last_name, email FROM admin WHERE (last_name LIKE %s OR first_name LIKE %s OR email LIKE %s) AND is_active = True",
                (search_text, search_text, search_text)
            )
            results = cursor.fetchall()

            if results:
                for result in results:
                    self.edituserCONTENT.show()
                    self.nameDISPLAY.setText(f"{result[0]} {result[1]}")
                    self.emailDISPLAY.setText(result[2])
                    self.activate_admin()
            else:
                self.create_dialog_box("No user found with the provided details.", "User Not Found")
        except Exception as e:
            print(f"An error occurred: {e}")

    def activate_staff(self):
        self.staffBTN.setStyleSheet(self.active_button_style)
        self.adminBTN.setStyleSheet(self.inactive_button_style)

        self.restrictionBUTTONGRP.setEnabled(True)
        self.cashierBTN.setStyleSheet(self.active_button_style)
        self.kitchenBTN.setStyleSheet(self.inactive_button_style)

    def activate_admin(self):
        returnValue = self.confirmation_dialog("Are you sure you want to make this user as an admin?")
        if returnValue == QMessageBox.Ok:
            self.adminBTN.setStyleSheet(self.active_button_style)
            self.staffBTN.setStyleSheet(self.inactive_button_style)

            self.restrictionBUTTONGRP.setEnabled(False)
            self.cashierBTN.setStyleSheet(self.inactive_button_style)
            self.kitchenBTN.setStyleSheet(self.inactive_button_style)

    def activate_cashier(self):
        self.cashierBTN.setStyleSheet(self.active_button_style)
        self.kitchenBTN.setStyleSheet(self.inactive_button_style)

    def activate_kitchen(self):
        self.kitchenBTN.setStyleSheet(self.active_button_style)
        self.cashierBTN.setStyleSheet(self.inactive_button_style)

    def deactivate_user(self):
        returnValue = self.confirmation_dialog("Are you sure you want to deactivate this user?")
        if returnValue == QMessageBox.Ok:
            email = self.emailDISPLAY.text()
            cursor = conn.cursor()

            try:
                # Deactivate user in the admin table
                cursor.execute(
                    "UPDATE admin SET is_active = False WHERE email = %s",
                    (email,)
                )
                # Commit the changes
                conn.commit()
                print(f"{email} deactivated in admin table")
            except Exception as e:
                print(f"Error deactivating user in admin table: {e}")

            try:
                # Deactivate user in the employee table
                cursor.execute(
                    "UPDATE employee SET is_active = False WHERE email = %s",
                    (email,)
                )
                # Commit the changes
                conn.commit()
                print(f"{email} deactivated in employee table")
            except Exception as e:
                print(f"Error deactivating user in employee table: {e}")

            # Hide content and clear search field
            self.rightcontent.hide()
            self.edituserCONTENT.hide()
            self.searchFIELD.clear()
            print(f"{email} deactivated")

            self.create_dialog_box(f"User {email} has been successfully deactivated.", "User Deactivated")


    def show_rightcontent(self):
        self.rightcontent.show()

    def confirmation_dialog(self, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(message)
        msgBox.setWindowTitle("Confirmation")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        return msgBox.exec()

    def create_dialog_box(self, message, title):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(message)
        msgBox.setWindowTitle(title)

        return msgBox.exec()

    def discard(self):
        self.rightcontent.hide()
        self.edituserCONTENT.hide()
        self.searchFIELD.clear()