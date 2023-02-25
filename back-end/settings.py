import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:<password>@cluster0.elnnjtq.mongodb.net/?retryWrites=true&w=majority")
db = client.test