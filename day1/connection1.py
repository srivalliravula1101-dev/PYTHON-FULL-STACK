import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "abc"
)
if conn.is_connected():
    print("Database connected")
else:
    print("Not connected")    
