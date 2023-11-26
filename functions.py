import json
import sys
from pymongo import MongoClient

# from load_json import load_json

# Connecting to MongoDB
client = MongoClient('localhost', 27017)
db = client['291db']
collection = db['tweets']


def search_tweets(keywords):
    # Matching tweets containing all keywords
    query = {'$and': [{'content': {'$regex': keyword, '$options': 'i'}}
                      for keyword in keywords
                      ]}

    results = collection.find(query)

    # Print the id, date, content, and username for each matching tweet

    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: <script>.py <keyword1> <keyword2> ... <keywordN>")
        sys.exit(1)

    keywords = sys.argv[1:]
    search_tweets(keywords)
