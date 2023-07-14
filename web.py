from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com"

web = requests.get(url)
html = BeautifulSoup(web.text, "html.parser")
quotes = html.findAll("span", attrs={"class":"text"})
authors = html.findAll('small', attrs={"class":"author"})


with open("data.csv", "w+") as csvfile:
    csvfile.write('Quotes')
    csvfile.write('|9064| Authors')


    for quotes, authors in zip(quotes, authors):
        csvfile.write("\n" + quotes.text)
        csvfile.write('|9064| ' + authors.text)
