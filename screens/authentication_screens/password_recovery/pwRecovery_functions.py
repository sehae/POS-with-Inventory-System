from screens.authentication_screens.password_recovery.passwordRecovery import Ui_MainWindow
from server.local_server import conn
from validator.password_validator import isValidPassword


class PasswordRecovery(Ui_MainWindow):
    def __init__(self, email):
        super().__init__()
        self.email = email
        self.id, self.source_table = self.check_email_source(email)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.saveBTN.clicked.connect(self.save_password)

    def save_password(self):
        print("save_password method called")
        new_password = self.passwordFIELD.text()
        retype_new_password = self.retypeFIELD.text()

        if new_password == retype_new_password:
            print("Passwords match!")

            # Validate the new password
            if not isValidPassword(new_password):
                return

            cursor = conn.cursor()
            try:
                if self.source_table == 'admin':
                    print("Updating password in adminlogin table")
                    cursor.execute(
                        "UPDATE adminlogin SET password = %s WHERE admin_id = %s",
                        (new_password, self.id)
                    )
                elif self.source_table == 'employee':
                    print("Updating password in employeelogin table")
                    cursor.execute(
                        "UPDATE employeelogin SET password = %s WHERE employee_id = %s",
                        (new_password, self.id)
                    )

                conn.commit()
                print("Password reset successful!")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Passwords do not match!")

    def check_email_source(self, email):
        cursor = conn.cursor()

        # Query the employee table
        cursor.execute(
            "SELECT employee_id FROM employee WHERE email = %s",
            (email,)
        )
        user = cursor.fetchone()

        if user:
            print(f"Email found in employee table with ID {user[0]}")
            return user[0], 'employee'

        # Query the admin table
        cursor.execute(
            "SELECT admin_id FROM admin WHERE email = %s",
            (email,)
        )
        user = cursor.fetchone()

        if user:
            print(f"Email found in admin table with ID {user[0]}")
            return user[0], 'admin'

        print("Email not found")
        return None, None
