import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

list = soup.find("tbody", {"class":"lister-list"}).find_all("tr", limit=50)
count = 1

for tr in list:
    title = tr.find("td", {"class":"titleColumn"}).find("a").text # listedeki ilk 10 filmin isim bilgisi bize gelir.
    released = tr.find("td", {"class":"titleColumn"}).find("span").text.strip("()")
    rate = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text
    print(f'{count}. Filmin adı: {title.ljust(50)}\tImdb Puanı: {rate} Çıkış tarihi: {released}')
    count+=1