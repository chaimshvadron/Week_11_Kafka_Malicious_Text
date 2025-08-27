import json
import os
from db.dal import MongoDAL
from db.connector import get_db_connection

STATE_FILE = os.path.join(os.path.dirname(__file__), 'retriever_state.json')

class RetrieverManager:
    def __init__(self, db, collection_name):
        self.collection_name = collection_name
        self.db = db
        self.dal = MongoDAL(self.db)
        self.state = self._load_state()

    def _load_state(self):
        if not os.path.exists(STATE_FILE):
            return {"last_date": None, "last_id": None}
        with open(STATE_FILE, 'r') as f:
            return json.load(f)

    def _save_state(self, last_date, last_id):
        with open(STATE_FILE, 'w') as f:
            json.dump({"last_date": last_date, "last_id": str(last_id)}, f)

    def fetch_next(self, limit=100):
        last_date = self.state.get("last_date")
        last_id = self.state.get("last_id")
        batch = self.dal.fetch_next_batch(self.collection_name, last_date, last_id, limit)
        if batch:
            last_doc = batch[-1]
            self._save_state(last_doc.get("createdate"), last_doc.get("_id"))
            self.state = {"last_date": last_doc.get("createdate"), "last_id": str(last_doc.get("_id"))}
        return batch
