import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host="localhost",user="root",password="1234",database="node-app")
    cursor = connection.cursor()

    #   cursor.execute("Select * from Products Where id=1") 
    #   cursor.execute("Select * from Products Where name='Samsung S8' and price>3000") 
    #   cursor.execute("Select * from Products Where name='Samsung S8' or price=3000") 
    #   cursor.execute("Select * from Products Where name LIKE '%Samsung%'") # içerisinde samsung geçen tüm kayıtları getirir.
    #   cursor.execute("Select * from Products Where name LIKE 'Samsung%'") # kayıdın başı samsungla başlamalı    
    cursor.execute("Select * from Products") # kayıdın sonu samsungla bitmeli    
    result = cursor.fetchall() 

    print(f'ID: {result[0]}, Name: {result[1]}, Price: {result[2]}')

    for product in result:
        print(f'ID: {product[0]}, Name: {product[1]}, Price: {product[2]}')

def getProductById(id):
    connection = mysql.connector.connect(host="localhost",user="root",password="1234",database="node-app")
    cursor = connection.cursor()

    sql = "Select * from Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)
    result = cursor.fetchone()

    print(f'ID: {result[0]}, Name: {result[1]}, Price: {result[2]}')

# getProducts() # Tüm elemanları getirir.
# getProductById(3) # id'ye göre tek bir elemanı istediğimiz gibi getirebiliriz.
