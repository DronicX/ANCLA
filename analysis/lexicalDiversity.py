import tweepy #The Twitter API
from loadCreds import loadCreds

Creds = loadCreds()
CONSUMER_KEY = Creds['CONSUMER_KEY']
CONSUMER_SECRET = Creds['CONSUMER_SECRET']
OAUTH_TOKEN = Creds['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = Creds['OAUTH_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

# A function for computing lexical diversity in the text of a set of tweets
def lexical_diversity(text, count=100):
    tokens = get_tweets(text,int(count))
    print(tokens)
    return 1.0*len(set(tokens))/len(tokens)

# Get tweets
def get_tweets(keyword, tweetNumber):
    status_text = [tweet.text for tweet in tweepy.Cursor(api.search, keyword,lang="en").items(tweetNumber)]
    words = [w for t in status_text for w in t.split()]
    return words
