import random
import string

from PyQt5 import QtCore
from PyQt5.QtCore import QRegExp, QDateTime, QTimer, Qt
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow  # Import QMainWindow

from automated.email_automation import send_username_password
from screens.admin_screens.admin_maintenance.maintenanceADDuser import Ui_MainWindow
from shared.dialog import show_username_password, show_error_message

from server.local_server import conn
from validator.internet_connection import is_connected
from styles.universalStyles import COMBOBOX_STYLE, COMBOBOX_STYLE_VIEW, COMBOBOX_DISABLED_STYLE


class adminMaintenance(QMainWindow, Ui_MainWindow):  # Inherit from QMainWindow
    back_signal = QtCore.pyqtSignal()
    edit_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Call the setupUi method to initialize the UI

        self.saveBTN.clicked.connect(self.add_user)
        self.loaBOX.currentTextChanged.connect(self.check_admin)
        self.editUserButton.clicked.connect(self.navigate_edit)
        self.backButton.clicked.connect(self.back)
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

    def back(self):
        self.back_signal.emit()

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
            show_error_message("All fields must be filled. Please fill in the fields before adding a user.")
            return

        cursor = conn.cursor()
        print("Cursor created")

        if LoA == 'Admin':
            add_user_query = "INSERT INTO admin (last_name, first_name, contact_number, email) VALUES (%s, %s, %s, %s)"
            user_data = (last_name, first_name, contact_number, email)
            dept_number = '01'

        else:
            add_user_query = "INSERT INTO employee (last_name, first_name, department, contact_number, email) VALUES (%s, %s, %s, %s, %s)"
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

        # Add username and password to the respective login table
        if LoA == 'Admin':
            add_login_query = "INSERT INTO adminlogin (admin_id, username, password) VALUES (%s, %s, %s)"
        else:
            add_login_query = "INSERT INTO employeelogin (employee_id, username, password) VALUES (%s, %s, %s)"

        login_data = (user_id, username, password)
        cursor.execute(add_login_query, login_data)
        conn.commit()
        print("Login details added successfully.")
        try:
            if is_connected():
                send_username_password(username, password, email)
            else:
                show_username_password(username, password)
        except Exception as e:
            print(e)

    def generate_password(self):
        length = 8
        all_chars = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(random.choice(all_chars) for _ in range(length))
            if (any(c.isupper() for c in password) and
                    any(c.isdigit() for c in password) and
                    any(c in string.punctuation for c in password)):
                return password