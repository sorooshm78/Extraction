from bs4 import BeautifulSoup
import requests
import mysql.connector

# setting
url = "<table><tr><th>name</th><th>riazy</th><th>araby</th></tr><tr><td>Jill</td><td>19</td><td>20</td></tr><tr><td>Eve</td><td>18</td><td>50</td></tr></table>"
database_name = "sm"
table_name = "pop"
#username
#password

# html config
soup = BeautifulSoup(url, "html.parser")
html = soup.find("table")
header = html.find_all("th")
record = html.find_all("tr")

# mysql config
mydb = mysql.connector.connect(
  host = "localhost",
  user = "soroush",
  password = "S.4556.m",
  database = database_name
)

mycursor = mydb.cursor()

# check exist table
sql_command = "SHOW TABLES LIKE \'%s\'" % table_name
mycursor.execute(sql_command)
result = mycursor.fetchone()

if result:
	print("exist")
else:
	print("not exist")
	id = header[0].string
	sql_command = "CREATE TABLE %s(%s VARCHAR(255))" %(table_name, id)
	print(sql_command)
	mycursor.execute(sql_command)

# ********************* fix check name exist **********************

# insert id
for x in range(1, len(record)):
	el = record[x].find_all("td")
	val_id = el[0].string
	sql_command = "INSERT INTO pop (%s) VALUES (\"%s\")"% (id, val_id)
	print(sql_command)
	mycursor.execute(sql_command)


# insert header table
for x in range(1, len(header)):
		column = header[x].string
		sql_command = "ALTER TABLE pop ADD COLUMN %s INT" % column		
		print(sql_command)
		mycursor.execute(sql_command)


# insert record
for x in range(1, len(record)):
	el = record[x].find_all("td")
	val_id = el[0].string
	for y in range(1, len(el)):	
		column = header[y].string
		val_column = el[y].string
		sql_command = "UPDATE pop SET %s = %s WHERE %s = \"%s\"" % (column, val_column, id, val_id)
		print(sql_command)
		mycursor.execute(sql_command)
	
mydb.commit()
