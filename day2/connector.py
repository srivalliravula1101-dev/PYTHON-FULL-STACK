import pymysql
def get_connection():
    conn = pymysql.connect(
       host = "localhost",
       user = "root",
       password = "root",
       database = "pqr")

    return conn

