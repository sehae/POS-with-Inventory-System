import mysql.connector

password = "root"

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=password,
    database="poswithinventorysystem"
    )

if conn.is_connected():
    print("Connected to MySQL database")