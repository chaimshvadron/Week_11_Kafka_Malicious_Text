import os
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords



class TextProcessor:
    def __init__(self):
        nltk_dir = "/tmp/nltk_data"
        os.makedirs(nltk_dir, exist_ok=True)
        nltk.data.path.append(nltk_dir)
        nltk.download('stopwords', download_dir=nltk_dir, quiet=True)
        nltk.download('wordnet', download_dir=nltk_dir, quiet=True)
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def remove_punctuation_and_special(self, text):
        return ''.join([c for c in text if c.isalnum() or c.isspace()])

    def remove_extra_whitespace(self, text):
        return ' '.join(text.split()).strip()

    def to_lowercase(self, text):
        return text.lower()

    def remove_stopwords(self, text):
        return ' '.join([w for w in text.split() if w not in self.stop_words])

    def lemmatize_text(self, text):
        return ' '.join([self.lemmatizer.lemmatize(w) for w in text.split()])

    def process(self, text):
        text = self.remove_punctuation_and_special(text)
        text = self.remove_extra_whitespace(text)
        text = self.to_lowercase(text)
        text = self.remove_stopwords(text)
        text = self.lemmatize_text(text)
        return text
