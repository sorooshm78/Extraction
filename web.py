from bs4 import BeautifulSoup
import requests
import json

url = "https://www.ffiec.gov/census/report.aspx?year=2011&state=01&report=demographic&msa=11500"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
content = soup.find("table", {"class":"main-body"})

file = open("date.txt", "a")

# header table
for head in content.find_all("th"):
	if head.string is not None:
		file.write(head.string)
		file.write("	")

file.write("\n")


# record table
for record in content.find_all("tr"):
	for el in record.find_all("td"):
		if el.string is None:
			file.write("	")
		else:
			file.write(el.string)
			file.write("	 ")

	file.write("\n")

file.close()
