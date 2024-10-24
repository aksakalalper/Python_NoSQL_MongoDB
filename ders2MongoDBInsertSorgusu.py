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
    collection = db["users"]
    # Veri yazma
    data={"name":"ahmet","phone":123456}
    collection.insert_one(data)
    datas=[
        {"name":"ahmet","phone":123456,"description":"erkek"},
        {"name":"mehmet","phone":456789,"description":["erkek","uzun"]},
        {"name":"ada","phone":456789},
        {"name":"yeşim","phone":2347896}
    ]
    collection.insert_many(datas)
    # Veri alma
    documents = collection.find()
    # Verileri yazdırma
    for doc in documents:
         print(doc,"\n")

except Exception as e:
    print(e)

