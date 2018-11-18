import tweepy
import numpy as np
import matplotlib.pyplot as plt
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

def runComptetitorAnalysis(usr, cmptr):
    settings = loadSettings()
    tweetJSON = {}
    tweetJSON['Tweets'] = []

    user = api.get_user(screen_name = usr)

    competitor = api.get_user(screen_name = cmptr)

    userVals = ["@" + user.screen_name, user.followers_count, user.statuses_count, user.favourites_count, user.friends_count]
    competitorVals = ["@" + competitor.screen_name, competitor.followers_count, competitor.statuses_count, competitor.favourites_count, competitor.friends_count]
    cat = ["User Handle: ", "Followers: ", "Tweets: ", "FavesGiven: ", "Friends: "]
    #userFollowers = (user.followers_count / (user.followers_count + competitor.followers_count)) * 100
    #competitorFollowers = (competitor.followers_count / (user.followers_count + competitor.followers_count)) * 100 
    
    #userTweets = (user.statuses_count / (user.statuses_count + competitor.statuses_count)) * 100
    #competitorTweets = (competitor.statuses_count / (user.statuses_count + competitor.statuses_count)) * 100 
    
    #userLikes = (user.favourites_count / (user.favourites_count + competitor.favourites_count)) * 100
    #competitorLikes = (competitor.favourites_count / (user.favourites_count + competitor.favourites_count)) * 100 
    
    #userFriends = (user.friends_count / (user.friends_count + competitor.friends_count)) * 100
    #competitorFriends = (competitor.friends_count / (user.friends_count + competitor.friends_count)) * 100 
    
    extra = 0
    for userV in userVals:
        if len(str(userV)) > extra:
            extra = len(str(userV))
    
    if extra < 4:
        extra = 0
    else:
        extra -= 4

    #print("User" + " " * extra + " Competitor")
    for userV, compV, c in zip(userVals, competitorVals, cat):
        print(c + str(userV) + " | " + str(compV))
    
    tweetJSON['Tweets'].append({
                'id': user.id,
                'created_at': str(user.created_at),
                'description': user.description,
                'user_name': user.name,
                'user_handle': user.screen_name,
                'verified': user.verified,
                'followers': user.followers_count,
                'friends': user.friends_count,
                'likes': user.favourites_count,
                'tweets': user.statuses_count,
            })

    tweetJSON['Tweets'].append({
                'id': competitor.id,
                'created_at': str(competitor.created_at),
                'description': competitor.description,
                'user_name': competitor.name,
                'user_handle': competitor.screen_name,
                'verified': competitor.verified,
                'followers': competitor.followers_count,
                'friends': competitor.friends_count,
                'likes': competitor.favourites_count,
                'tweets': competitor.statuses_count,
            })

    '''
    N = 4
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27       # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)

    userPercents = [userFollowers, userTweets, userLikes, userFriends]
    rects1 = ax.bar(ind, userPercents, width, color='b')
    competitorPercents = [competitorFollowers, competitorTweets, competitorLikes, competitorFriends]
    rects2 = ax.bar(ind+width, competitorPercents, width, color='r')

    ax.set_ylabel('Percentage')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( ('Followers', 'Tweets', 'Likes', 'Friends') )
    ax.legend( (rects1[0], rects2[0]), (usr, cmptr) )

    print(userVals)
    print(userPercents)

    def autolabel(rects, vals):
        for rect, val in zip(rects, vals):
            print(val)
            h = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, val,
                    ha='center', va='bottom')

    autolabel(rects1, userVals)
    autolabel(rects2, competitorVals)

    plt.show()
    '''

    if settings["datalog"] == True:
        writeToFile(tweetJSON, 'analyze-sentiment')

    return tweetJSON
    

