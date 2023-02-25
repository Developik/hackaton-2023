import os

import dotenv

import pymongo
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

username = os.environ.get('MONGODB_USERNAME')
password = os.environ.get('MONGODB_PASSWORD')

print("USERNAME", username)
print("PASSWORD", password)

client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.elnnjtq.mongodb.net/?retryWrites=true&w=majority")

print(client.server_info())
db = client.sample_airbnb