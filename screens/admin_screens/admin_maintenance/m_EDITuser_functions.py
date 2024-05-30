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
        self.rightcontent.hide()
        self.edituserCONTENT.hide()

    def edit_user(self):
        # Get the current user's email
        email = self.emailDISPLAY.text()

        cursor = conn.cursor()

        # Check if the staff button is active
        if self.staffBTN.styleSheet() == self.active_button_style:
            # The user is a staff, no need to move the user
            print(f"{email} is a staff")
        elif self.adminBTN.styleSheet() == self.active_button_style:
            # The user is an admin, move the user from the employee table to the admin table
            try:
                # Insert the user into the admin table
                cursor.execute(
                    "INSERT INTO admin (first_name, last_name, email) SELECT first_name, last_name, email FROM employee WHERE email = %s",
                    (email,)
                )

                # Delete the user from the employee table
                cursor.execute(
                    "DELETE FROM employee WHERE email = %s",
                    (email,)
                )

                conn.commit()
                print(f"{email} moved to admin table")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("No role selected")

    def search_user(self):
        try:
            search_text = self.searchFIELD.text()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT first_name, last_name, email FROM employee WHERE last_name LIKE %s OR first_name LIKE %s OR email LIKE %s",
                (search_text, search_text, search_text)
            )
            results = cursor.fetchall()

            if results:
                for result in results:
                    self.edituserCONTENT.show()
                    self.nameDISPLAY.setText(f"{result[0]} {result[1]}")
                    self.emailDISPLAY.setText(result[2])
                    self.activate_staff()
                return

            cursor.execute(
                "SELECT first_name, last_name, email FROM admin WHERE last_name LIKE %s OR first_name LIKE %s OR email LIKE %s",
                (search_text, search_text, search_text)
            )
            results = cursor.fetchall()

            if results:
                for result in results:
                    self.edituserCONTENT.show()
                    self.nameDISPLAY.setText(f"{result[0]} {result[1]}")
                    self.emailDISPLAY.setText(result[2])
                    self.activate_admin()
        except Exception as e:
            print(f"An error occurred: {e}")

    def activate_staff(self):
        self.staffBTN.setStyleSheet(self.active_button_style)
        self.adminBTN.setStyleSheet(self.inactive_button_style)

        self.restrictionBUTTONGRP.setEnabled(True)
        self.cashierBTN.setStyleSheet(self.active_button_style)
        self.kitchenBTN.setStyleSheet(self.inactive_button_style)

    def activate_admin(self):
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

    def show_rightcontent(self):
        self.rightcontent.show()
