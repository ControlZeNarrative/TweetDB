import json
import pymongo
from pymongo import MongoClient


# indexing for display name and location
def loadjson(file_name, port):
    # Connect to MongoDB
    client = MongoClient('localhost', port)
    db = client['291db']
    # Drop the collection if it exists
    if 'tweets' in db.list_collection_names():
        db['tweets'].drop()

    # Create a new collection
    collection = db['tweets']

    # Checking the json file
    with open(file_name, 'r') as file:
        batch = []
        for line in file:
            try:
                tweet = json.loads(line)
                batch.append(tweet)
                # change the batch size as needed
                if len(batch) >= 1000:
                    collection.insert_many(batch)
                    batch.clear()
            except json.JSONDecodeError as e:
                print("Error decoding JSON: %s" % e)
                continue
        if batch:
            collection.insert_many(batch)

    create_indexes(db)


def create_indexes(db):
    # Text index for content field in tweets
    db['tweets'].create_index([("content", pymongo.TEXT)])
    db['tweets'].create_index("retweetCount")
    db['tweets'].create_index("likeCount")
    db['tweets'].create_index("quoteCount")
    # Index for user's username, displayname, and followersCount in tweets
    db['tweets'].create_index("user.displayname")
    db['tweets'].create_index("user.followersCount")

