import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    )

if conn.is_connected():
    print("Connected to MySQL database")