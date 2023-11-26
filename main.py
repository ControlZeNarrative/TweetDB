import sys
import functions.py
import load-json.py

def main_menu():
    print("Welcome to your twitchat homepage! What would you like to do?: ")
    print("1. Search tweets")
    print("2. Search users")
    print("3. List top tweets")
    print("4. List most followed users")
    print("5. Compose a tweet")
    print("6. Exit")

    while True:
        option = input("> ")
        if option.isdigit() and 1 <= int(option) <= 6:
            break
        else:
            print("Invalid option selected! Please enter a number between 1 and 5.")
    return int(option)

def correct_input(usr_input: str, a: int, b: int):
    if usr_input.isdigit():
        uinput = int(uinput)
    else:
        return 0
    
    if (uinput >= a and uinput <= b) or uinput == 0:
        return 1
    return 0

def display_tweets(keywords: tuple):
    tweets = {}#search_tweets(keywords, collection)
    i = 0
    for tweet in tweets:
        i += 1
        #print(f"{i}. id: {tweet["id"]}, Date: {tweet["date"]}, Username: {tweet["user"]["username"]}\nTweet Content: {tweet["content"]}")
    
    #If there is at least one tweet that matches the keywords, give the user the option to select one
    if i != 0:
        answer = input("Select a tweet to see more info about it or enter 0 to return to main menu: ")
        while correct_input(answer, 1, i) != 1:
            answer = input(f"Please enter a number between 0 and {i}: ")

        #Print all fields
        if answer != 0:
            for j, tweet in enumerate(tweets, start=1):
                if answer == j:
                    for key, value in tweet.items():
                        print(f"{key}: {value}")
                    print(" ")
                    return
    else:
        print("No such tweets")
    return

def display_users(keyword: str):
    users = {}#search_users(keyword, collection)
    i = 0
    for user in users:
        i += 1
        #print(f"{i}. Username: {user["username"]}, Display name: {user["displayname"]}, Location: {user["location"]}")
    
    #If there is at least one user that matches the keyword, give the option to select them
    if i != 0:
        answer = input("Select a user to see more info on them or enter 0 to return to main menu: ")
        while correct_input(answer, 1, i) != 1:
            answer = input(f"Please enter a number between 0 and {i}: ")

        answer = int(answer)
        #Print all fields
        if answer != 0:
            for j, user in enumerate(users, start=1):
                if answer == j:
                    for key, value in user.items():
                        print(f"{key}: {value}")
                    print(" ")
                    return
    else:
        print("No such user")

    return

def display_top_tweets(n: int, count: str):
    tweets = {}#top_tweets(n, count)
    i = 0
    for tweet in tweets:
        i += 1
        #print(f"{i}. ID: {tweet["id"]}, Date: {tweet["date"]}, Username: {tweet["username"]}\nTweet Content: {tweet["content"]}")

    if i != 0: 
        answer = input("Select a tweet to see more info or enter 0 to go back to the main screen: ")
        while (correct_input(answer, 1, i) != 1):
            print("Invalid input")
            answer = input("Select a tweet to see more info or enter 0 to go back to the main screen: ")

        answer = int(answer)
        #Print all fields
        if answer != 0:
            for j, tweet in enumerate(tweets, start=1):
                if answer == j:
                    for key, value in tweet.items():
                        print(f"{key}: {value}")
                    print(" ")
                    return
    else:
        print("No such tweets")
    
    return

def display_top_users(n: int):
    users = {}#top_users(n)
    i = 1
    for user in users:
        #print(f"{i}. Username: {user["username"]}, Display name: {user["displayname"]}, Location: {user["location"]}")
        i += 1
    answer = input("Select a user to see more info or enter 0 to go back to the main screen: ")
    while (correct_input(answer, 1, i) != 1):
        print("Invalid input")
        answer = input("Select a user to see more info or enter 0 to go back to the main screen: ")
    
    answer = int(answer)
    #Print all fields
    if answer != 0:
        for j, user in enumerate(users, start=1):
            if answer == j:
                for key, value in user.items():
                    print(f"{key}: {value}")
                print(" ")
                return
    else:
        print("No such user")
    
    return

def main():
    if len(sys.argv) != 3:
        print("Usage: load-json.py <filename.json> <port>")
        sys.exit(1)

    json_file, port = sys.argv[1], int(sys.argv[2])
    load_json(json_file, port)


    command = main_menu()
    while (command):
        if command == 1:
            keywords = input("Enter keywords to search for in tweets: ")
            # Check that the input is not whitespace or empty
            while not any(char.isalpha() or char.isdigit() for char in keywords):
                keywords = input("Enter keywords to search for in tweets: ")
            keywords = keywords.split(" ")

            # Display the tweets that match at least one of the keywords
            display_tweets(tuple(keywords))
        elif command == 2:
            keyword = input("Enter a keyword to search for in users: ")
            # Check that the input is not empty or whitespaces
            while not any(char.isalpha() or char.isdigit() for char in keyword):
                keyword = input("Enter a keyword to search for in users: ")

            display_users(keyword)
        elif command == 3:
            n = input("Enter the Top 'n' tweets you wish to see: ")
            # Check that the input is not whitespace or empty
            while not n.isdigit() and int(n) < 1:
                n = input("Enter the Top 'n' tweets you wish to see: ")
            n = int(n)

            print(f"Do you wish to see the top {n} tweets based on retweetCount, likeCount, or quoteCount?")
            count = input("Enter r, l, or q for retweet, like, or quote counts respectively")
            while count.islower() not in ["r", "l", "q"]:
                count = input("Enter r, l, or q for retweet, like, or quote counts respectively")
            

            # Display the tweets that match at least one of the keywords
            display_top_tweets(n, count)
        elif command == 4:
            n = input("Enter the Top 'n' users you wish to see: ")
            # Check that the input is not whitespace or empty
            while not n.isdigit() and int(n) < 1:
                n = input("Enter the Top 'n' users you wish to see: ")
            n = int(n)

            display_top_users(n)
        elif command == 5:
            text = input("Please enter the text of your tweet: ")
            #functions.compose_tweet(text)
            print("You've posted a tweet.\n")
        else:
            break
        command = main_menu()
    print("Exiting...\n")
    return 0

if __name__ == "__main__":
    main()