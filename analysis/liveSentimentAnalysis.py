import time
from tweepy import Stream
from tweepy import API
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import re

positive=0
negative=0
compound=0
initime=0
count=0
plt.ion()

def calctime(a):
    return time.time()-a

class listener(StreamListener):

    def __init__(self, count, maxTweets, maxTime):
        self.count = count
        self.maxTweets = maxTweets
        self.maxTime = maxTime

    def on_data(self,data):
        all_data=json.loads(data)
        tweet=all_data["text"]
        #username=all_data["user"]["screen_name"]
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

        #Time in seconds
        print("Time: " + str(t))
        #Current count        
        print("Tweet: " + str(count))
        #Tweet text
        #print(tweet.strip())
        #Sentiment value
        print("Sentiment value: " + str(senti) + "\n")
        #Sentiment values
        #print(str(positive) + ' ' + str(negative) + ' ' + str(compound))
        
        if count == 1:
            x = 70
            minusy = -20
            y = 20
        
        if t > x:
            x = t + 5
        if negative < minusy:
            minusy = negative - 5
        if positive > y:
            y = positive + 5

        if count == 1:
            minusx = t

        if not plt.fignum_exists(1) and count != 1:
            plt.close()
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
                plt.close()
                count = 0
                return False
            else:
                return True

        if self.maxTime != 0:
            if t >= self.maxTime:
                plt.close()
                count = 0
                return False
            else:
                return True
        
    def on_error(self,status):
        print(status)

def runLiveSentimentAnalysis(keyword, maxTweets = 300, maxTime = 0):
    maxTweets = int(maxTweets)
    maxTime = int(maxTime)

    CONSUMER_KEY = '5bKnzZoSPFqdyxxqaQ5K3UswP'
    CONSUMER_SECRET = 'L5jQ1a0Ya25aW6GRcMMrHpvrTSoRJGLp7vmA7nC9NeBVpaxIXX'
    OAUTH_TOKEN = '1250454920-HsnOaMRoTz8LRNQrvBCqX2SA4y7XCPlU9YLxSmr'
    OAUTH_TOKEN_SECRET = '0RdkK0PgrdGKQgJTObxkwa1Q5IgcmWCUU1MmcouaytVJY'

    auth=OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

    api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5, retry_errors=5)
    
    twitterStream =  Stream(auth=api.auth, listener=listener(count, maxTweets, maxTime))
    twitterStream.filter(track=[keyword])

if __name__ == '__main__':
    runLiveSentimentAnalysis("Donald Trump", 0, 5)