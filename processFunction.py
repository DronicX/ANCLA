import pickle
from settingHandler import *

def processFunction(data, function, action, specification, variable = None):
    if function == "tendencies":
        if action == "analyze":
            if specification == "sentiment":
                print("Tendencies not yet implemented. For now, here is the data:\n")
                if variable is not None:
                    print("Variable detected: " + variable + "\n")
                print(data)
                print("")

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