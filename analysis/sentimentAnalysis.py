import tweepy #The Twitter API
from time import sleep
from datetime import datetime
from textblob import TextBlob #For Sentiment Analysis
import matplotlib.pyplot as plt #For Graphing the Data

CONSUMER_KEY = '5bKnzZoSPFqdyxxqaQ5K3UswP'
CONSUMER_SECRET = 'L5jQ1a0Ya25aW6GRcMMrHpvrTSoRJGLp7vmA7nC9NeBVpaxIXX'
OAUTH_TOKEN = '1250454920-HsnOaMRoTz8LRNQrvBCqX2SA4y7XCPlU9YLxSmr'
OAUTH_TOKEN_SECRET = '0RdkK0PgrdGKQgJTObxkwa1Q5IgcmWCUU1MmcouaytVJY'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

#Print your user name
#user = api.me()
#print (user.name)

def runSentimentAnalysis(keyword, tweetNumber = 100):
    tweetNumber = int(tweetNumber)

    polarity_list = []
    numbers_list = []
    number = 1

    for tweet in tweepy.Cursor(api.search, keyword, lang="en").items(tweetNumber):
        try:
            analysis = TextBlob(tweet.text)
            analysis = analysis.sentiment
            polarity = analysis.polarity
            polarity_list.append(polarity)
            numbers_list.append(number)
            number = number + 1

        except tweepy.TweepError as e:
            print(e.reason)
        
        except StopIteration:
            break

    #Here we define axes
    axes = plt.gca()
    axes.set_ylim([-1, 2])

    plt.scatter(numbers_list, polarity_list)

    #Here we calculate imporant info to show on a plt box
    averagePolarity = (sum(polarity_list))/(len(polarity_list))
    averagePolarity = "{0:.0f}%".format(averagePolarity * 100)
    time  = datetime.now().strftime("At: %H:%M\nOn: %m-%d-%y")
    plt.text(0, 1.25, "Average Sentiment:  " + str(averagePolarity) + "\n" + time, fontsize=12, bbox = dict(facecolor='none', edgecolor='black', boxstyle='square, pad = 1'))

    plt.title("Sentiment of " + keyword + " on Twitter") 
    plt.xlabel("Number of Tweets")
    plt.ylabel("Sentiment")

    plt.show()