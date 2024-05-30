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
        self.rightcontent.hide()
        self.edituserCONTENT.hide()

    def edit_user(self):
        # Get the current user's email
        email = self.emailDISPLAY.text()
        department = self.get_department()
        print(department)

        cursor = conn.cursor()

        # Check if the admin button is active
        if self.adminBTN.styleSheet() == self.active_button_style:
            # The user is an admin, move the user from the employee table to the admin table
            try:
                cursor.execute(
                    "SELECT * FROM admin WHERE email = %s",
                    (email,)
                )
                result = cursor.fetchone()

                if result is None:
                    # The user does not exist in the admin table, insert a new record
                    cursor.execute(
                        "INSERT INTO admin (first_name, last_name, contact_number, email) SELECT first_name, last_name, contact_number, email FROM employee WHERE email = %s AND is_active = True",
                        (email,)
                    )
                else:
                    # The user exists in the admin table, reactivate the user
                    cursor.execute(
                        "UPDATE admin SET is_active = True WHERE email = %s",
                        (email,)
                    )

                # Set the user's status in the employee table to inactive
                cursor.execute(
                    "UPDATE employee SET is_active = False WHERE email = %s",
                    (email,)
                )

                conn.commit()
                print(f"{email} moved to admin table")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif self.staffBTN.styleSheet() == self.active_button_style:
            # The user is a staff, move the user from the admin table to the employee table
            try:
                cursor.execute(
                    "SELECT * FROM employee WHERE email = %s",
                    (email,)
                )
                result = cursor.fetchone()

                if result is None:
                    # The user does not exist in the employee table, insert a new record
                    cursor.execute(
                        "INSERT INTO employee (first_name, last_name, contact_number, email, department) SELECT first_name, last_name, contact_number, email, %s FROM admin WHERE email = %s AND is_active = True",
                        (department, email,)
                    )
                else:
                    # The user exists in the employee table, reactivate the user
                    cursor.execute(
                        "UPDATE employee SET is_active = True WHERE email = %s",
                        (email,)
                    )

                # Set the user's status in the admin table to inactive
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

    def get_department(self):
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

    def deactivate_user(self):
        email = self.emailDISPLAY.text()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE admin SET is_active = False WHERE email = %s",
            (email,)
        )
        self.rightcontent.hide()
        self.edituserCONTENT.hide()
        print(f"{email} deactivated")

    def show_rightcontent(self):
        self.rightcontent.show()
