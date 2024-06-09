from PyQt5 import QtCore

class userManager(QtCore.QObject):
    _instance = None  # Singleton instance

    user_type_updated = QtCore.pyqtSignal(str)  # Create a signal

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.updated_userType = None  # Initialize updated_userType to None

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
