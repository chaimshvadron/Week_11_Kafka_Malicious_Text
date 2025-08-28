import json
import os
from services.retriever.db.dal import MongoDAL
from shared.db.connector import MongoDBConnection

STATE_FILE = os.path.join(os.path.dirname(__file__), 'retriever_state.json')

class RetrieverManager:
    def __init__(self, db, collection_name):
        self.collection_name = collection_name
        self.db = db
        self.dal = MongoDAL(self.db)
        self.skip = 0
        self._save_skip(self.skip)

    def _load_skip(self):
        if not os.path.exists(STATE_FILE):
            return 0
        with open(STATE_FILE, 'r') as f:
            return int(json.load(f).get("skip", 0))

    def _save_skip(self, skip):
        with open(STATE_FILE, 'w') as f:
            json.dump({"skip": skip}, f)

    def fetch_next(self, limit=100):
        
        batch = self.dal.fetch_next_batch(self.collection_name, skip=self.skip, limit=limit)
        if batch:
            self.skip += len(batch)
            self._save_skip(self.skip)
        return batch
