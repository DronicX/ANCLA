import tweepy #The Twitter API
from time import sleep
from datetime import datetime
from textblob import TextBlob #For Sentiment Analysis
import matplotlib.pyplot as plt #For Graphing the Data
from settingHandler import loadSettings
from writeFile import writeToFile
from loadCreds import loadCreds

Creds = loadCreds()
CONSUMER_KEY = Creds['CONSUMER_KEY']
CONSUMER_SECRET = Creds['CONSUMER_SECRET']
OAUTH_TOKEN = Creds['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = Creds['OAUTH_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

def getTweets(keyword, tweetNumber = 100, backup = 10):
    if backup == '0':
        backup = '1'

    tweetNumber = int(tweetNumber)

    number = 1
    settings = loadSettings()
    tweetJSON = {}
    tweetJSON['Tweets'] = []

    for tweet in tweepy.Cursor(api.search, keyword, lang="en").items(tweetNumber):
        try:

            if settings["verbose"] == True:
                #Current count        
                print("Tweet: " + str(number))
                #Tweet text
                print(tweet.text)
            
            tweetJSON['Tweets'].append({
                'tweet_id': tweet.id,
                'tweet_created': str(tweet.created_at),
                'text': tweet.text,
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

            if number == number % int(backup) and settings["datalog"] == True:
                writeToFile(tweetJSON, 'search-tweets')

        except tweepy.TweepError as e:
            print(e.reason)
        
        except StopIteration:
            break

    if settings["datalog"] == True:
        writeToFile(tweetJSON, 'search-tweets')
       
    return tweetJSON
