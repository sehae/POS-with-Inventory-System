def auth_back(user_manager, back_signal, back_employee_signal):
    updated_user_type = user_manager.updated_userType
    if updated_user_type == "Admin":
        back_signal.emit()
    elif updated_user_type == "Employee":
        back_employee_signal.emit()


def back(signal):
    signal.emit()