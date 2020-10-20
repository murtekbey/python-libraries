import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://")

mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

# mycollection.update_one( # bulduğu ilk kaydı update eder.
#     {"name": "Samsung S6"},
#     {"$set": {
#         "name": "Iphone 6",
#         "price": "5000"    
#     }}
# )

query = {"name": "Samsung"}
newvalues = {"$set": {
        "name": "Iphone 6",
        "price": "5000"    
    }}

result = mycollection.update_many(query, newvalues) # bulduğu bütün kayıtları update eder.

print(f'{result.modified_count} adet kayıt güncellendi.')

for i in mycollection.find():
    print(i)