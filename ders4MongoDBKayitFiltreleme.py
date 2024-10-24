import pymongo
from bson.objectid import ObjectId

uri = "mongodb+srv://aksakal4646:******@cluster0.ohlhc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = pymongo.MongoClient(uri)
try:
    # Database seçme
    db = client["node-app"]
    # Koleksiyonu seçme
    collection = db["users"]
    # Sorgu oluşturulur.
    query={"name":"yeşim"}
    for i in collection.find(query):
        print(i,"\n")
    # _id bilgisi ile sorgulama yapılacaksa objectid eklenmesi gerekir.
    query={"_id":ObjectId("671932d2045fa1f09edf8e9a")}
    for i in collection.find(query):
        print(i,"\n")
    # İşaretler ile arama yapılır.
    query={"name":{"$in":["ahmet","ada"]}}
    for i in collection.find(query):
        print(i,"\n")
    # İşaretler ile arama yapılır.
    query={"phone":{"$gt":5000000}}
    for i in collection.find(query):
        print(i,"\n")
    # İşaretler ile arama yapılır.
    query={"phone":{"$eq":5000000}}
    for i in collection.find(query):
        print(i,"\n")
    # İşaretler ile arama yapılır.
    query={"phone":{"$gte":5000000}}
    for i in collection.find(query):
        print(i,"\n")
    # İşaretler ile arama yapılır.
    query={"phone":{"$lt":5000000}}
    for i in collection.find(query):
        print(i,"\n")
    # İşaretler ile arama yapılır.
    query={"name":{"$regex":"^ad"}}
    for i in collection.find(query):
        print(i,"\n")
    

except Exception as e:
    print(e)
