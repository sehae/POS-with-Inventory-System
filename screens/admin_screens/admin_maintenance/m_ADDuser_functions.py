import mysql
from PyQt5 import QtWidgets, QtGui
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

        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")
        print(f"Contact Number: {contact_number}")
        print(f"Level of Access: {LoA}")
        print(f"Department: {dept}")

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