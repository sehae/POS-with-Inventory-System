from PyQt5 import QtCore

from database.DB_Queries import FETCH_USER_INFO
from server.local_server import conn


class userManager(QtCore.QObject):
    _instance = None  # Singleton instance

    user_type_updated = QtCore.pyqtSignal(str)  # Create a signal
    username_updated = QtCore.pyqtSignal(str)
    fullname_updated = QtCore.pyqtSignal(str)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.updated_department = None  # Initialize updated_userType to None
        self.current_username = None
        self.current_id = None
        self.current_department = None
        self.current_fullname = None  # Initialize current_fullname to None

    def set_department(self, department):
        # Validate user_type (optional)
        if department in ("Admin", "Cashier", "Kitchen"):
            self.updated_department = department
            self.user_type_updated.emit(department)  # Emit signal with new type
        else:
            # Handle invalid user type (e.g., raise exception)
            pass

    def reset_user_data(self):
        self.updated_department = None
        self.current_username = None
        self.current_fullname = None
        print("USERMANAGER: User data reset.")
        
    def get_department(self):
        return self.updated_department

    def set_current_username(self, username):
        self.current_username = username
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
                self.set_current_department(result[4])


            print(f"USERMANAGER: User information retrieved.")
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()

    def set_current_user_id(self, id):
        self.current_id = id
        print(f"USERMANAGER: Current user id set to: {self.current_id}")

    def set_current_department(self, department):
        self.current_department = department
        print(f"USERMANAGER: Current department set to: {self.current_department}")

    def get_current_user_id(self):
        return self.current_id

    def get_current_department(self):
        return self.current_department
    
    def set_current_fullname(self, fullname):
        self.current_fullname = fullname
        print(f"USERMANAGER: Current fullname set to: {self.current_fullname}")
        self.fullname_updated.emit(fullname)

    def get_current_fullname(self):
        return self.current_fullname


