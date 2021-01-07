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

# header table
for head in content.find_all("th"):
	if head.string is not None:
		sql = "ALTER TABLE sch ADD COLUMN %s varchar(255)" % head.string
		mycursor.execute(sql)

mydb.commit()
