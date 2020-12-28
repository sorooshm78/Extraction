import requests
import re

x = requests.get('https://www.digikala.com/search/category-mobile-phone/')
page = x.text
num = re.findall("Moto E6 Play", page)
print(num)
