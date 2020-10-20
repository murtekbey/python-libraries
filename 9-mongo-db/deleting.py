import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://")

mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

print('*'*50)

# mycollection.delete_one({"name":"Iphone 6"}) # ilk bulduğu kaydı siler.
# mycollection.delete_many({"name": {"$regex" : "^S"}}) # S ile başlayan tüm kayıtları siler.
result = mycollection.delete_many({}) # tüm kayıtları siler

print(f'{result.deleted_count} adet kayıt silindi.')

for i in mycollection.find():
    print(i)
# print(f'{result.modified_count} adet kayıt silindi.')