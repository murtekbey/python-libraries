import requests

from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

# list = soup.find("ul", {"class":"lister-list"}).find_all("tr", limit=50)

# list = soup.find("div", {"class":"listView"}).find("ul").find_all("li", {"class":"column"}, limit=10)
list = soup.find_all("li", {"class":"column"}, limit=10)
count = 1

for li in list:
    # name = ul.find("div", {"class":"proDetail"}).find("a").get("title")
    name = li.div.a.h3.text.strip()
    link = li.div.a.get('href')
    # oldPrice = li.find("a", {"class":"oldPrice"}).find("del").text
    # newPrice = li.find("a", {"class":"newPrice"}).find("ins").text.split()[0]
    oldPrice = li.find("div", {"class":"proDetail"}).find_all("a")[0].text.strip().strip('TL')
    newPrice = li.find("div", {"class":"proDetail"}).find_all("a")[1].text.split()[0]
    print(f"{count}. Ürün Adı: {name}\nEski fiyatı: {oldPrice} TL\tYeni fiyatı: {newPrice} TL\nLink: {link}\n")
    count+=1