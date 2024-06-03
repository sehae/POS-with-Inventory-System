from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


def show_error_message(text):
    error_dialog = QtWidgets.QMessageBox()
    error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
    error_dialog.setWindowTitle("Error")
    error_dialog.setText(text)
    error_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
    error_dialog.exec_()


def show_username_password(username, password):
    msg = QMessageBox()
    msg.setWindowTitle("User's Credentials")
    msg.setText(f"Username: {username}\nPassword: {password}")
    msg.exec_()