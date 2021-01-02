from bs4 import BeautifulSoup
import requests
import json

url = "https://www.ffiec.gov/census/report.aspx?year=2011&state=01&report=demographic&msa=11500"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
content = soup.find("table", {"class":"main-body"})

# header table
for x in content.find_all("th"):
	print("header:", x.string)

# record table
for record in content.find_all("tr"):
	print("-----------------------")
	for el in record.find_all("td"):
		print(el.string)
