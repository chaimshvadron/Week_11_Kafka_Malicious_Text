class PersisterDAL:
    @staticmethod
    def insert_document(collection, data):
        collection.insert_one(data)
