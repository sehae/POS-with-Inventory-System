""" This file contains all the imports that are shared across multiple files. """

# Python imports
import random
import string

# PyQt5 imports
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QLineEdit, QAction
from PyQt5.QtCore import QRegExp

# Database
from server.local_server import conn
from database.DB_Queries import (GET_ADMIN_LOGIN, GET_ADMIN_FIRST_NAME, GET_EMPLOYEE_LOGIN,
                                 GET_EMPLOYEE_FIRST_NAME, GET_ADMIN_ID, GET_EMPLOYEE_ID, UPDATE_ADMIN_PASSWORD,
                                 UPDATE_EMPLOYEE_PASSWORD, ADD_ADMIN, ADD_EMPLOYEE, ADD_ADMIN_LOGIN, ADD_EMPLOYEE_LOGIN)

# Automated Email
from automated.email_automation import send_username_password

# Security Module
from security.hash import hash_password, verify_password

# Validator
from validator.password_validator import isValidPassword
from validator.internet_connection import is_connected

# Shared
from shared.dialog import show_error_message, show_username_password

# Styles
from styles.universalStyles import COMBOBOX_STYLE, COMBOBOX_STYLE_VIEW, COMBOBOX_DISABLED_STYLE

# Authentication Screens
from screens.authentication_screens.login_screen.loginScreen import Ui_MainWindow
from screens.authentication_screens.password_recovery.passwordRecovery import Ui_MainWindow

# Dashboard
from screens.admin_screens.admin_dashboard.adminDashboard_functions import myAdminDashboard