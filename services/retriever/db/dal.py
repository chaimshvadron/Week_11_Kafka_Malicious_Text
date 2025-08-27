class MongoDAL:
    def __init__(self, db = None):
        self.db = db

    def fetch_all(self, collection_name):
        collection = self.db[collection_name]
        documents = list(collection.find({}))
        return documents

    def fetch_next_batch(self, collection_name, last_date=None, last_id=None, limit=100):

        collection = self.db[collection_name]
        query = {}
        if last_date is not None and last_id is not None:
            query = {
                "$or": [
                    {"createdate": {"$gt": last_date}},
                    {"createdate": last_date, "_id": {"$gt": last_id}}
                ]
            }
        elif last_date is not None:
            query = {"createdate": {"$gte": last_date}}
            
        cursor = collection.find(query).sort([("createdate", 1), ("_id", 1)]).limit(limit)
        return list(cursor)
        
