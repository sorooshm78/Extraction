from bs4 import BeautifulSoup
import requests
import mysql.connector
import re

# *************************** function ***************************

def check_exist(sql, word):
	mycursor.execute(sql)
	result = mycursor.fetchall()
	for x in result:
		if word in x:
			return True
	return False	

def exist(sql):
	mycursor.execute(sql)
	result = mycursor.fetchone()
	if result:
		return True
	else:
		return False
	
def find_file(word):
	f = open("info.txt", "r")
	txt = f.read()
	s = re.findall(word + ".*=.*", txt)
	return s[0].replace(" ","").replace(word + "=","")

# *************************** setting ***************************

url = find_file("url")
database_name = find_file("database")
table_name = find_file("table")
username = find_file("username")
password = find_file("password")
host = find_file("host")

# *************************** html config ***************************

# web url
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")


# local url
#soup = BeautifulSoup(url, "html.parser")

html = soup.find("table")
header = html.find_all("th")
record = html.find_all("tr")

# mysql config
mydb = mysql.connector.connect(
  host = host,
  user = username,
  password = password,
)

mycursor = mydb.cursor()

print("*************************** check exist database ***************************")

sql_command = "SHOW DATABASES LIKE \'%s\'" % database_name

if exist(sql_command):
	print("database exist")
else:
	print("database not exist")
	sql_command = "CREATE DATABASE `%s`" %(database_name)
	print(sql_command)
	mycursor.execute(sql_command)

sql = "USE %s" % database_name
mycursor.execute(sql)

print("*************************** check exist table ***************************")

sql_command = "SHOW TABLES LIKE \'%s\'" % table_name

if exist(sql_command):
	print("table exist")
else:
	print("table not exist")
	id = header[0].string
	sql_command = "CREATE TABLE `%s` (`%s` VARCHAR(255))" %(table_name, id)
	print(sql_command)
	mycursor.execute(sql_command)

print("*************************** check name exist ***************************")

for x in range(1, len(record)):
	el = record[x].find_all("td")
	val_id = el[0].string
	id = header[0].string

	sql = "SELECT `%s` FROM `%s`" %(id, table_name)

	if check_exist(sql, val_id) == True:
		print(val_id + " is exist")
	else:
		print(val_id + " is not exist")	
		sql_command = "INSERT INTO `%s` (`%s`) VALUES (\"%s\")"% (table_name, id, val_id)
		print(sql_command)
		mycursor.execute(sql_command)
		mydb.commit()


print("*************************** insert header table ***************************")

for x in range(1, len(header)):
		column = header[x].string
		sql = "SHOW COLUMNS FROM `%s` LIKE \"%s\"" %(table_name, column)

		if exist(sql) == True:
			print(column + " column is exist")
		else:
			print(column + " column is not exist")
			sql_command = "ALTER TABLE `%s` ADD COLUMN `%s` VARCHAR(255)" % (table_name, column)
			print(sql_command)
			mycursor.execute(sql_command)
			mydb.commit()

print("*************************** insert record table ***************************")
for x in range(1, len(record)):
	el = record[x].find_all("td")
	val_id = el[0].string

	for y in range(1, len(el)):	
		column = header[y].string
		val_column = el[y].string
		sql_command = "UPDATE `%s` SET `%s` = \"%s\" WHERE `%s` = \"%s\"" % (table_name, column, val_column, id, val_id)

		print(sql_command)
		mycursor.execute(sql_command)
		mydb.commit()
