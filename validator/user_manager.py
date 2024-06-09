from PyQt5 import QtCore

class userManager(QtCore.QObject):
    user_type_updated = QtCore.pyqtSignal(str)  # Create a signal

    def __init__(self):
        super().__init__()
        self.userType = None # Initialize userType to None

    def set_user_type(self, user_type):
        # Validate user_type (optional)
        if user_type in ("admin", "employee"):
            self.userType = user_type
            print(f"USERMANAGER: User type updated to: {self.userType}")  # Print within userManager
            self.user_type_updated.emit(user_type)  # Emit signal with new type
        else:
            # Handle invalid user type (e.g., raise exception)
            pass
