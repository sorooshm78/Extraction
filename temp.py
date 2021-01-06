from bs4 import BeautifulSoup
import requests
import mysql.connector


# local table
url ="<table><tr><th>First</th><th>Last</th><th>Age</th></tr><tr><td>Jill</td><td>Smith</td><td>50</td></tr><tr><td>Eve</td><td>Jackson</td><td>94</td></tr></table>"
soup = BeautifulSoup(url, "html.parser")
content = soup.find("table")


mydb = mysql.connector.connect(
  host="localhost",
  user="soroush",
  password="S.4556.m",
  database="sm"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE sch(id int)")

# header table
for head in content.find_all("th"):
    if head.string is not None:
		sql = "ALTER TABLE sch ADD (%s) char(255)"
		var = head.string
		mycursor.execute(sql, var)
       

mycursor.execute("SELECT * FROM sch")

for x in mycursor:
  print(x)

"""
# record table
for record in content.find_all("tr"):
    for el in record.find_all("td"):
"""
