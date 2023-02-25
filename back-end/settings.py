# import pymongo

# client = pymongo.MongoClient("mongodb+srv://admin:<password>@cluster0.elnnjtq.mongodb.net/?retryWrites=true&w=majority")
# db = client.test

from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient()

# Create a new database
db = client['mydatabase']
collection_names = db.list_collection_names()

# Print out the collection names
for name in collection_names:
    print(name)