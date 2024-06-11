""" This file contains all the imports that are shared across multiple files. """

# Python imports
import sys
import random
import string

# PyQt5 imports
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QLineEdit, QAction, QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QRegExp

# Database
from server.local_server import conn
from database.DB_Queries import (GET_ADMIN_LOGIN, GET_ADMIN_FIRST_NAME, GET_EMPLOYEE_LOGIN,
                                 GET_EMPLOYEE_FIRST_NAME, GET_ADMIN_ID, GET_EMPLOYEE_ID, UPDATE_ADMIN_PASSWORD,
                                 UPDATE_EMPLOYEE_PASSWORD, ADD_ADMIN, ADD_EMPLOYEE,
                                 GET_ADMIN_DATA, GET_EMPLOYEE_DATA, MOVE_TO_ADMIN, MOVE_TO_EMPLOYEE,
                                 UPDATE_EMPLOYEE_DEPARTMENT, ENABLE_ADMIN, ENABLE_EMPLOYEE, DISABLE_ADMIN,
                                 DISABLE_EMPLOYEE, SEARCH_EMPLOYEE, SEARCH_ADMIN, DISABLE_ADMIN_ID,
                                 DISABLE_ACCOUNT_EMPLOYEE, DISABLE_ACCOUNT_ADMIN,)

# Automated Email
from automated.email_automation import send_username_password

# Security Module
from security.hash import hash_password, verify_password

# Validator
from validator.password_validator import isValidPassword
from validator.internet_connection import is_connected

# Shared
from shared.dialog import (show_error_message, show_username_password, confirmation_dialog, create_dialog_box)

# Styles
from styles.universalStyles import (COMBOBOX_STYLE, COMBOBOX_STYLE_VIEW, COMBOBOX_DISABLED_STYLE,
                                    ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE, )


