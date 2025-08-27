import os
from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, connection_string, db_name):
        self.connection_string = connection_string
        self.db_name = db_name
        self.client = None
        self.db = None

    def __enter__(self):
        try:
            self.client = MongoClient(self.connection_string)
            self.db = self.client[self.db_name]
            print(f"Connected to MongoDB, DB: {self.db_name}")
            return self
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")
