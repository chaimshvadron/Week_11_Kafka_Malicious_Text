from shared.db.connector import MongoDBConnection
import os
from services.dataretrieval.dal import DataRetrievalDAL

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "IranMalDBLocal")

def convert_objectid(data):
    for doc in data:
        if '_id' in doc:
            doc['id'] = str(doc.pop('_id'))
    return data

def get_tweets(collection_name):
    with MongoDBConnection(MONGO_URI, DB_NAME) as mongo_conn:
        collection = mongo_conn.db[collection_name]
        data = DataRetrievalDAL.get_all(collection)
        return convert_objectid(data)
