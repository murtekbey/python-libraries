import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host="localhost",user="root",password="1234",database="node-app")
    cursor = connection.cursor()

    cursor.execute("Select * from Products")

    result = cursor.fetchall() 

    for i in result:
        print(f'ID: {i[0]}, Name: {i[1]}, Price: {i[2]}')

def updateProduct(id,name,price):
    connection = mysql.connector.connect(host="localhost",user="root",password="1234",database="node-app")
    cursor = connection.cursor()

    # sql = "Update products Set name='Samsung S10'" # Bütün name alanlarını Samsung S10 yapar.
    # sql = "Update products Set name='Samsung S10' where id=5" # id'si 5 olan kaydın name alanını Samsung S10 yapar.
    # sql = "Update products Set name='Samsung S10' where id=5" # id'si 5 olan kaydın name alanını Samsung S10 yapar.
    # sql = "Update products Set name='Samsung S10', price=5000 where id=5" # id'si 5 olan kaydın name alanını Samsung S10, fiyatını 5000 yapar.
    sql = "Update products Set name=%s, price=%s where id=%s" # name,price ve id parametrelerini dışardan alalım.
    values = (name,price,id)
    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi.')
    except mysql.connector.Error as err:
        print('Hata:',err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

# updateProduct(1,'Murtekbey S2Q',22500)
# getProducts()
