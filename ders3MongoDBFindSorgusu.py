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
    # Sadece belirli öğeleri filtreleyerek getirir.
    for i in collection.find({},{"_id":0,"name":1,"phone":1}):
        print(i,"\n")

except Exception as e:
    print(e)
