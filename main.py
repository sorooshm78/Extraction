import requests
import re

x = requests.get('https://w3schools.com/python/demopage.htm')
text = x.text
num = re.findall("[0-9]", text)
print(num)
