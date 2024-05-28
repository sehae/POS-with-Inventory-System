import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="poswithinventorysystem"
    )

if conn.is_connected():
    print("Connected to MySQL database")