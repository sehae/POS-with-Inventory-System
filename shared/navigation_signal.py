from maintenance.user_logs import user_log


def auth_back(user_manager, back_signal, back_employee_signal):
    updated_user_type = user_manager.updated_department
    if updated_user_type == "Admin":
        back_signal.emit()
    elif updated_user_type == "Kitchen":
        back_employee_signal.emit()
    elif updated_user_type == "Cashier":
        back_employee_signal.emit()
