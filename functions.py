import json
import sys
from datetime import datetime
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

    # Printing

    return results

def search_users(keyword: str, db: str):

    collection = db['users']

    # Matching users whose displayname or location contains the keyword
    query = {'$or': [{'displayname': {'$regex': keyword, '$options': 'i'}}, {'location': {'$regex': keyword, '$options': 'i'}}]}

    results = collection.find(query)

    # Listing the users
    users = []
    for user in results:
        if not any(u['username'] == user['username'] for u in users):
            # Add the user to the list
            users.append({
                'username': user['username'],
                'displayname': user['displayname'],
                'location': user['location']
            })

    return users

def top_tweets(n: int, count: str, db: str):
    
    collection = db['tweets']

    # Retrieving the top n tweets based on the specified field
    query = collection.find().sort([(count, -1)]).limit(n)

    # Create a list of tweets
    tweets = []
    for tweet in query:
        tweets.append({
            'id': tweet['id'],
            'date': tweet['date'],
            'content': tweet['content'],
            'username': tweet['username']
        })

    return tweets

def top_users(n: int, db: str):
    
    collection = db['users']

    # Getting the top n users based on the 'followersCount' field
    query = collection.find().sort([('followersCount', -1)]).limit(n)

    # Create a list of users
    users = []
    for user in query:
        # Check if the user is already in the list
        if not any(u['username'] == user['username'] for u in users):
            # Add the user to the list
            users.append({
                'username': user['username'],
                'displayname': user['displayname'],
                'followersCount': user['followersCount']
            })

    return users

def compose_tweet(content: str, db: str):
   
    collection = db['tweets']

    # Creating a new tweet format
    tweet = {
        'content': content,
        'date': datetime.now(),
        'username': '291user',
        'retweetCount': None,
        'likeCount': None,
        'quoteCount': None,
        # Add other fields as needed
    }

    # Inserting the tweet into the database
    collection.insert_one(tweet)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: <script>.py <keyword1> <keyword2> ... <keywordN>")
        sys.exit(1)

    keywords = sys.argv[1:]
    search_tweets(keywords)
