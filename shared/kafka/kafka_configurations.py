from kafka import KafkaProducer
import os
import json

def get_producer_config():
    kafka_server = os.getenv("KAFKA_SERVERS", "kafka:9092")
    return KafkaProducer(
        bootstrap_servers=kafka_server,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
