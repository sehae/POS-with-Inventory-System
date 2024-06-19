from datetime import datetime
from database.DB_Queries import GET_ACTION_BY_ID, LOG_ACTIVITY
from maintenance.pc_details import get_pc_name
from shared.imports import conn


def user_log(user_id, user_action, username, specific_action=None):
    log_datetime = datetime.now()
    log_time = log_datetime.time()
    log_date = log_datetime.date()
    pc_name = get_pc_name()

    try:
        cursor = conn.cursor()
        cursor.execute(GET_ACTION_BY_ID, (user_action,))
        action = cursor.fetchone()[0]
    except Exception as e:
        print(f"An error occurred while getting the action: {e}")
    finally:
        cursor.close()

    if specific_action is None:
        parameter = f"User:\"{username}\" using {pc_name}: {action}"
    else:
        parameter = f"User:\"{username}\" using {pc_name}: {action} \"{specific_action}\""

    # Execute the SQL query to log the user's login activity
    try:
        cursor = conn.cursor()
        cursor.execute(LOG_ACTIVITY, (user_id, user_action, log_date, log_time, parameter))
        conn.commit()
        print("User log created successfully")
    except Exception as e:
        print(f"An error occurred while logging the user's login activity: {e}")
    finally:
        cursor.close()

