from shared.imports import *
from screens.admin_screens.admin_maintenance.maintenanceADDuser import Ui_MainWindow

class adminMaintenance(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.saveBTN.clicked.connect(self.add_user)
        self.loaBOX.currentTextChanged.connect(self.check_admin)

        self.UIComponents()

    def UIComponents(self):
        self.loaBOX.setStyleSheet(COMBOBOX_STYLE)
        self.loaBOX.view().setStyleSheet(COMBOBOX_STYLE_VIEW)
        self.deptBox.setStyleSheet(COMBOBOX_STYLE)
        self.deptBox.view().setStyleSheet(COMBOBOX_STYLE_VIEW)
        self.contactNum.setValidator(QRegExpValidator(QRegExp(r'^09\d{9}$')))

    def check_admin(self):
        if self.loaBOX.currentText() == 'Admin':
            self.deptBox.setEnabled(False)
            self.deptBox.setStyleSheet(COMBOBOX_DISABLED_STYLE)
        else:
            self.deptBox.setEnabled(True)
            self.deptBox.setStyleSheet(COMBOBOX_STYLE)

    def add_user(self):
        print("add_user method called")
        first_name = self.firstName.text()
        last_name = self.lastName.text()
        email = self.email.text()
        contact_number = self.contactNum.text().strip()
        LoA = self.loaBOX.currentText()
        dept = self.deptBox.currentText()

        # Error handling
        if not first_name or not last_name or not email or not contact_number or not LoA or (
                not dept and LoA != 'Admin'):
            show_error_message("Error","All fields must be filled. Please fill in the fields before adding a user.")
            return

        try:
            cursor = conn.cursor()
            print("Cursor created")

            if LoA == 'Admin':
                add_user_query = ADD_ADMIN
                user_data = (last_name, first_name, contact_number, email)
                dept_number = '01'
            else:
                add_user_query = ADD_EMPLOYEE
                user_data = (last_name, first_name, dept, contact_number, email)
                dept_number = '02'

            cursor.execute(add_user_query, user_data)
            conn.commit()
            print("User added successfully.")

            # Get the last inserted id
            user_id = cursor.lastrowid

            # Generate username
            initials = first_name[0] + last_name[0]
            staff_number = str(user_id).zfill(2)
            username = initials.upper() + dept_number + staff_number

            # Generate password
            password = self.generate_password()

            # Hash the password
            hashed_password = hash_password(password)

            # Add username and password to the respective login table
            if LoA == 'Admin':
                add_login_query = ADD_ADMIN_LOGIN
            else:
                add_login_query = ADD_EMPLOYEE_LOGIN

            login_data = (user_id, username, hashed_password)
            cursor.execute(add_login_query, login_data)
            conn.commit()
            print("Login details added successfully.")

            try:
                if is_connected():
                    send_username_password(username, password, email)
                else:
                    show_username_password(username, password)
            except Exception as e:
                print("Error sending username and password: ", e)

        except Exception as e:
            show_error_message("Database Error", f"An error occurred while adding the user: {e}")
        finally:
            cursor.close()

    def generate_password(self):
        length = 8
        all_chars = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(random.choice(all_chars) for _ in range(length))
            if (any(c.isupper() for c in password) and
                    any(c.isdigit() for c in password) and
                    any(c in string.punctuation for c in password)):
                return password
