import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find_one({"name": "Samsung S5"})
# result = mycollection.find_one({"_id" : ObjectId("5f089e1e04aca92d96984b90")})

# result = mycollection.find({
#     "name": {
#         "$in" : ["Samsung S5", "Samsung S6"] # name içerisinde listede yazılan ifade geçiyorsa yazdırılır.
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$gt": 2000 # fiyatı 2000'den yüksek kayıtlar.
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$gte": 2000 # fiyatı 2000'e eşit ya da yüksek kayıtlar.
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$eq": 2000 # fiyatı 2000'e eşit kayıtlar.
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$lt": 2000 # fiyatı 2000'den az kayıtlar.
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$lte": 2000 # fiyatı 2000'e eşit ya da az kayıtlar.
#     }
# })

# mongoDB query operatörleri => https://docs.mongodb.com/manual/reference/operator/query/

result = mycollection.find({
    "name": {"$regex": "^S"} # name alanı S ile başlayan kayıtlar.
})

for i in result:
    print(i)

# print(result)