import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find().sort('name', 1) # alfabetik sıraya göre sıralar.
# result = mycollection.find().sort('name', -1) # alfabetik sıranın tersine göre sıralar.
# result = mycollection.find().sort('price', 1) # fiyatı azalandan artana doğru sıralar.
# result = mycollection.find().sort('price', -1) # fiyatı artandan azalana doğru sıralar.
result = mycollection.find().sort([('name',1),('price',-1)]) # önce isime sonra fiyata göre sıralama.

for i in result:
    print(i)