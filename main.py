from pymongo import MongoClient
from dotenv import dotenv_values
mongo_uri = "blabla"
mongo_client = MongoClient(mongo_uri)

database = mongo_client['database_test']
test_collection = database['test_collection']

person = {"name": "Lucca de Enzo", "age": 12 }
test_collection.insert_one(person)

config = dotenv_values('.env')
mongo_uri = config ['URI_MONGO_ALTAS']

mongo_client = MongoClient(mongo_uri)