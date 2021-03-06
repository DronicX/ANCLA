import pickle
from settingHandler import *
from functions.printData import printData
from functions.average import average

def processFunction(data, function, action, specification, variable = None):
    if function == "print":
        printData(data, action, specification, variable)
    
    if function == "average":
        average(data, action, specification, variable)
        """if action == "analyze":
            if specification == "sentiment":
                #Temp code on how to do an analysis. THis will be moved to another file
                s = 0.0
                r = 0.0
                for tweet in data["Tweets"]:
                    s += tweet["favorites"]
                    r += tweet["retweets"]
                s /= len(data["Tweets"])
                r /= len(data["Tweets"])

                print("Average likes: " + str(s))
                print("Average retweets: " + str(r))

                if variable is not None:
                    for tweet in data["Tweets"]:
                        print(tweet[variable])
        
        if action == "live":
            if specification == "sentiment":
                #Temp code on how to do an analysis. THis will be moved to another file
                s = 0.0
                for tweet in data["Tweets"]:
                    s += tweet["favorites"]
                s /= len(data["Tweets"])

                print("Average likes: " + str(s))

                if variable is not None:
                    for tweet in data["Tweets"]:
                        print(tweet[variable])
        """