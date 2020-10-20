import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host="localhost",user="root",password="1234",database="node-app")
    cursor = connection.cursor()

    cursor.execute("Select * from Products")

    result = cursor.fetchall() 

    for i in result:
        print(f'ID: {i[0]}, Name: {i[1]}, Price: {i[2]}')

def deleteProduct(id):
    connection = mysql.connector.connect(host="localhost",user="root",password="1234",database="node-app")
    cursor = connection.cursor()

    # sql = "Delete from products" # Tüm kayıtları siler. (products içindeki.)
    # sql = "Delete from products where id=6" # 6. kayıtı siler.
    # sql = "Delete from products where name like '%s7%'" # içinde s7 geçen tüm kayıtları siler.
    sql = "Delete from products where id=%s" # dışardan aldığımız id parametresine göre silme işlemi.
    values = (id,)
    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt silindi.')
    except mysql.connector.Error as err:
        print('Hata:',err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

deleteProduct(4)
getProducts()