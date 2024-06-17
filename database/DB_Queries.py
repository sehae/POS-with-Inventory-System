""" This file contains all the queries that are used in the database """

# NEW QUERIES - NEW TABLE
GET_NEXT_ID = "SELECT MAX(user_id) FROM user;"
GET_USER_ID = "SELECT user_id FROM user WHERE email = %s;"
ADD_USER = ("INSERT INTO user (last_name, first_name, user_type, department, contact_number, email, username, password)"
            " VALUES (%s, %s, %s, %s, %s, %s, %s, %s);")
FETCH_USER_INFO = "SELECT * FROM admin WHERE username = %s;"
LOG_ACTIVITY = ("INSERT INTO user_logs (user_id, action_id, log_date, log_time, parameter) "
                "VALUES (%s, %s, %s, %s, %s);")
SEARCH_USER = ("SELECT first_name, last_name, email, department FROM user WHERE (last_name LIKE %s OR first_name LIKE %s OR "
                "email LIKE %s) AND is_active = True;")
CHANGE_USER_TYPE = "UPDATE user SET user_type = %s WHERE email = %s;"
CHANGE_DEPARTMENT = "UPDATE user SET department = %s WHERE email = %s;"
DISABLE_USER = "UPDATE user SET is_active = 'Disabled' WHERE email = %s;"
GET_USER_LOGS = "SELECT log_date, log_time, parameter FROM user_logs WHERE user_id = %s ORDER BY log_date DESC, log_time DESC;"
LOGIN = "SELECT user_id, password, is_active, user_type FROM user WHERE username = %s;"
GET_USER_FIRST_NAME = "SELECT first_name FROM user WHERE user_id = %s;"

# Authentication Queries
GET_ADMIN_LOGIN = "SELECT admin_id, password, is_active FROM admin WHERE username = %s;"
GET_ADMIN_ID = "SELECT admin_id FROM admin WHERE username = %s;"
GET_EMPLOYEE_ID = "SELECT employee_id FROM employee WHERE username = %s;"
GET_EMPLOYEE_LOGIN = "SELECT employee_id, password, is_active FROM employee WHERE username = %s;"
GET_ADMIN_PASSWORD = "SELECT password FROM admin WHERE username = %s;"
GET_EMPLOYEE_PASSWORD = "SELECT password FROM employee WHERE username = %s;"
CHECK_EMAIL_ADMIN = "SELECT email FROM admin WHERE email = %s;"
CHECK_EMAIL_EMPLOYEE = "SELECT email FROM employee WHERE email = %s;"

# User Information Retrieval Queries
GET_ADMIN_FIRST_NAME = "SELECT first_name FROM admin WHERE admin_id = %s;"
GET_EMPLOYEE_FIRST_NAME = "SELECT first_name FROM employee WHERE employee_id = %s;"
GET_NEXT_ADMIN_ID = "SELECT MAX(admin_id) FROM admin;"
GET_NEXT_EMPLOYEE_ID = "SELECT MAX(employee_id) FROM employee;"

# Update Queries
UPDATE_ADMIN_PASSWORD = "UPDATE admin SET password = %s WHERE email = %s;"
UPDATE_EMPLOYEE_PASSWORD = "UPDATE employee SET password = %s WHERE email = %s;"

# Add User Queries
ADD_ADMIN = ("INSERT INTO admin (last_name, first_name, contact_number, email, username, password) VALUES (%s, %s, %s, "
             "%s, %s, %s);")
ADD_EMPLOYEE = ("INSERT INTO employee (last_name, first_name, department, contact_number, email, username, password) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s);")
# ADD_ADMIN_LOGIN = "INSERT INTO adminlogin (admin_id, username, password) VALUES (%s, %s, %s);"
# ADD_EMPLOYEE_LOGIN = "INSERT INTO employeelogin (employee_id, username, password) VALUES (%s, %s, %s);"

# Retrieve data of the user
GET_ADMIN_DATA = "SELECT * FROM admin WHERE email = %s;"
GET_EMPLOYEE_DATA = "SELECT * FROM employee WHERE email = %s;"

# Update User Data Queries (SPECIFICALLY FOR EDIT USER SCREEN)
MOVE_TO_ADMIN = ("INSERT INTO admin (first_name, last_name, contact_number, email) SELECT first_name, last_name, "
                 "contact_number, email FROM employee WHERE email = %s AND is_active = True;")
MOVE_TO_EMPLOYEE = ("INSERT INTO employee (first_name, last_name, contact_number, email, department) SELECT"
                    "first_name, last_name, contact_number, email, %s FROM admin WHERE email = %s AND is_active = True;")
UPDATE_EMPLOYEE_DEPARTMENT = "UPDATE employee SET is_active = True, department = %s WHERE email = %s;"

# Update _is_active_ column
ENABLE_ADMIN = "UPDATE admin SET is_active = True WHERE email = %s;"
ENABLE_EMPLOYEE = "UPDATE employee SET is_active = True WHERE email = %s;"
DISABLE_ADMIN = "UPDATE admin SET is_active = False WHERE email = %s;"
DISABLE_EMPLOYEE = "UPDATE employee SET is_active = False WHERE email = %s;"

# Search User Query
SEARCH_EMPLOYEE = ("SELECT first_name, last_name, email, department FROM employee WHERE (last_name LIKE %s OR "
                   "first_name LIKE %s OR email LIKE %s) AND is_active = True;")
SEARCH_ADMIN = ("SELECT first_name, last_name, email, 'Admin' FROM admin WHERE (last_name LIKE %s OR first_name LIKE %s OR "
                "email LIKE %s) AND is_active = True;")

# User Logs
LOG = ("INSERT INTO user_logs (user_id, action_id, user_type, log_date, log_time, parameter) VALUES (%s, %s, %s, "
             "%s, %s, %s);")
GET_ACTION_BY_ID = "SELECT action FROM user_actions WHERE action_id = %s;"