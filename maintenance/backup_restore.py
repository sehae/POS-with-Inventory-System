import datetime
import subprocess
import os
import configparser
from server.local_server import conn, password

# Function to load configuration
def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

# Function to save configuration
def save_config(backup_path):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'backup_path': backup_path}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

# Function to back up the database
def backup_db(backup_path):
    try:
        print("Backup function called")  # Print a message when the function is called
        if conn.is_connected():
            # Generate a timestamped filename for the backup file
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            backup_file = f"Moon Hey Hotpot and Grill_{timestamp}.sql"

            # Define the command to back up the database
            dumpcmd = f"mysqldump -h{conn.server_host} -u{conn.user} -p{password} {conn.database} > {os.path.join(backup_path, backup_file)}"

            # Use the subprocess module to run the command
            subprocess.Popen(dumpcmd, shell=True)

            print("Database backup successful")
    except Exception as e:
        print(f"An error occurred: {e}")  # Print any errors that occur
