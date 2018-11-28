import time
import re
import json
import matplotlib.pyplot as plt
from textblob import TextBlob
from tweepy import Stream
from tweepy import API
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from settingHandler import loadSettings
from writeFile import writeToFile
from loadCreds import loadCreds

positive=0
negative=0
compound=0
initime=0
count=0
plt.ion()
settings = loadSettings()

tweetJSON = {}
tweetJSON['Tweets'] = []

def calctime(a):
    return time.time()-a

class listener(StreamListener):

    def __init__(self, count, maxTweets, maxTime, backup):
        self.count = count
        self.maxTweets = maxTweets
        self.maxTime = maxTime
        self.backup = backup

    def on_data(self,data):
        all_data=json.loads(data)
        tweet=all_data["text"]
        tweet=" ".join(re.findall("[a-zA-Z]+", tweet))
        blob=TextBlob(tweet.strip())

        global initime
        global positive
        global negative     
        global compound  
        global count
        global minusx
        global x
        global minusy
        global y
        
        count=count+1

        if count == 1:
            initime = time.time()

        t = int(calctime(initime)) 

        senti=0
        for sen in blob.sentences:
            senti=senti+sen.sentiment.polarity
            if sen.sentiment.polarity >= 0:
                positive=positive+sen.sentiment.polarity   
            else:
                negative=negative+sen.sentiment.polarity  

        compound=compound+senti

        if settings["verbose"] == True:
            #Time in seconds
            print("Time: " + str(t))
            #Current count        
            print("Tweet: " + str(count))
            #Tweet text
            print(tweet)
            #Sentiment value
            print("Sentiment value: " + str(senti) + "\n")
            #Sentiment values
            #print(str(positive) + ' ' + str(negative) + ' ' + str(compound))

        
        tweetJSON['Tweets'].append({
            'tweet_id': all_data['id'],
            'tweet_created': all_data['created_at'],
            'text': all_data['text'],
            'sentiment': senti,
            'favorites': all_data['favorite_count'],
            'retweets': all_data['retweet_count'],
            'replies': all_data['reply_count'],
            'user_name': all_data['user']['name'],
            'user_handle': all_data['user']['screen_name'],
            'verified': all_data['user']['verified'],
            'followers': all_data['user']['followers_count'],
            'friends': all_data['user']['friends_count'],
            'user_likes': all_data['user']['favourites_count'],
            'user_tweets': all_data['user']['statuses_count'],
            'user_created': all_data['user']['created_at']    
        })
        
        if count == 1:
            x = 70
            minusy = -20
            y = 20

        if count == count % int(self.backup) and settings["datalog"] == True:
            writeToFile(tweetJSON, 'live-sentiment')
        
        if t > x:
            x = t + 5
        if negative < minusy:
            minusy = negative - 5
        if positive > y:
            y = positive + 5

        if count == 1:
            minusx = t

        if not plt.fignum_exists(1) and count != 1:
            count = 0
            return False

        plt.axis([minusx, x, minusy,y])
        plt.title("Live Tweet Sentiment Analysis") 
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        plt.plot([t], [positive], 'bo', [t], [negative], 'ro', [t], [compound], 'mo')
        plt.figure(num=1)
        plt.pause(0.0001)

        if self.maxTweets != 0:
            if count==self.maxTweets:
                count = 0
                return False
            else:
                return True

        if self.maxTime != 0:
            if t >= self.maxTime:
                count = 0
                return False
            else:
                return True
        
    def on_error(self,status):
        print(status)

def runLiveSentimentAnalysis(keyword, maxTweets = 300, maxTime = 0, backup = 10):
    maxTweets = int(maxTweets)
    maxTime = int(maxTime)

    Creds = loadCreds()
    CONSUMER_KEY = Creds['CONSUMER_KEY']
    CONSUMER_SECRET = Creds['CONSUMER_SECRET']
    OAUTH_TOKEN = Creds['OAUTH_TOKEN']
    OAUTH_TOKEN_SECRET = Creds['OAUTH_TOKEN_SECRET']

    auth=OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

    api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5, retry_errors=5)
    
    twitterStream =  Stream(auth=api.auth, listener=listener(count, maxTweets, maxTime, backup))
    twitterStream.filter(track=[keyword])
    if settings["datalog"] == True:
        writeToFile(tweetJSON, 'live-sentiment')
        
    while plt.fignum_exists(1):
        plt.show()
        plt.pause(0.0001)
    return tweetJSON
  

if __name__ == '__main__':
    runLiveSentimentAnalysis("Donald Trump", 0, 5)