from bs4 import BeautifulSoup
import requests


# local table
url ="<table><tr><th>First</th><th>Last</th><th>Age</th></tr><tr><td>Jill</td><td>Smith</td><td>50</td></tr><tr><td>Eve</td><td>Jackson</td><td>94</td></tr></table>"
soup = BeautifulSoup(url, "html.parser")
content = soup.find("table")


# table from web
"""
url = "https://www.ffiec.gov/census/report.aspx?year=2011&state=01&report=demographic&msa=11500"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
content = soup.find("table", {"class":"main-body"})
"""

file = open("date.txt", "a")

# header table
for head in content.find_all("th"):
	if head.string is not None:
		file.write(head.string)
		file.write("\t")

file.write("\n")

# record table
for record in content.find_all("tr"):
	for el in record.find_all("td"):
		file.write(el.string)
		file.write("\t")

	file.write("\n")

file.close()
