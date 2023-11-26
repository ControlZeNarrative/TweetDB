import json
import sys
from pymongo import MongoClient

from load-json import load_json

# Connecting to MongoDB
client = MongoClient('localhost', 27017)
db = client[db]
collection = db['tweets']


def search_tweets(keywords: tuple, db: str):
    
    # Matching tweets containing all keywords
    query = {'$and': [{'content': {'$regex': keyword, '$options': 'i'}} 
    for keyword in keywords
    ]}

    results = collection.find(query)

    # Print the id, date, content, and username for each matching tweet
    for tweet in results:
        print(f"ID: {tweet['id']}")
        print(f"Date: {tweet['date']}")
        print(f"Content: {tweet['content']}")
        print(f"Username: {tweet['username']}")
        print("-------------------")

    return results
