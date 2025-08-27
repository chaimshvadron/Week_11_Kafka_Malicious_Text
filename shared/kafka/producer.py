from shared.kafka.kafka_configurations import get_producer_config


producer = get_producer_config()

def send_messages(topic, messages):
    for msg in messages:
        producer.send(topic, msg)
    producer.flush()
