import datetime
import json
import os

from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from maintenance.backup_restore import backup_db, load_config, save_config, restore_backup
from maintenance.user_logs import user_log
from screens.admin_screens.admin_maintenance.backup import Ui_MainWindow
from shared.dialog import create_dialog_box
from styles.universalStyles import COMBOBOX_STYLE, COMBOBOX_STYLE_VIEW
from validator import user_manager
from validator.user_manager import userManager


class adminMaintenanceBACKUP(QMainWindow, Ui_MainWindow):
    back_signal = QtCore.pyqtSignal()
    add_signal = QtCore.pyqtSignal()
    edit_signal = QtCore.pyqtSignal()
    def __init__(self):
        try:
            super().__init__()
            self.setupUi(self)
            self.backBTN.clicked.connect(self.back_signal.emit)
            self.adduserBTN.clicked.connect(self.add_signal.emit)
            self.editBTN.clicked.connect(self.edit_signal.emit)
            self.restoreBTN.clicked.connect(self.handle_restore_click)
            self.viewBTN.clicked.connect(self.view_backup_location)
            self.selectfolderBTN.clicked.connect(self.select_backup_directory)
            self.backupnowBTN.clicked.connect(self.start_backup_timer)

            self.update_last_backup_date()
            self.update_backup_dates()

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
            # Perform a backup immediately
            self.perform_backup(backup_path)

            # Connect the timeout signal of the timer to the backup_db method
            self.backup_timer.timeout.connect(lambda: self.perform_backup(backup_path))

        # Start the timer with the determined interval
        self.backup_timer.start(interval)
        print(f"Database will be backed up every {frequency.lower()}")
        print(f"Timer is active: {self.backup_timer.isActive()}")  # Check if the timer is active

    def perform_backup(self, backup_path):
        # Perform the backup
        backup_db(backup_path)

        # Update the backup dates in the combobox
        self.update_backup_dates()

        # Update the last backup date display
        self.update_last_backup_date()
        create_dialog_box("Backup successful", "Backup")

        user_action = 14
        self.log_action(user_action)

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

    def update_last_backup_date(self):
        config = load_config()
        backup_path = config.get('DEFAULT', 'backup_path', fallback=None)
        if backup_path:
            try:
                # List all files in the backup directory
                files = os.listdir(backup_path)

                # Filter out directories, leaving only files
                files = [f for f in files if os.path.isfile(os.path.join(backup_path, f))]

                # If there are no files, there's no backup date to display
                if not files:
                    self.lastbackupDISPLAY.setText("No backups yet")
                    return

                # Sort the files by modification time
                files.sort(key=lambda x: os.path.getmtime(os.path.join(backup_path, x)))

                # Get the modification time of the most recent file
                last_backup_time = os.path.getmtime(os.path.join(backup_path, files[-1]))

                # Convert the modification time to a datetime object
                last_backup_date = datetime.datetime.fromtimestamp(last_backup_time)

                # Format the datetime object as a string
                last_backup_date_str = last_backup_date.strftime(
                    '%B %d, %Y, %H:%M:%S')  # Month Day, Year, Hour:Minute:Second format

                formatted_date_time = last_backup_date.strftime('%B %d, %Y %I:%M %p')

                # Display the last backup date
                self.lastbackupDISPLAY.setText(formatted_date_time)
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            self.lastbackupDISPLAY.setText("No backup location set")

    def update_backup_dates(self):
        config = load_config()
        backup_path = config.get('DEFAULT', 'backup_path', fallback=None)
        if backup_path:
            try:
                # Clear the combobox
                self.backupDatesBOX.clear()
                self.original_filename = {}

                # List all files in the backup directory
                files = os.listdir(backup_path)

                # Filter out directories, leaving only files
                files = [f for f in files if os.path.isfile(os.path.join(backup_path, f))]

                # If there are no files, there's no backup date to display
                if not files:
                    self.backupDatesBOX.addItem("No backups yet")
                    return

                # Sort the files by modification time
                files.sort(key=lambda x: os.path.getmtime(os.path.join(backup_path, x)), reverse=True)

                # Add the sorted files to the combobox
                for file in files:
                    # Extract the date from the file name
                    date_time_str = f"{file.split('_')[1]} {file.split("_")[2].replace(".sql", "")}"  # Get the date part of the file name
                    date_time_obj = datetime.datetime.strptime(date_time_str,
                                                          '%Y-%m-%d %H-%M-%S')  # Convert the date string to a datetime object
                    formatted_date = date_time_obj.strftime('%B %d, %Y %I:%M %p')  # Format the date as Month Day, Year
                    self.original_filename[formatted_date] = file
                    self.backupDatesBOX.addItem(formatted_date)
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            self.backupDatesBOX.addItem("No backup location set")

    def handle_restore_click(self):
        # Get the selected date from the combobox
        selected_date_str = self.backupDatesBOX.currentText()

        original_file_name = self.original_filename[selected_date_str]

        # Call the restore_backup function with the selected date
        restore_backup(original_file_name)
        create_dialog_box(f"Database restored successfully to {selected_date_str}", "Restore")
        user_action = 15
        specific_action = f"Restored database to {selected_date_str}"
        self.log_action(user_action, specific_action)

    def log_action(self, user_action, specific_action=None):
        user_manager = userManager._instance
        user_id = user_manager.get_current_user_id()
        username = user_manager.get_current_username()
        user_log(user_id, user_action, username, specific_action)