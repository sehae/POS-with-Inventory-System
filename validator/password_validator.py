from shared.dialog import show_error_message


def isValidPassword(password):
    title = "Invalid Password"
    
    if not 7 < len(password):
        show_error_message(title, "Password must have a minimum of 8 characters.")
        return False

    if len(password) > 20:
        show_error_message(title, "Password is too long. Password should be less than 20 characters.")

    if not any(char.isupper() for char in password):
        show_error_message(title, "Password must contain at least one uppercase letter.")
        return False

    if not any(char.isdigit() for char in password):
        show_error_message(title, "Password must contain at least one digit.")
        return False

    if not any(not char.isalnum() for char in password):
        show_error_message(title, "Password must contain at least one special character.")
        return False

    return True
