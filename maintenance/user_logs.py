from datetime import datetime
from database.DB_Queries import LOG, GET_ACTION_BY_ID
from shared.imports import conn

def user_log(user_id, user_action, user_type, username):
    parameter = user_type
    log_datetime = datetime.now()
    log_time = log_datetime.time()
    log_date = log_datetime.date()

    try:
        cursor = conn.cursor()
        cursor.execute(GET_ACTION_BY_ID, (user_action,))
        action = cursor.fetchone()[0]
    except Exception as e:
        print(f"An error occurred while getting the action: {e}")
    finally:
        cursor.close()

    parameter = f"{username} {action} {parameter}"

    # Execute the SQL query to log the user's login activity
    try:
        cursor = conn.cursor()
        cursor.execute(LOG, (user_id, user_action, user_type, log_date, log_time, parameter))
        conn.commit()
    except Exception as e:
        print(f"An error occurred while logging the user's login activity: {e}")
    finally:
        cursor.close()