from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


def show_error_message(title, text):
    error_dialog = QtWidgets.QMessageBox()
    error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
    error_dialog.setWindowTitle(title)
    error_dialog.setText(text)
    error_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
    error_dialog.exec_()


def show_username_password(username, password):
    msg = QMessageBox()
    msg.setWindowTitle("User's Credentials")
    msg.setText(f"Username: {username}\nPassword: {password}")
    msg.exec_()

def confirmation_dialog(message):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText(message)
    msgBox.setWindowTitle("Confirmation")
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    return msgBox.exec_()

def create_dialog_box(message, title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText(message)
    msgBox.setWindowTitle(title)

    return msgBox.exec_