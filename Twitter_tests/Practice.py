import twitter
import json

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.

CONSUMER_KEY = '5bKnzZoSPFqdyxxqaQ5K3UswP'
CONSUMER_SECRET = 'L5jQ1a0Ya25aW6GRcMMrHpvrTSoRJGLp7vmA7nC9NeBVpaxIXX'
OAUTH_TOKEN = '1250454920-HsnOaMRoTz8LRNQrvBCqX2SA4y7XCPlU9YLxSmr'
OAUTH_TOKEN_SECRET = '0RdkK0PgrdGKQgJTObxkwa1Q5IgcmWCUU1MmcouaytVJY'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
 CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable
print (twitter_api) #Object representation of Twitter API

##################### FIRST: TRENDS ##########################

# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.
world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID) # initiates an HTTP call to GET https://api.twitter.com/1.1/trends/place.json?id=1.
us_trends = twitter_api.trends.place(_id=US_WOE_ID)
#print (json.dumps(world_trends, indent=1))
#print()
#print (json.dumps(us_trends, indent=1))

#Use Python list comprehension to parse out the names of the trending
#topics from the queried results
world_trends_set = set([trend['name']
    for trend in world_trends[0]['trends']])
us_trends_set = set([trend['name']
    for trend in us_trends[0]['trends']])
common_trends = world_trends_set.intersection(us_trends_set)
print (common_trends)

##########################################################

################# SEARCH HASHTAG #########################

# XXX: Set this variable to a trending topic,
# or anything else for that matter. 
q = '#Charmed'
count = 100

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets
search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']
# Iterate through 5 more batches of results by following the cursor
for _ in range(5):
    print ("Length of statuses", len(statuses))
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError: # No more results when next_results doesn't exist
        break

    # Create a dictionary from next_results, which has the following form:
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

    # The use of *args and **kwargs (dictionary of key/value pairs) 
    # as parameters to a function is a Python idiom
    # fomr expressing arbitrary arguments and keyword arguments

# Show one sample search result by slicing the list...
#print (json.dumps(statuses[0], indent=1))

#################################################################

#################### ANALYZING 140 CHARACTERS ###################
t = statuses[0] #This represents a tweet
print(t['id'])
print(t['text'])
print(t['favorite_count'])
print(t['retweet_count'])
print(t['retweeted'])
print(json.dumps(t['entities'], indent=1))
# print(t['retweeted_status']) Doesn't work TODO: Check why it doesn't

################################################################
