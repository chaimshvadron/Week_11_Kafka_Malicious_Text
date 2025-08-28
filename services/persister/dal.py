class PersisterDAL:
    @staticmethod
    def insert_document(collection, data):
        # Remove _id if exists, so MongoDB will generate a new one
        if '_id' in data:
            del data['_id']
        collection.insert_one(data)
