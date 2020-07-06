from bs4 import BeautifulSoup as soup
import requests
import time
from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np

client = MongoClient()
coin_market = client.get_database("CoinMarket")
coin_price = coin_market.get_collection("CoinPrice")
url = "https://coinmarketcap.com/all/views/all/"
t = int(time.time())
rt = t
while rt - t < 0.0001:
    response = requests.get(url)
    page_soup = soup(response.content, "html.parser")
    rows = page_soup.find_all("tr")
    for row in rows:
        data = row.find_all("td")
        list_cell = []
        for cell in data:
            list_cell.append(cell.text)
        if list_cell != []:
            if coin_price.find_one({"Name": list_cell[1]}) == None:
                coin = {
                    "Name": list_cell[1],
                    "Symbol": list_cell[2],
                    "Price": [list_cell[4]]
                }
                coin_price.insert_one(coin)
            else:
                unit_update = coin_price.find_one({"Name": list_cell[1]})
                unit_update["Price"].append(list_cell[4])
                coin_price.update_one({"Name": list_cell[1]},{"$set":{"Price": unit_update["Price"]}})
    all_coin = coin_price.find()
    for item in all_coin:
        fig,ax = plt.subplots()
        print(ax.plot(range(len(item["Price"])),item["Price"]))
        plt.show()
    rt = int(time.time())
    time.sleep(3)


