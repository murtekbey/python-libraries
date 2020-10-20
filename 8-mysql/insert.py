import mysql.connector

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host="localhost",user="root",password="1234",database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values) # sorgu hazırlanmış oluyo.

    try:
        connection.commit() # sorgu databaseye gönderiliyor.
        print(f'{cursor.rowcount} tane kayıt eklendi.')
        print(f'Son eklenen kaydın id numarası: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:',err)
    finally:
        connection.close()
        print('Database bağlantısı kapandı.')

def insertProducts(list):
    connection = mysql.connector.connect(host="localhost",user="root",password="1234",database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql,values) # sorgu hazırlanmış oluyo.

    try:
        connection.commit() # sorgu databaseye gönderiliyor.
        print(f'{cursor.rowcount} tane kayıt eklendi.')
        print(f'Son eklenen kaydın id numarası: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:',err)
    finally:
        connection.close()
        print('Database bağlantısı kapandı.')

list = []
while True:
    name = input('Ürün adını giriniz: ')
    price = float(input('Ürün fiyatını giriniz: '))
    imageUrl = input('Ürün resim adını giriniz: ')
    description = input('Ürün açıklaması giriniz: ')

    list.append((name,price,imageUrl,description))

    result = input('Kayıt eklemeye devam etmek ister misiniz? (e/h): ')
    if result == 'h':
        print('Kayıtlarınız veritabanına aktarılıyor..')
        print(list)
        insertProducts(list)
        break
        # kayıt

# insertProduct(name,price,imageUrl,description)