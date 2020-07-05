from bs4 import BeautifulSoup as soup
import requests
import time

url = "https://coinmarketcap.com/all/views/all/"
fname = "CoinMarketData.txt"
f = open(fname,"w")
f.write("\t")
f.close()
t = int(time.time())
rt = t
response = requests.get(url)
page_soup = soup(response.content, "html.parser")
rows = page_soup.find_all("tr")
for row in rows:
    data = row.find_all("td")
    list_cell = []
    for cell in data:
        list_cell.append(cell.text)
    if len(list_cell) > 0:
        f = open(fname,"a")
        f.write("\t"+list_cell[1]+" ("+list_cell[2]+")")
        f.close()
i = 0
while rt - t < 3600:
    response = requests.get(url)
    page_soup = soup(response.content, "html.parser")
    rows = page_soup.find_all("tr")
    i += 1
    f = open(fname,"a")
    f.write("\nprice"+str(i))
    f.close()
    for row in rows:
        data = row.find_all("td")
        list_cell = []
        for cell in data:
            list_cell.append(cell.text)
        if len(list_cell) > 0:
            while len(list_cell[4]) < len(list_cell[1]) + len(list_cell[2]) + 3:
                list_cell[4] += " "
            f = open(fname,"a")
            f.write("\t"+list_cell[4])
            f.close()
    rt = int(time.time())
    time.sleep(300)


