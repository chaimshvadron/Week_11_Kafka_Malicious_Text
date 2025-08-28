import os

from services.enricher.sentiment_processor import SentimentProcessor
from services.enricher.weapon_processor import WeaponProcessor
from services.enricher.date_processor import DateProcessor
from shared.kafka.consumer import get_consumer
from shared.kafka.producer import send_messages

class EnricherService:
    def __init__(self):
        self.sentiment_processor = SentimentProcessor()
        self.weapon_processor = WeaponProcessor(weapon_list_path="data/weapon_list.txt")
        self.date_processor = DateProcessor()
        self.consumer = get_consumer(['preprocessed_tweets_antisemitic', 'preprocessed_tweets_not_antisemitic'])

    def process_message(self, message):
        original_text = message.get('text', '')
        processed_sentiment = self.sentiment_processor.get_sentiment(original_text)
        message['sentiment'] = processed_sentiment
        processed_weapon = self.weapon_processor.find_weapon(original_text)
        message['weapons_detected'] = processed_weapon
        processed_date = self.date_processor.find_latest_date(original_text)
        message['relevant_timestamp'] = processed_date
        if 'TweetID' in message:
            del message['TweetID']
        return message

    def get_output_topic(self, topic):
        if topic == 'preprocessed_tweets_antisemitic':
            return 'enriched_preprocessed_tweets_antisemitic'
        elif topic == 'preprocessed_tweets_not_antisemitic':
            return 'enriched_preprocessed_tweets_not_antisemitic'
        return None

    def run(self):
        for message in self.consumer:
            topic = message.topic
            data = message.value
            processed_data = self.process_message(data)
            output_topic = self.get_output_topic(topic)
            if output_topic:
                send_messages(output_topic, [processed_data])
        self.consumer.close()
