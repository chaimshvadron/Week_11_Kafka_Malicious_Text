from fastapi import FastAPI,  FastAPI
from services.dataretrieval.dataretrieval_service import get_tweets

app = FastAPI()

@app.get("/tweets_antisemitic")
def api_get_antisemitic():
    return get_tweets("tweets_antisemitic")

@app.get("/tweets_not_antisemitic")
def api_get_not_antisemitic():
    return get_tweets("tweets_not_antisemitic")
