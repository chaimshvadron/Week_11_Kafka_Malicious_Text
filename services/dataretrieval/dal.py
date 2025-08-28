class DataRetrievalDAL:
    @staticmethod
    def get_all(collection):
        return list(collection.find({}, {"_id": 0}))
