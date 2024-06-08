""" This file contains all the queries that are used in the database """

# Authentication Queries
GET_ADMIN_LOGIN = "SELECT admin_id, password FROM adminlogin WHERE username = %s;"
GET_EMPLOYEE_LOGIN = "SELECT employee_id, password FROM employeelogin WHERE username = %s;"

# User Information Retrieval Queries
GET_ADMIN_FIRST_NAME = "SELECT first_name FROM admin WHERE admin_id = %s;"
GET_EMPLOYEE_FIRST_NAME = "SELECT first_name FROM employee WHERE employee_id = %s;"
GET_ADMIN_ID = "SELECT admin_id FROM admin WHERE email = %s;"
GET_EMPLOYEE_ID = "SELECT employee_id FROM employee WHERE email = %s;"

# Update Queries
UPDATE_ADMIN_PASSWORD = "UPDATE adminlogin SET password = %s WHERE admin_id = %s;"
UPDATE_EMPLOYEE_PASSWORD = "UPDATE employeelogin SET password = %s WHERE employee_id = %s;"

# Add User Queries
ADD_ADMIN = "INSERT INTO admin (last_name, first_name, contact_number, email) VALUES (%s, %s, %s, %s);"
ADD_EMPLOYEE = ("INSERT INTO employee (last_name, first_name, department, contact_number, email) VALUES (%s, %s, %s, "
                "%s, %s);")
ADD_ADMIN_LOGIN = "INSERT INTO adminlogin (admin_id, username, password) VALUES (%s, %s, %s);"
ADD_EMPLOYEE_LOGIN = "INSERT INTO employeelogin (employee_id, username, password) VALUES (%s, %s, %s);"
