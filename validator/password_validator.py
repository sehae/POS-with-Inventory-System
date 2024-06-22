from shared.dialog import show_error_message


def isValidPassword(password):
    title = "Invalid Password"

    if not password:
        return False  # Empty password, no need to show any error message

    if not 8 <= len(password) <= 20:
        if len(password) < 8:
            show_error_message(title, "Password must have a minimum of 8 characters.")
        elif len(password) > 20:
            show_error_message(title, "Password is too long. Password should be less than 20 characters.")
        return False

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

