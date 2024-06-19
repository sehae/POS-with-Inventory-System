from datetime import datetime
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
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            backup_file = f"MoonHeyHotpotandGrill_{timestamp}.sql"

            # Define the command to back up the database
            dumpcmd = f"mysqldump -u {conn.user} -p{password} {conn.database} -r {os.path.join(backup_path.replace("/", "\\"), backup_file)}"

            # Use the subprocess module to run the command
            p = subprocess.Popen(dumpcmd, shell=True, cwd="C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin")
            p.wait()

            print("Database backup successful")
    except Exception as e:
        print(f"An error occutyjtyjtjtrred: {e}")  # Print any errors that occur

# Function to restore the database from a backup
def restore_backup(original_file_name):
    # Construct the backup file name
    backup_file = original_file_name

    # Define the command to restore the database
    config = load_config()
    backup_path = config.get('DEFAULT', 'backup_path', fallback=None)
    restorecmd = f"mysql -u {conn.user} -p{password} {conn.database} < {os.path.join(backup_path.replace('/', '\\'), backup_file)}"

    # Use the subprocess module to run the command
    p = subprocess.Popen(restorecmd, shell=True, cwd="C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin")
    p.wait()

    print("Database restore successful")
