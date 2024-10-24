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
    # Artan şekilde sıralar.
    for i in collection.find().sort("name",1):
        print(i,"\n")
    # Azalan şekilde sıralar.
    for i in collection.find().sort("name",-1):
        print(i,"\n")

except Exception as e:
    print(e)
