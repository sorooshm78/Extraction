import mysql.connector
import re


def find_file(word):
	f = open("pass.txt", "r")
	txt = f.read()
	s = re.findall(word + " =.*", txt)
	return s[0].replace(word + " = ","")



mydb = mysql.connector.connect(
host="localhost",
user=find_file("username"),
password=find_file("password"),
database="sm"
)

cursor = mydb.cursor()
