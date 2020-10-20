import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host="localhost",user="root",password="1234",database="node-app")
    cursor = connection.cursor()

    # sql = "Select * From Categories"
    # sql = "Select * From Products"
    # sql = "Select * From Products inner join Categories on Categories.id=Products.Categoryid" # Her bir ürün bilgisinin sonuna bir kategori bilgisi eklendi.
    # sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid" # isim,fiyat ve kategori bilgisi gelir.
    # sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid where Categories.name='Telefon'" # sadece categories'de name kısmı telefon olanlar gelir.
    sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid where Products.name='Samsung S10'" # sadece products'da name kısmı samsung s10 olanlar gelir.
    sql = "Select p.name,p.price,c.name From Products as p inner join Categories as c on c.id=p.Categoryid where p.name='Samsung S10'" # Products yerine p, Categories yerine c atayarak sadeleştirdik.


    cursor.execute(sql) 

    try:
        result = cursor.fetchall()
        for product in result:
            # print(f'ID: {product[0]}, Name: {product[1]}, Price: {product[2]}')
            print(product)
    except mysql.connector.Error as err:
        print('Hata: ',err)
    finally:
        connection.close()
        print('Database bağlantısı kapatıldı.')

getProducts()