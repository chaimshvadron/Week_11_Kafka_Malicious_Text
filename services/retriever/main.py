import os
import time
from shared.db.connector import MongoDBConnection
from services.retriever.manager import RetrieverManager
from shared.kafka.producer import send_messages

from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")


def publish_to_kafka(batch):
    antisemitic_msgs = [doc for doc in batch if doc.get("Antisemitic", 0)]
    not_antisemitic_msgs = [doc for doc in batch if not doc.get("Antisemitic", 0)]
    print(f"Antisemitic: {len(antisemitic_msgs)}, Not antisemitic: {len(not_antisemitic_msgs)}")
    if antisemitic_msgs:
        print(f"Publishing {len(antisemitic_msgs)} antisemitic messages to raw_tweets_antisemitic")
        send_messages("raw_tweets_antisemitic", antisemitic_msgs)
    if not_antisemitic_msgs:
        print(f"Publishing {len(not_antisemitic_msgs)} not antisemitic messages to raw_tweets_not_antisemitic")
        send_messages("raw_tweets_not_antisemitic", not_antisemitic_msgs)

def main():
    if not MONGO_URI or not DB_NAME:
        print("Missing MONGO_URI or DB_NAME in environment.")
        return
    with MongoDBConnection(MONGO_URI, DB_NAME) as mongo_conn:
        manager = RetrieverManager(mongo_conn.db, COLLECTION_NAME)
        while True:
            batch = manager.fetch_next(limit=100)
            if not batch:
                print("No more tweets to fetch. Waiting for new data...")
                time.sleep(60)
                continue
            publish_to_kafka(batch)
            print(f"Published {len(batch)} tweets to Kafka.")
            time.sleep(60)

if __name__ == "__main__":
    main()
