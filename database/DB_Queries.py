""" This file contains all the queries that are used in the database """

# NEW QUERIES - NEW TABLE
GET_NEXT_ID = "SELECT MAX(user_id) FROM user;"
GET_USER_ID = "SELECT user_id FROM user WHERE email = %s;"
ADD_USER = ("INSERT INTO user (user_id, last_name, first_name, user_type, department, contact_number, email, username, "
            "password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);")
FETCH_USER_INFO = "SELECT * FROM user WHERE username = %s;"
LOG_ACTIVITY = ("INSERT INTO user_logs (user_id, action_id, log_date, log_time, parameter) "
                "VALUES (%s, %s, %s, %s, %s);")
SEARCH_USER = ("SELECT first_name, last_name, email, department FROM user WHERE (last_name LIKE %s OR first_name LIKE %s OR "
                "email LIKE %s) AND is_active = True;")
CHANGE_USER_TYPE = "UPDATE user SET user_type = %s WHERE email = %s;"
CHANGE_DEPARTMENT = "UPDATE user SET department = %s WHERE email = %s;"
DISABLE_USER = "UPDATE user SET is_active = 'Disabled' WHERE email = %s;"
GET_USER_LOGS = "SELECT log_date, log_time, parameter FROM user_logs WHERE user_id = %s ORDER BY log_date DESC, log_time DESC;"
LOGIN = "SELECT user_id, password, is_active, department FROM user WHERE username = %s;"
GET_USER_NAME = "SELECT first_name, last_name FROM user WHERE user_id = %s;"
UPDATE_PASSWORD = "UPDATE user SET password = %s WHERE email = %s;"
CHECK_EMAIL = "SELECT email FROM user WHERE email = %s;"
GET_USERNAME = "SELECT username FROM user WHERE email = %s;"
GET_PASSWORD = "SELECT password FROM user WHERE username = %s;"
GET_PASSWORD_BY_EMAIL = "SELECT password FROM user WHERE email = %s;"
UPDATE_PASSWORD_BY_USERNAME = "UPDATE user SET password = %s WHERE username = %s;"
GET_EMAIL = "SELECT email FROM user WHERE user_id = %s;"

# User Logs
LOG = ("INSERT INTO user_logs (user_id, action_id, user_type, log_date, log_time, parameter) VALUES (%s, %s, %s, "
             "%s, %s, %s);")
GET_ACTION_BY_ID = "SELECT action FROM user_actions WHERE action_id = %s;"