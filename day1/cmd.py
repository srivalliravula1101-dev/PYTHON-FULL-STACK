import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "abc"
)

cmd = conn.cursor()

cmd.executed("CREATE TABLE IF NOT EXISTS demo(id int,name varchar(10));")
print("Table created go and check")
conn.commit()
conn.close()