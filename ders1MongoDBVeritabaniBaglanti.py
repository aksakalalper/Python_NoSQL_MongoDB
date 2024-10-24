import pymongo

uri = "mongodb+srv://aksakal4646:******@cluster0.ohlhc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = pymongo.MongoClient(uri)

try:
    # Tüm veritabanı isimlerini alma
    databases = client.list_database_names()
    # Veritabanı isimlerini yazdırma
    for db_name in databases:
        print(db_name)
    # Veritabanını seçme
    db = client["node-app"]
    # Koleksiyonu seçme
    collection = db["products"]
    # Veri alma
    documents = collection.find()
    # Verileri yazdırma
    for doc in documents:
         print(doc,"\n")

except Exception as e:
    print(e)
