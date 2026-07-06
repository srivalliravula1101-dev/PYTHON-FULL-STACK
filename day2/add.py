import mysql.connector
def get_connection():
     con = mysql.connector.connect(
          host="localhost",
          user="root",
          password="root",
          database="abc"
     )
     
     return con

def AddStudent():
     sid = int(input("Enter sId: "))
     sname = input("Enter sName: ")
     sbranch = input("Enter sBranch")
     
     conn = get_connection()
     cmd = conn.cursor()
     cmd.execute("INSERT INTO STUDENT VALUES(%s,%s,%s)",(sid,sname,sbranch))     
     print("Data inserted !!!!")
     conn.commit()
     conn.close()
     
def deleteStudent():
     sid = int(input("Enter sid to delete: "))
     conn = get_connection()
     cmd = conn.cursor()
     cmd.execute("DELETE FROM STUDENT WHERE s_id=%s",(sid,))
     print("Student deleted successfullyyyy!!!!")
     conn.commit()
     conn.close()

def updateStudent():
     print("Choose one option to update: ")
     print("1. s_id")
     print("2. s_name")
     print("3. s_branch")
     
     option = int(input("Enter your option: "))
     sid = int(input("Enter your s_id: "))
     
     conn = get_connection()
     cmd = conn.cursor()
     if option == 1:
          new_sid = int(input("Enter your new sId"))
          cmd.execute("UPDATE STUDENT SET s_id = %s where s_id = %s",(new_sid,sid))
     elif option == 2:
          new_sname = input("Enter your new sName: ")
          cmd.execute("UPDATE STUDENT SET s_name = %s where s_id = %s",(new_sname,sid))
     elif option == 3:
          new_sbranch = input("Enter your new sBranch: ")
          cmd.execute("UPDATE STUDENT SET s_branch = %s where s_id = %s",(new_sbranch,sid))
     else:
          print("Choose correct option")
          
     print("Updated Successfullyyyyy")
     conn.commit()
     conn.close()
  
print("Welcome Admin\n-------------")   
while True:
     print("Choose one option:")
     print("1. Add Student Details")
     print("2. Delete Student Details")
     print("3. Update Student Details")
     print("4. Exit")
     
     option = int(input("Enter your Option: "))
     
     if option == 1:
          AddStudent()
     elif option == 2:
          deleteStudent()
     elif option == 3:
          updateStudent()
     elif option == 4:
          print("Bye Admin !!!")
          break
     else:
          print("Please check options and try again!!!!!!")
