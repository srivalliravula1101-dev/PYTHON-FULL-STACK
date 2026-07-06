import pymysql

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "xyz")

cmd = conn.cursor()
id = int(input("Enter student ID"))
name = input("Enter student name")
branch = input("Enter student branch")

cmd.execute("INSERT INTO STUDENT VALUES(%s,%s,%s)",(id,name,branch))
print("data inserted")
# conn.commit()
# cmd.execute("CREATE TABLE IF NOT EXISTS STUDENT(ID INT,NAME VARCHAR(20),BRANCH VARCHAR(10));")
conn.commit()
conn.close()
