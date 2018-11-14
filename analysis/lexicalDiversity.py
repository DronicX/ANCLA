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
    try:
        tweets_text = get_tweets(text,int(count))       # List of the text in all the resulting tweets
        settings = loadSettings()                       # Instance of the settings
        lexicalValue_list = []                          # List of all the lexical diversity values calculated
        number_list = []                                # List of of all the number of tweets
        sum = 0                                         # Sum of all the lexical diversity values
        number = 1                                      # Counter of texts

        # For the text in a list of all the texts
        for text in tweets_text:
            words = []
            # For all the words in the text
            for w in text.split():
                words.append(w)
            lexicalValue = 1.0*len(set(words))/len(words)      # Calculate the lexical diversity
            lexicalValue_list.append(lexicalValue)
            sum += lexicalValue
            number_list.append(number)
            if settings["verbose"] == True:
                print("Lexical Diversity value from 0 to 1 is " + str(lexicalValue))
            number += 1
        if settings["verbose"] == True:
                print("The average lexical value is " + str(sum/len(lexicalValue_list)))

        # Scatter Plot of the data
        plt.xlabel("Number of Tweets")
        plt.ylabel("Lexical Diversity")
        plt.scatter(number_list, lexicalValue_list)
        plt.show
        
     except tweepy.TweepError as e:
            print(e.reason)

# Get tweets
def get_tweets(keyword, tweetNumber):
    statuses_text = [tweet.text for tweet in tweepy.Cursor(api.search, keyword,lang="en").items(tweetNumber)]
    return statuses_text
