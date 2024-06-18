from PyQt5.QtCore import QDateTime, QTimer

from database.DB_Queries import GET_NEXT_ADMIN_ID, GET_NEXT_EMPLOYEE_ID, GET_NEXT_ID, ADD_USER, LOG_ACTIVITY
from maintenance.user_logs import user_log
from shared.imports import *
from PyQt5.QtWidgets import QMainWindow  # Import QMainWindow
from automated.email_automation import send_username_password
from screens.admin_screens.admin_maintenance.maintenanceADDuser import Ui_MainWindow
from shared.dialog import show_username_password, show_error_message

from server.local_server import conn
from shared.navigation_signal import back
from validator.internet_connection import is_connected
from styles.universalStyles import COMBOBOX_STYLE, COMBOBOX_STYLE_VIEW, COMBOBOX_DISABLED_STYLE
from validator.user_manager import userManager


class adminMaintenance(QMainWindow, Ui_MainWindow):  # Inherit from QMainWindow
    back_signal = QtCore.pyqtSignal()
    edit_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Call the setupUi method to initialize the UI

        self.saveBTN.clicked.connect(self.add_user)
        self.loaBOX.currentTextChanged.connect(self.check_admin)
        self.editUserButton.clicked.connect(self.navigate_edit)
        self.backButton.clicked.connect(lambda: back(self.back_signal))
        self.UIComponents()

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
        self.sysTimeDate.setText(formattedDateTime)

    def navigate_edit(self):
        self.edit_signal.emit()

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

            if LoA == 'Admin':
                dept_number = '01'
            else:
                dept_number = '02'

            # Generate password
            password = self.generate_password()

            # Hash the password
            hashed_password = hash_password(password)

            # Get the next ID
            cursor.execute(GET_NEXT_ID)
            result = cursor.fetchone()
            max_id = 0 if result[0] is None else result[0]
            next_id = max_id + 1

            # Generate username
            initials = first_name[0] + last_name[0]
            staff_number = str(next_id).zfill(2)
            username = initials.upper() + dept_number + staff_number

            # Add username and password to the respective login table
            if LoA == 'Admin':
                add_query = ADD_USER
                print("Adding user...")
                user_data = (last_name, first_name, LoA, 'Admin', contact_number, email, username, hashed_password)
            else:
                add_query = ADD_USER
                print("Adding user...")
                user_data = (last_name, first_name, LoA, dept, contact_number, email, username, hashed_password)

            cursor.execute(add_query, user_data)
            conn.commit()

            print("User added successfully")

            # User Log
            user_action = 10
            specific_action = username
            self.log_add(user_action, specific_action)

            # Send username and password
            try:
                if is_connected():
                    print("Sending username and password...")
                    send_username_password(username, password, email)
                else:
                    show_username_password(username, password)
            except Exception as e:
                print("Error sending username and password: ", e)

            print("Username and password sent successfully")
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

    def log_add(self, user_action, specific_action):
        user_manager = userManager._instance
        current_id = user_manager.get_current_user_id()
        current_username = user_manager.get_current_username()
        user_log(current_id, user_action, current_username, specific_action)