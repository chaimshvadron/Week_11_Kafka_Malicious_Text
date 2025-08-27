import os
from pymongo import MongoClient
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

class MongoDBConnection:
    def __init__(self):
        self.connection_string = os.getenv("MONGODB_CONNECTION_STRING")
        self.client = None

    def __enter__(self):
        try:
            self.client = MongoClient(self.connection_string)
            print(f"Connected to MongoDB")
            return self
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")
