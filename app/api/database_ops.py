import pandas as pd
from pymongo import MongoClient
import pymongo
import json

class DatabaseOperations():
    def __init__(self,dbName):
        self.db = self.get_database(dbName)

    def get_database(self,dbName):
        #password: 7HlUBeIneZYKJwEV
        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        CONNECTION_STRING = "mongodb+srv://administrator:7HlUBeIneZYKJwEV@cluster0.5o88u.mongodb.net/test"

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        client = MongoClient(CONNECTION_STRING)

        # Create the database for our example (we will use the same database throughout the tutorial
        return client[dbName]

    def findinCollection(self,collection,query={},start=0,limit=10**10):
        collection_name = self.db[collection]
        item_details = collection_name.find(query)
        for item in item_details:
            yield item
        
    def mongoimport(self,csv_path, coll_name):
        """ Imports a csv file at path csv_name to a mongo colection
        returns: count of the documants in the new collection
        """
        coll = self.db[coll_name]
        data = pd.read_csv(csv_path)
        payload = json.loads(data.to_json(orient='records'))
        #coll.remove()
        coll.insert_many(payload)
        return coll.count()


if __name__ == "__main__":
    db = DatabaseOperations("Dataset1")
    print(next(db.findinCollection("animals.csv"))["WebframeWorkedWith"])