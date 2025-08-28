import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os

class SentimentProcessor:

    def __init__(self):
        nltk_dir = "/tmp/nltk_data"
        os.makedirs(nltk_dir, exist_ok=True)
        nltk.data.path.append(nltk_dir)
        nltk.download('vader_lexicon', download_dir=nltk_dir, quiet=True)
        self.analyzer = SentimentIntensityAnalyzer()

    def get_sentiment(self, text):
        score = self.analyzer.polarity_scores(text)
        compound = score['compound']
        if compound >= 0.5:
            return 'Positive'
        elif compound <= -0.5:
            return 'Negative'
        else:
            return 'Neutral'