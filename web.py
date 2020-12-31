from bs4 import BeautifulSoup
import requests

url = "https://www.digikala.com/product/dkp-3754319/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-poco-x3-m2007j20cg-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-128-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA"

req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

#div = soup.find_all("div", {"class":"c-product__price-survey-question u-hidden js-price-question js-pricing-survey"})

content = soup.find_all("script", {"type":"application/ld+json"})

# use regex 
print(content)
