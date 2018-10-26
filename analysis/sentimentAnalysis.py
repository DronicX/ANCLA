import tweepy #The Twitter API
from time import sleep
from datetime import datetime
from textblob import TextBlob #For Sentiment Analysis
import matplotlib.pyplot as plt #For Graphing the Data
from settingHandler import loadSettings
from writeFile import writeToFile

CONSUMER_KEY = '5bKnzZoSPFqdyxxqaQ5K3UswP'
CONSUMER_SECRET = 'L5jQ1a0Ya25aW6GRcMMrHpvrTSoRJGLp7vmA7nC9NeBVpaxIXX'
OAUTH_TOKEN = '1250454920-HsnOaMRoTz8LRNQrvBCqX2SA4y7XCPlU9YLxSmr'
OAUTH_TOKEN_SECRET = '0RdkK0PgrdGKQgJTObxkwa1Q5IgcmWCUU1MmcouaytVJY'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

def runSentimentAnalysis(keyword, tweetNumber = 100, backup = 10):
    tweetNumber = int(tweetNumber)

    polarity_list = []
    numbers_list = []
    number = 1
    settings = loadSettings()
    tweetJSON = {}
    tweetJSON['Tweets'] = []

    for tweet in tweepy.Cursor(api.search, keyword, lang="en").items(tweetNumber):
        try:

            analysis = TextBlob(tweet.text)
            analysis = analysis.sentiment
            polarity = analysis.polarity
            polarity_list.append(polarity)
            numbers_list.append(number)

            if settings["verbose"] == True:
                #Current count        
                print("Tweet: " + str(number))
                #Tweet text
                print(tweet.text)
                #Sentiment value
                print("Sentiment value: " + str(polarity) + "\n")

            
            tweetJSON['Tweets'].append({
                'tweet_id': tweet.id,
                'tweet_created': str(tweet.created_at),
                'text': tweet.text,
                'sentiment': polarity,
                'favorites': tweet.favorite_count,
                'retweets': tweet.retweet_count,
                'user_name': tweet.user.name,
                'user_handle': tweet.user.screen_name,
                'verified': tweet.user.verified,
                'followers': tweet.user.followers_count,
                'friends': tweet.user.friends_count,
                'user_likes': tweet.user.favourites_count,
                'user_tweets': tweet.user.statuses_count,
                'user_created': str(tweet.user.created_at)    
            })

            number = number + 1

            if number == number % backup if settings["datalog"] == True:
                writeToFile(tweetJSON, 'analyze-sentiment')

        except tweepy.TweepError as e:
            print(e.reason)
        
        except StopIteration:
            break

    if settings["datalog"] == True:
        writeToFile(tweetJSON, 'analyze-sentiment')
       
    #Here we define axes
    plt.figure(num=1)
    plt.ion()
    axes = plt.gca()
    axes.set_ylim([-1, 2])

    plt.scatter(numbers_list, polarity_list)

    #Here we calculate imporant info to show on a plt box
    averagePolarity = (sum(polarity_list))/(len(polarity_list))
    averagePolarity = "{0:.0f}%".format(averagePolarity * 100)
    time  = datetime.now().strftime("At: %H:%M\nOn: %m-%d-%y")
    plt.text(1, 1.25, "Average Sentiment:  " + str(averagePolarity) + "\n" + time, fontsize=12, bbox = dict(facecolor='none', edgecolor='black', boxstyle='square, pad = 1'))

    plt.title("Sentiment of " + keyword + " on Twitter") 
    plt.xlabel("Number of Tweets")
    plt.ylabel("Sentiment")

    while plt.fignum_exists(1):
        plt.show()
        plt.pause(0.0001)

    return tweetJSON
