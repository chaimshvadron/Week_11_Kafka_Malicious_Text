import os
from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
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
