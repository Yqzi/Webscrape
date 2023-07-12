from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com"

web = requests.get(url)
html = BeautifulSoup(web.text, "html.parser")
quotes = html.findAll("span", attrs={"class":"text"})
authors = html.findAll('small', attrs={"class":"author"})

for authors in authors:
    print(authors.text)