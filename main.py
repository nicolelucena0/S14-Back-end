from pymongo import MongoClient

mongo_uri = "mongodb+srv://nick37:17092007Nc@cluster0.ftznygf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo_client = MongoClient(mongo_uri)

database = mongo_client['database_test']
test_collection = database['test_collection']

person = {"name"; "Lucca de Enzo", "age": 12 }
test_collection.insert_one(person)