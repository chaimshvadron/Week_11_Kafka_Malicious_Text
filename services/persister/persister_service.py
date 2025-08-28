import os
from shared.db.connector import MongoDBConnection
from shared.kafka.consumer import get_consumer
from services.persister.dal import PersisterDAL

class PersisterService:
    def __init__(self):
        self.mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        self.db_name = os.getenv("DB_NAME", "IranMalDBLocal")
        self.consumer = get_consumer([
            "enriched_preprocessed_tweets_antisemitic",
            "enriched_preprocessed_tweets_not_antisemitic"
        ], group_id="persister-group")

    def get_collection_by_topic(self, db, topic):
        if topic == "enriched_preprocessed_tweets_antisemitic":
            return db["tweets_antisemitic"]
        elif topic == "enriched_preprocessed_tweets_not_antisemitic":
            return db["tweets_not_antisemitic"]
        return None

    def persist(self, db, topic, data):
        collection = self.get_collection_by_topic(db, topic)
        if collection:
            PersisterDAL.insert_document(collection, data)

    def run(self):
        try:
            with MongoDBConnection(self.mongo_uri, self.db_name) as mongo_conn:
                db = mongo_conn.db
                for message in self.consumer:
                    topic = message.topic
                    data = message.value
                    self.persist(db, topic, data)
        except KeyboardInterrupt:
            print("Shutting down PersisterService...")
        finally:
            self.consumer.close()
