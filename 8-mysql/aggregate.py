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

def getProductInfo(): # Toplam kayıt bilgilerini getirir.
    connection = mysql.connector.connect(host="localhost",user="root",password="1234",database="node-app")
    cursor = connection.cursor()

    # sql = "Select COUNT(*) from Products "
    # sql = "Select COUNT(*) from Products where price > 2000"
    # sql = "Select COUNT(name) from Products where price > 2000" # sayma işlemi

    # sql = "Select AVG(Price) from Products" # ortalama işlemi

    # sql = "Select SUM(Price) from Products" # toplama işlemi

    # sql = "Select MAX(Price) from Products" # maximum değer
    # sql = "Select MIN(Price) from Products" # toplama işlemi

    sql = "Select Name from Products Where Price = (Select MAX(Price) from Products)"

    cursor.execute(sql)
    result = cursor.fetchone()

    print(f'Result: {result[0]}')

getProductInfo()
