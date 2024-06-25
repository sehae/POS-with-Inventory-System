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

