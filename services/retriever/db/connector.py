import os
from pymongo import MongoClient
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

class MongoDBAtlasConnection:
	def __init__(self):
		self.connection_string = os.getenv("MONGODB_CONNECTION_STRING")
		self.db_name = os.getenv("MONGODB_DBNAME", "IranMalDB")
		self.client = None
		self.db = None

	def __enter__(self):
		try:
			self.client = MongoClient(self.connection_string)
			self.db = self.client[self.db_name]
			print(f"Connected to MongoDB Atlas, database: {self.db_name}")
			return self
		except Exception as e:
			print(f"Failed to connect to MongoDB Atlas: {e}")
			raise

	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.client:
			self.client.close()
			print("MongoDB Atlas connection closed.")

	def get_db(self):
		return self.db

if __name__ == "__main__":
    with MongoDBAtlasConnection() as conn:
        db = conn.get_db()
        print("Connection test successful:", db is not None)

