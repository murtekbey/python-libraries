import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host="localhost",user="root",password="1234",database="node-app")
    cursor = connection.cursor()

    # cursor.execute("Select * from Products Order By name") # İsime göre Sıralama yapar.
    # cursor.execute("Select * from Products Order By price") # Fiyata göre Sıralama yapar.
    # cursor.execute("Select * from Products Order By id") # id'ye göre Sıralama yapar.
    # cursor.execute("Select * from Products Order By id DESC") # id'ye göre AZALAN! sıralama yapar.
    cursor.execute("Select * from Products Order By name, price") # önce isime göre daha sonra fiyata göre bir sıralama yapar.
    
    try:
        result = cursor.fetchall() 
        for product in result:
            print(f'ID: {product[0]}\tName: {product[1]}\tPrice: {product[2]}')
    except mysql.connector.Error as err:
        print('Hata:',err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')


def getProductById(id):
    connection = mysql.connector.connect(host="localhost",user="root",password="1234",database="node-app")
    cursor = connection.cursor()

    sql = "Select * from Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)
    result = cursor.fetchone()

    print(f'ID: {result[0]}, Name: {result[1]}, Price: {result[2]}')

getProducts()