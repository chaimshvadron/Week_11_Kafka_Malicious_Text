class MongoDAL:
    def __init__(self, db = None):
        self.db = db

    def fetch_all(self, collection_name):
        collection = self.db[collection_name]
        documents = list(collection.find({}))
        return documents
        
