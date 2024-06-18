import json
import os

from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from maintenance.backup_restore import backup_db, load_config, save_config
from screens.admin_screens.admin_maintenance.backup import Ui_MainWindow
from shared.navigation_signal import back
from styles.universalStyles import COMBOBOX_STYLE, COMBOBOX_STYLE_VIEW


class adminMaintenanceBACKUP(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    add_signal = QtCore.pyqtSignal()
    edit_signal = QtCore.pyqtSignal()
    def __init__(self):
        try:
            super().__init__()
            self.setupUi(self)
            self.backBTN.clicked.connect(lambda: back(self.back_signal))
            self.adduserBTN.clicked.connect(self.add_signal.emit)
            self.editBTN.clicked.connect(self.edit_signal.emit)

            self.viewBTN.clicked.connect(self.view_backup_location)
            self.selectfolderBTN.clicked.connect(self.select_backup_directory)
            self.backupnowBTN.clicked.connect(self.start_backup_timer)

            config = load_config()
            directory = config.get('DEFAULT', 'backup_path', fallback=None)
            if directory:
                self.filelocDISPLAY.setText(directory)

            # Create a QTimer object
            self.timer = QTimer()

            # Connect the timeout signal of the timer to the updateDateTime slot
            self.timer.timeout.connect(self.updateDateTime)

            # Set the interval for the timer (in milliseconds)
            self.timer.start(1000)  # Update every second

            self.UIComponents()
        except Exception as e:
            print(f"An error occurred: {e}")

    def UIComponents(self):
        self.frequencyBOX.setStyleSheet(COMBOBOX_STYLE)
        self.frequencyBOX.view().setStyleSheet(COMBOBOX_STYLE_VIEW)
        self.backupDatesBOX.setStyleSheet(COMBOBOX_STYLE)
        self.backupDatesBOX.view().setStyleSheet(COMBOBOX_STYLE_VIEW)

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.dateDISPLAY.setText(formattedDateTime)

    def select_backup_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")

        if directory:
            # Save the backup directory to the configuration file
            save_config(directory)

            # Set the text of the filelocDISPLAY label to the selected directory
            self.filelocDISPLAY.setText(directory)

    def start_backup_timer(self):
        print("Starting backup timer")
        # Get the selected backup frequency
        frequency = self.frequencyBOX.currentText()

        # Determine the interval based on the selected frequency
        if frequency == 'Hourly':
            interval = 60 * 60 * 1000  # 1 hour in milliseconds
        elif frequency == 'Daily':
            interval = 24 * 60 * 60 * 1000  # 1 day in milliseconds
        elif frequency == 'Weekly':
            interval = 7 * 24 * 60 * 60 * 1000  # 1 week in milliseconds
        else:
            print(f"Unknown frequency: {frequency}")
            return

        # Create a QTimer object
        self.backup_timer = QTimer()

        # Connect the timeout signal of the timer to the backup_db method
        config = load_config()
        backup_path = config.get('DEFAULT', 'backup_path', fallback=None)
        print(f"Backup path: {backup_path}")
        if backup_path:
            self.backup_timer.timeout.connect(backup_db(backup_path))

        # Start the timer with the determined interval
        self.backup_timer.start(interval)
        print(f"Database will be backed up every {frequency.lower()}")
        print(f"Timer is active: {self.backup_timer.isActive()}")  # Check if the timer is active

    def view_backup_location(self):
        try:
            config = load_config()
            backup_path = config.get('DEFAULT', 'backup_path', fallback=None)
            if backup_path:
                print(f"The backup location is: {backup_path}")
                os.startfile(backup_path)  # Open the backup directory in the file explorer
            else:
                print("No backup location has been set.")
        except Exception as e:
            print(f"An error occurred: {e}")

