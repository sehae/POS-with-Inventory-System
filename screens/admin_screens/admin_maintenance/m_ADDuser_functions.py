import random
import string

import mysql
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

from screens.admin_screens.admin_maintenance.maintenanceADDuser import Ui_MainWindow

from setup.connector import conn


class adminMaintenance(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.saveBTN.clicked.connect(self.add_user)
        self.loaBOX.currentTextChanged.connect(self.check_admin)

    def check_admin(self):
        if self.loaBOX.currentText() == 'Admin':
            self.deptBox.setEnabled(False)
        else:
            self.deptBox.setEnabled(True)

    def add_user(self):
        print("add_user method called")
        first_name = self.firstName.text()
        last_name = self.lastName.text()
        email = self.email.text()
        contact_number = self.contactNum.text()
        LoA = self.loaBOX.currentText()
        dept = self.deptBox.currentText()

        cursor = conn.cursor()
        print("Cursor created")

        if LoA == 'Admin':
            add_user_query = "INSERT INTO admin (last_name, first_name, contact_number, email) VALUES (%s, %s, %s, %s)"
            user_data = (last_name, first_name, contact_number, email)

        else:
            add_user_query = "INSERT INTO employee (last_name, first_name, department, contact_number, email) VALUES (%s, %s, %s, %s, %s)"
            user_data = (last_name, first_name, dept, contact_number, email)

        cursor.execute(add_user_query, user_data)
        conn.commit()
        print("User added successfully.")

        # Get the last inserted id
        user_id = cursor.lastrowid

        # Generate username
        initials = first_name[0] + last_name[0]
        dept_number = '01'  # replace with actual department number
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

        # Show username and password
        self.show_username_password(username, password)

    def generate_password(self):
        # Generate a password that meets the criteria
        length = 8
        all_chars = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(random.choice(all_chars) for _ in range(length))
            if (any(c.isupper() for c in password) and
                    any(c.isdigit() for c in password) and
                    any(c in string.punctuation for c in password)):
                return password

    def show_username_password(self, username, password):
        # Show the generated username and password in a popup window/dialog box
        msg = QMessageBox()
        msg.setWindowTitle("User Added Successfully")
        msg.setText(f"Username: {username}\nPassword: {password}")
        msg.exec_()