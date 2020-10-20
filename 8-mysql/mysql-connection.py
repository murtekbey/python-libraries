import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", #192.23.45.56
    user = "root",
    password = "1234",
    database = "node-app"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), adress VARCHAR(255))")
