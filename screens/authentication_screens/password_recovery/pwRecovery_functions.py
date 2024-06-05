from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QAction

from screens.authentication_screens.password_recovery.passwordRecovery import Ui_MainWindow
from server.local_server import conn
from validator.password_validator import isValidPassword
from security.encryption import generate_key, create_cipher, encrypt_data, decrypt_data


class PasswordRecovery(Ui_MainWindow):
    def __init__(self, email):
        super().__init__()
        self.email = email
        self.id, self.source_table = self.check_email_source(email)
        self.check_action = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.saveBTN.clicked.connect(self.save_password)
        self.pw_visibilityBTN.clicked.connect(lambda: self.toggle_visibility(self.passwordFIELD, self.pw_visibilityBTN))
        self.rp_visibilityBTN.clicked.connect(lambda: self.toggle_visibility(self.retypeFIELD, self.rp_visibilityBTN))
        self.passwordFIELD.textChanged.connect(self.check_password_match)
        self.retypeFIELD.textChanged.connect(self.check_password_match)
        self.UiComponents()

    def UiComponents(self):
        self.passwordFIELD.setEchoMode(QLineEdit.Password)
        self.retypeFIELD.setEchoMode(QLineEdit.Password)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOff.png"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("assets/Icons/visibilityOn.png"), QIcon.Normal, QIcon.On)
        self.pw_visibilityBTN.setIcon(icon)
        self.rp_visibilityBTN.setIcon(icon)

    def toggle_visibility(self, field, button):
        if field.echoMode() == QtWidgets.QLineEdit.Password:
            field.setEchoMode(QtWidgets.QLineEdit.Normal)
            button.setIcon(QtGui.QIcon("assets/Icons/visibilityOn.png"))
        else:
            field.setEchoMode(QtWidgets.QLineEdit.Password)
            button.setIcon(QtGui.QIcon("assets/Icons/visibilityOff.png"))

    def check_password_match(self):
        # Compare the text in the password and retype fields
        if self.passwordFIELD.text() == self.retypeFIELD.text():
            # Create the check icon action
            check_icon = QIcon("assets/Icons/check.png")
            self.check_action = QAction(check_icon, "Passwords Match", self.passwordFIELD)

            # Add the check icon action to the password fields
            self.passwordFIELD.addAction(self.check_action, QLineEdit.TrailingPosition)
            self.retypeFIELD.addAction(self.check_action, QLineEdit.TrailingPosition)
        else:
            # Remove the check icon action from the password fields
            if self.check_action:
                self.passwordFIELD.removeAction(self.check_action)
                self.retypeFIELD.removeAction(self.check_action)

    def save_password(self):
        new_password = self.passwordFIELD.text()
        retype_new_password = self.retypeFIELD.text()

        if new_password == retype_new_password:
            # Validate the new password
            if not isValidPassword(new_password):
                return

            key = generate_key()
            cipher = create_cipher(key)
            encrypted_password = encrypt_data(cipher, new_password.encode())

            cursor = conn.cursor()
            try:
                if self.source_table == 'admin':
                    cursor.execute(
                        "UPDATE adminlogin SET password = %s WHERE admin_id = %s",
                        (encrypted_password, self.id)
                    )
                elif self.source_table == 'employee':
                    cursor.execute(
                        "UPDATE employeelogin SET password = %s WHERE employee_id = %s",
                        (encrypted_password, self.id)
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


