from bs4 import BeautifulSoup
import requests

url = "https://deviceatlas.com/resources/clientside/ios-hardware-identification"
ModelMap = {}
priceMap = {}

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
        if "iPhone4,1" in x[1]: break
        if x[2][0] == 'iPhone':
            run = True
            while run:
                v = ""
                try:
                    v = input("Price of " + x[0][0] + ": ")
                    priceMap[x[0][0]] = float(v)
                    run = False
                except:
                    if v.lower() == "f": 
                        priceMap[x[0][0]] = False
                        run = False
                    else:
                        print('no')
            for j in range(len(x[1])):
                ModelMap[x[1][j]] = x[0][0]

with open("data.json", "w+") as f:
    f.write({"Model" : ModelMap, "Price" : priceMap}.__repr__().replace("'", '"'))
    
