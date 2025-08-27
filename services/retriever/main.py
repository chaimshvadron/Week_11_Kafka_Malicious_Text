import os
import time
from shared.db.connector import MongoDBConnection
from services.retriever.manager import RetrieverManager
from shared.kafka.kafka_configurations import get_producer_config

from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
DB_NAME = MONGO_URI.split("/")[-1] if MONGO_URI else None

producer = get_producer_config()

def publish_to_kafka(batch):
    for doc in batch:
        topic = "raw_tweets_antisemitic" if doc.get("antisemietic", 0) else "raw_tweets_not_antisemitic"
        producer.send(topic, value=doc)
    producer.flush()

def main():
    if not MONGO_URI or not DB_NAME:
        print("Missing MONGO_URI or DB_NAME in environment.")
        return
    mongo_conn = MongoDBConnection(MONGO_URI, DB_NAME)
    manager = RetrieverManager(mongo_conn.db, COLLECTION_NAME)
    while True:
        batch = manager.fetch_next(limit=100)
        if not batch:
            print("No more tweets to fetch.")
            break
        publish_to_kafka(batch)
        print(f"Published {len(batch)} tweets to Kafka.")
        time.sleep(60)

if __name__ == "__main__":
    main()
