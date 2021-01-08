import mysql.connector


f = open("/home/soroush/Desktop/work/Extraction/date.txt", "r")
line = f.readline()
for x in line:
	print(x)
"""
  mydb = mysql.connector.connect(
  host="localhost",
  user=***,
  password=***,
  database="sm"
)

cursor = mydb.cursor()
"""
