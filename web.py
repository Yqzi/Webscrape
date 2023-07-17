from bs4 import BeautifulSoup
import requests
import csv

url = "https://deviceatlas.com/resources/clientside/ios-hardware-identification"
ModelMap = {}

web = requests.get(url)
html = BeautifulSoup(web.text, "html.parser")
table = html.find('table', attrs={"class":"table table-striped table-bordered"})
table_row = table.find_all("tr")

for row in table_row:
    x = []
    tds = row.find_all("td")
    for td in tds:
        t = td.text.replace("iP", "|9064|iP").split("|9064|")[1:]
        x.append(t)
    if len(x) > 0:
        if x[2][0] == 'iPhone':
            for j in range(len(x[1])):
                ModelMap[x[1][j]] = input("sss?: ")

print(ModelMap)
