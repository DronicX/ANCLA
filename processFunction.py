import pickle
from analysis.sentimentAnalysis import runSentimentAnalysis
from analysis.liveSentimentAnalysis import runLiveSentimentAnalysis
from settingHandler import *

def processFunction(data, function, action, specification):
    if function == "tendencies":
        if action == "analyze":
            if specification == "sentiment":
                print("Tendencies not yet implemented. For now, here is the data:\n")
                print(data)
                print("")

        if action == "live":
            if specification == "sentiment":
                print("Tendencies not yet implemented. For now, here is the data:\n")
                print(data)
                print("")