import pymongo

uri = "mongodb+srv://aksakal4646:373737@cluster0.ohlhc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = pymongo.MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    # Tüm veritabanı isimlerini alma
    databases = client.list_database_names()
# Veritabanı isimlerini yazdırma
    for db_name in databases:
        print(db_name)
except Exception as e:
    print(e)
