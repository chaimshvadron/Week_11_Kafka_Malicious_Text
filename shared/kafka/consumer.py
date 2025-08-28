from kafka import KafkaConsumer
import os
import json

def get_consumer(topics, group_id="default-group"):
    kafka_server = os.getenv("KAFKA_SERVERS", "localhost:9092")
    return KafkaConsumer(
        *topics,
        bootstrap_servers=kafka_server,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        group_id=group_id
    )
