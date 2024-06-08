""" This file contains all the imports that are shared across multiple files. """

# PyQt5 imports
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QAction

# Database
from server.local_server import conn
from database.DB_Queries import (GET_ADMIN_LOGIN, GET_ADMIN_FIRST_NAME, GET_EMPLOYEE_LOGIN,
                                 GET_EMPLOYEE_FIRST_NAME, GET_ADMIN_ID, GET_EMPLOYEE_ID, UPDATE_ADMIN_PASSWORD,
                                 UPDATE_EMPLOYEE_PASSWORD)

# Security Module
from security.hash import hash_password, verify_password
from validator.password_validator import isValidPassword

# Shared
from shared.dialog import show_error_message

# Authentication Screens
from screens.authentication_screens.login_screen.loginScreen import Ui_MainWindow
from screens.authentication_screens.password_recovery.passwordRecovery import Ui_MainWindow

# Dashboard
from screens.admin_screens.admin_dashboard.adminDashboard_functions import myAdminDashboard