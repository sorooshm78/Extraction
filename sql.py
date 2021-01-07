import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="soroush",
  password="S.4556.m",
  database="sm"
)

cursor = mydb.cursor()


table_name = "per"

sql_command = "SHOW TABLES LIKE \'%s\'" % table_name
cursor.execute(sql_command)
result = cursor.fetchone()

if result:
	print("exist")
else:
	print("not exist")
 
cursor.close()
