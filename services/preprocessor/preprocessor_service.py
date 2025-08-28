from shared.text_processing.text_processor import TextProcessor
from shared.kafka.consumer import get_consumer
from shared.kafka.producer import send_messages

class PreprocessorService:
    def __init__(self):
        self.processor = TextProcessor()
        self.consumer = get_consumer(['raw_tweets_antisemitic', 'raw_tweets_not_antisemitic'])

    def process_message(self, message):
        original_text = message.get('text', '')
        processed_text = self.processor.process(original_text)
        message['processed_text'] = processed_text
        return message

    def get_output_topic(self, topic):
        if topic == 'raw_tweets_antisemitic':
            return 'preprocessed_tweets_antisemitic'
        elif topic == 'raw_tweets_not_antisemitic':
            return 'preprocessed_tweets_not_antisemitic'
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
