from bs4 import BeautifulSoup
import requests

url = "https://www.ebay.ca/deals?_trkparms=pageci%3Ae825a93c-2342-11ee-96bd-3e8771155599%7Cparentrq%3A5af3d44a1890aaee4d045db4fffdb7a7%7Ciid%3A1"


web = requests.get(url)
html = BeautifulSoup(web.text, "html.parser")
reviews = html.findAll("span", attrs={"class":"SECONDARY"})
names = html.findAll('span', attrs={"itemprop":"name"})
prices = html.findAll('span', attrs={"itemprop":"price"})





with open("data.csv", "w+") as csvfile:
    csvfile.write('Name')
    csvfile.write(' |9064| Price')




    for name, price in zip(names, prices):
        csvfile.write("\n" + name.text)
        csvfile.write(' |9064| ' + price.text)
