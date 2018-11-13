import tweepy #The Twitter API
import matplotlib.pyplot as plt #For Graphing the Data
from settingHandler import loadSettings

CONSUMER_KEY = '5bKnzZoSPFqdyxxqaQ5K3UswP'
CONSUMER_SECRET = 'L5jQ1a0Ya25aW6GRcMMrHpvrTSoRJGLp7vmA7nC9NeBVpaxIXX'
OAUTH_TOKEN = '1250454920-HsnOaMRoTz8LRNQrvBCqX2SA4y7XCPlU9YLxSmr'
OAUTH_TOKEN_SECRET = '0RdkK0PgrdGKQgJTObxkwa1Q5IgcmWCUU1MmcouaytVJY'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

# A function for computing lexical diversity in the text of a set of tweets
def lexical_diversity(text, count=100):
    tweets_text = get_tweets(text,int(count))
    settings = loadSettings()
    lexicalValue_list = []
    number_list = []
    average = 0
    number = 1

    for text in tweets_text:
        words = []
        for w in text.split():
            words.append(w)
        lexicalValue = 1.0*len(set(words))/len(words)
        lexicalValue_list.append(lexicalValue)
        average += lexicalValue
        number_list.append(number)
        if settings["verbose"] == True:
            print("Lexical Diversity value from 0 to 1 is " + str(lexicalValue))
        number += 1
    if settings["verbose"] == True:
            print("The average lexical value is " + str(average/len(lexicalValue_list)))

    # Scatter Plot of the data
    plt.xlabel("Number of Tweets")
    plt.ylabel("Lexical Diversity")
    plt.scatter(number_list, lexicalValue_list)
    plt.show

# Get tweets
def get_tweets(keyword, tweetNumber):
    statuses_text = [tweet.text for tweet in tweepy.Cursor(api.search, keyword,lang="en").items(tweetNumber)]
    return statuses_text
