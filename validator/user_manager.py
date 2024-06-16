from PyQt5 import QtCore

from database.DB_Queries import FETCH_USER_INFO
from server.local_server import conn


class userManager(QtCore.QObject):
    _instance = None  # Singleton instance

    user_type_updated = QtCore.pyqtSignal(str)  # Create a signal
    username_updated = QtCore.pyqtSignal(str)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.updated_userType = None  # Initialize updated_userType to None
        self.current_username = None
        self.current_id = None

    def set_user_type(self, user_type):
        # Validate user_type (optional)
        if user_type in ("admin", "employee"):
            self.updated_userType = user_type
            print(f"USERMANAGER: User type updated to: {self.updated_userType}")  # Print within userManager
            self.user_type_updated.emit(user_type)  # Emit signal with new type
        else:
            # Handle invalid user type (e.g., raise exception)
            pass

    def reset_user_type(self):
        self.updated_userType = None
        print("USERMANAGER: User type reset to None")  # Print within userManager

    def reset_user_data(self):
        self.updated_userType = None
        self.current_username = None
        print("USERMANAGER: User type reset to None")
        print("USERMANAGER: Username reset to None")

    def get_user_type(self):
        return self.updated_userType

    def set_current_username(self, username):
        self.current_username = username
        print(f"USERMANAGER: Current username set to: {self.current_username}")
        self.username_updated.emit(username)

    def get_current_username(self):
        return self.current_username

    # Retrieve user information from the database
    def get_user_info(self, username):
        print(f"USERMANAGER: Retrieving user information for {username}...")

        cursor = conn.cursor()

        try:
            # Fetch all user information based on username
            cursor.execute(FETCH_USER_INFO, (username,))
            result = cursor.fetchone()

            if result is not None:
                self.set_current_user_id(result[0])

            print(f"USERMANAGER: User information retrieved.")
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()

    def set_current_user_id(self, id):
        self.current_id = id
        print(f"USERMANAGER: Current user id set to: {self.current_id}")

    def get_current_user_id(self):
        return self.current_id
