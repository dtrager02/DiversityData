import pandas as pd
from pymongo import MongoClient
import pymongo
import json
import os
"""form gives:
name,
file uploads,
types for each file
description
username comes from cookie -> ownedBy 

for each file:
    create collection with the filename
    mongoimport on the fileobject
    add its type as a document like {type:csv}

when user contributes:
    get database name and collection name from url
    receive documents to insert
    receive demographic data and update values in users collection
"""
class DatabaseOperations():
    def __init__(self,dbName="master"):
        self.CONNECTION_STRING = "mongodb+srv://administrator:7HlUBeIneZYKJwEV@cluster0.5o88u.mongodb.net/test"
        self.client = MongoClient(self.CONNECTION_STRING)
        self.db = self.client[dbName]

    def change_db(self,dbName):
        self.db = self.client[dbName]

    def close(self):
        self.client.close()
    
    # def findinCollection(self,collection,query={},start=0,limit=10**10):
    #     collection_name = self.db[collection]
    #     item_details = collection_name.find(query,skip=start,limit=limit)
    #     for item in item_details:
    #         yield item

    def get_database(self,dbName):
        #password: 7HlUBeIneZYKJwEV
        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        client = MongoClient(self.CONNECTION_STRING)

        # Create the database for our example (we will use the same database throughout the tutorial
        return client[dbName]
        
    def mongoimport(self,csv_path, coll_name,form):
        """ Imports a csv file at path csv_name to a mongo colection
        returns: count of the documants in the new collection
        """
        coll = self.db[coll_name]
        data = pd.read_csv(csv_path)
        payload = json.loads(data.to_json(orient='records'))
        #coll.remove()
        coll.insert_many(payload)
        return coll.count_documents()
    
    def mongoexport(self,collection):
        #first get part of name that is the dataset name, not the user
        dataset_name = dataset_name = self.db[collection].database.split(";")[0]
        type = self.db[collection].find_one({},{"type":1})["type"]
        os.system(f'mongoexport --uri="{self.CONNECTION_STRING}"  --collection="{collection} --out={dataset_name}.{type}')

    def get_collection_names(self):
        return self.db.list_collection_names()
    
    def insert_documents(self,collection,docs):
         self.db[collection].insert_many(docs)

if __name__ == "__main__":
    db = DatabaseOperations("master").db
    print(db["metadata"].find({},{"dataset":1})[0]['dataset'])