import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host="localhost",user="root",password="1234",database="node-app")
    cursor = connection.cursor()

#   cursor.execute("Select * from Products") # Tüm kolonları seçmiş oluyoruz.
    cursor.execute("Select name,price from Products") # Sadece name ve price kolonlarını seçmiş oluyoruz.

#   result = cursor.fetchall() # Tüm kayıtları getirmiş oluruz.
    result = cursor.fetchone() # Sadece tek bir kaydı getirmiş oluruz

    # for i in result:
    #     print(f'Name: {i[0]}, Price: {i[1]}')
    print(f'Name: {result[0]}, Price: {result[1]}')

getProducts()