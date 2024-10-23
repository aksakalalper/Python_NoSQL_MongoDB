# kutuphane import edildi.
import pymongo
# alici bilgisi girilir.
client=pymongo.MongoClient("mongodb://localhost:27017")
db=client["node-app"]
collection=db["products"]
# Tüm belgeleri al
veriler = collection.find()

# Verileri yazdır
for veri in veriler:
    print(veri)

print(list(client.list_databases()))
