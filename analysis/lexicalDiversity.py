import tweepy #The Twitter API

CONSUMER_KEY = '5bKnzZoSPFqdyxxqaQ5K3UswP'
CONSUMER_SECRET = 'L5jQ1a0Ya25aW6GRcMMrHpvrTSoRJGLp7vmA7nC9NeBVpaxIXX'
OAUTH_TOKEN = '1250454920-HsnOaMRoTz8LRNQrvBCqX2SA4y7XCPlU9YLxSmr'
OAUTH_TOKEN_SECRET = '0RdkK0PgrdGKQgJTObxkwa1Q5IgcmWCUU1MmcouaytVJY'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

# A function for computing lexical diversity in the text of a set of tweets
def lexical_diversity(text, count=100):
    tokens = get_tweets(text,int(count))
    return 1.0*len(set(tokens))/len(tokens)

# Get tweets
def get_tweets(keyword, tweetNumber):
    status_text = [tweet.text for tweet in tweepy.Cursor(api.search, keyword,lang="en").items(tweetNumber)]
    words = [w for t in status_text for w in t.split()]
    return words
