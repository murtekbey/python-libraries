html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Sayfası</title>
</head>
<body>
<h1 id="header">
        Python Kursu
        </h1>

    <div class="grup1">
        <h2>
            Programlama
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
            <li>Menü 4</li>
        </ul>
    </div>

    <div class="grup2">
        <h2>
            Modüller
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
            <li>Menü 4</li>
        </ul>
    </div>

    <div class="grup3">
        <h2>
            Django
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
            <li>Menü 4</li>
        </ul>
    </div>

    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    
</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify() # htmml dosyamızı düzenleme işlemi yapıyor.
result = soup.title # html dosyasındaki etiket içerisindeki tüm bilgiyi bize getirir.
result = soup.head
result = soup.body

result = soup.title.name # title etiketinin ismini getirir.
result = soup.title.string # title etiketi içerisinde string içeriği getirir.

result = soup.h1
result = soup.h2 # sadece ilk h2 etiketini getirir.
result = soup.h2.name
result = soup.h2.string

result = soup.find_all('h2') # tüm h2 etiketlerini bize getirir.
result = soup.find_all('h2')[0] # sadece ilk listedeki ilk elemanı getirir.
result = soup.find_all('h2')[1] # sadece ikinci listedeki ilk elemanı getirir.

result = soup.div # ilk grup divi gelir.
result = soup.find_all('div')
result = soup.find_all('div')[0] # grup 1 gelir. 1- div
result = soup.find_all('div')[1] # grup 2 gelir. 2- div
result = soup.find_all('div')[1].ul # 2. divin altındaki ul etiketi gelir.
result = soup.find_all('div')[1].ul.find_all('li') # 2. divin altındaki ul'nin altındaki li etiketleri gelir.

result = soup.div.findChildren() # divin altındaki bütün alt elemanları getir. ayrıca ul etiketindeki alt elemanları da dizin şeklinde tekrar getirir. soy ağacı ilişkisi vardır.
result = soup.div.parent.name # divin üstündeki ana başlığı bize gösterir. (body)

result = soup.div.findNextSibling() # 2. divi getirir. (1. divden bi sonraki gelir)
result = soup.div.findNextSibling().findNextSibling() # 3. divi getirir. (bu şekilde arka arkaya tekrarlanabilir.)
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling() # 2. divi getirir. 2 ileri 1 geri gidiyoruz.

result = soup.find_all('a') # tüm attribute'ları bize getirir.

for link in result: # tek tek dolaşıp alt alta yazdırabiliriz.
    print(link.get('href')) # a etiketi içerisindeki linkleri bu şekilde alabiliriz.

# print(result)