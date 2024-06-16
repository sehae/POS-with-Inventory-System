from PyQt5 import QtCore


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
        self.updated_userType = None  # Initialize updated_userType to None
        self.current_username = None
        self.current_fullname = None  # Initialize current_fullname to None

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
        self.current_fullname = None
        print("USERMANAGER: User type reset to None")
        print("USERMANAGER: Username reset to None")
        print("USERMANAGER: Full Name reset to None")

    def get_user_type(self):
        return self.updated_userType

    def set_current_username(self, username):
        self.current_username = username
        print(f"USERMANAGER: Current username set to: {self.current_username}")
        self.username_updated.emit(username)

    def get_current_username(self):
        return self.current_username        return self.current_username

    def set_current_fullname(self, fullname):
        self.current_fullname = fullname
        print(f"USERMANAGER: Current fullname set to: {self.current_fullname}")
        self.fullname_updated.emit(fullname)

    def get_current_fullname(self):
        return self.current_fullname


