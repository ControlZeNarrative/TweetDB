import json
import sys
from pymongo import MongoClient


def load_json(file_name, port):
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
                if len(batch) >= 5000:
                    collection.insert_many(batch)
                    batch.clear()
            except json.JSONDecodeError as e:
                print("Error decoding JSON: %s" % e)
                continue
        if batch:
            collection.insert_many(batch)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: load-json.py <filename.json> <port>")
        sys.exit(1)

    json_file, port = sys.argv[1], int(sys.argv[2])
    load_json(json_file, port)
