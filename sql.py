import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="soroush",
  password="S.4556.m",
  database="sm"
)

mycursor = mydb.cursor()

#mycursor.execute("SHOW TABLES")
mycursor.execute("SELECT * FROM person")

for x in mycursor:
  print(x)
