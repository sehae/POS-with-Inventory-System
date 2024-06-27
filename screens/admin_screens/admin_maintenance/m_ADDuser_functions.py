import datetime
import os

from PyQt5.QtCore import QDateTime, QTimer

from database.DB_Queries import GET_NEXT_ID, ADD_USER
from modules.maintenance.user_logs import user_log
from screens.admin_screens.admin_maintenance.maintenanceADDuser import Ui_MainWindow
from shared.imports import *
from styles.universalStyles import COMBOBOX_STYLE, COMBOBOX_STYLE_VIEW, COMBOBOX_DISABLED_STYLE, INVALID_FIELD_STYLE, \
    VALID_FIELD_STYLE
from validator.email_validator import validate_email
from validator.internet_connection import is_connected
from validator.user_manager import userManager


class adminMaintenance(QMainWindow, Ui_MainWindow):  # Inherit from QMainWindow
    back_signal = QtCore.pyqtSignal()
    edit_signal = QtCore.pyqtSignal()
    backup_recovery_signal = QtCore.pyqtSignal()

    def __init__(self):
        try:
            super().__init__()
            self.setupUi(self)  # Call the setupUi method to initialize the UI

            self.saveBTN.clicked.connect(self.add_user)
            self.cancelBTN.clicked.connect(self.clearField)
            self.loaBOX.currentTextChanged.connect(self.check_admin)

            # Navigation signals
            self.editUserButton.clicked.connect(self.navigate_edit)
            self.backButton.clicked.connect(self.back_signal.emit)
            self.backupBTN.clicked.connect(self.backup_recovery_signal.emit)

            self.UIComponents()

            # Create a QTimer object
            self.timer = QTimer()

            # Connect the timeout signal of the timer to the updateDateTime slot
            self.timer.timeout.connect(self.updateDateTime)

            # Set the interval for the timer (in milliseconds)
            self.timer.start(1000)  # Update every second
        except Exception as e:
            print("Error in adminMaintenance: ", e)

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
        self.firstName.setValidator(QRegExpValidator(QRegExp(r'^[a-zA-Z\s]*$')))
        self.lastName.setValidator(QRegExpValidator(QRegExp(r'^[a-zA-Z\s]*$')))

    def check_admin(self):
        if self.loaBOX.currentText() == 'Admin':
            self.deptBox.setEnabled(False)
            self.deptBox.setStyleSheet(COMBOBOX_DISABLED_STYLE)
        else:
            self.deptBox.setEnabled(True)
            self.deptBox.setStyleSheet(COMBOBOX_STYLE)

    def add_user(self):
        first_name = self.firstName.text().strip()
        last_name = self.lastName.text().strip()
        email = self.email.text().strip()
        contact_number = self.contactNum.text().strip()
        LoA = self.loaBOX.currentText()
        dept = self.deptBox.currentText()

        all_fields_valid = True

        # Validate first name
        if first_name == "" or not all(char.isalpha() or char.isspace() for char in first_name):
            self.firstName.setStyleSheet(INVALID_FIELD_STYLE)
            all_fields_valid = False
        else:
            self.firstName.setStyleSheet(VALID_FIELD_STYLE)

        # Validate last name
        if last_name == "" or not last_name.isalpha():
            self.lastName.setStyleSheet(INVALID_FIELD_STYLE)
            all_fields_valid = False
        else:
            self.lastName.setStyleSheet(VALID_FIELD_STYLE)

        # Validate email
        if email == "" or not validate_email(email):
            self.email.setStyleSheet(INVALID_FIELD_STYLE)
            all_fields_valid = False
        else:
            self.email.setStyleSheet(VALID_FIELD_STYLE)

        # Validate contact number
        if contact_number == "" or not contact_number.isdigit() or len(contact_number) < 11:
            self.contactNum.setStyleSheet(INVALID_FIELD_STYLE)
            all_fields_valid = False
        else:
            self.contactNum.setStyleSheet(VALID_FIELD_STYLE)

        # Function to check if required fields are filled
        def are_fields_filled(fields):
            return all(fields)

        # Required fields
        required_fields = [first_name, last_name, LoA, dept, contact_number, email]

        # Check if all required fields are filled and valid
        if not are_fields_filled(required_fields) or not all_fields_valid:
            return

        cursor = conn.cursor()

        # Generate password
        password = self.generate_password()

        # Hash the password
        hashed_password = hash_password(password)

        # Generate username
        username = self.generate_username(first_name, last_name, LoA, dept)

        # Generate user ID
        user_id = self.generate_userid()

        # Add username and password to the respective login table
        if LoA == 'Admin':
            add_query = ADD_USER
            print("Adding user...")
            user_data = (user_id, last_name, first_name, LoA, 'Admin', contact_number, email, username, hashed_password)
        else:
            add_query = ADD_USER
            print("Adding user...")
            user_data = (user_id, last_name, first_name, LoA, dept, contact_number, email, username, hashed_password)

        cursor.execute(add_query, user_data)
        conn.commit()

        print("User added successfully")

        # User Log
        user_action = 10
        specific_action = username
        self.log_add(user_action, specific_action)

        # Send username and password
        if is_connected():
            try:
                print("Sending username and password...")
                send_username_password(username, password, email)
            except Exception as e:
                print("Error sending username and password: ", e)
        else:
            show_username_password(username, password)

        print("Username and password sent successfully")

        cursor.close()

        create_dialog_box("User added successfully.", "Success")
        self.clearField()

    def generate_password(self):
        length = 8
        all_chars = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(random.choice(all_chars) for _ in range(length))
            if (any(c.isupper() for c in password) and
                    any(c.isdigit() for c in password) and
                    any(c in string.punctuation for c in password)):
                return password

    def generate_username(self, first_name, last_name, LoA, dept):
        if LoA == 'Admin':
            dept_number = '01'
        else:
            dept_number = '02'

        # Get the last user ID from the database
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM user ORDER BY user_id DESC LIMIT 1")
        result = cursor.fetchone()

        # If the database is not empty, extract the counter from the last user ID
        if result is not None:
            last_user_id = result[0]
            counter = int(last_user_id[-2:])
        else:
            counter = 0

        # Increment the counter
        counter += 1

        # Generate username
        initials = first_name[0] + last_name[0]
        staff_number = str(counter).zfill(2)
        username = initials.upper() + dept_number + staff_number
        return username

    def generate_userid(self):
        current_year = str(datetime.datetime.now().year)[-2:]  # Only take the last two digits of the year

        # Get the last user ID from the database
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM user ORDER BY user_id DESC LIMIT 1")
        result = cursor.fetchone()

        # If the database is not empty, extract the counter and the year from the last user ID
        if result is not None:
            last_user_id = result[0]
            last_year = last_user_id[2:4]  # Only take the last two digits of the year
            counter = int(last_user_id[-2:])
            # If the year has changed, reset the counter to 1
            if last_year != current_year:
                counter = 1
            else:
                # Increment the counter
                counter += 1
        else:
            counter = 1

        counter_str = str(counter).zfill(2)
        user_id = "MH" + current_year + counter_str

        return user_id

    def clearField(self):
        self.firstName.clear()
        self.lastName.clear()
        self.email.clear()
        self.contactNum.clear()
        self.loaBOX.setCurrentIndex(0)
        self.deptBox.setCurrentIndex(0)
        self.firstName.setStyleSheet(VALID_FIELD_STYLE)
        self.lastName.setStyleSheet(VALID_FIELD_STYLE)
        self.email.setStyleSheet(VALID_FIELD_STYLE)
        self.contactNum.setStyleSheet(VALID_FIELD_STYLE)

    def log_add(self, user_action, specific_action):
        user_manager = userManager._instance
        current_id = user_manager.get_current_user_id()
        current_username = user_manager.get_current_username()
        user_log(current_id, user_action, current_username, specific_action)
