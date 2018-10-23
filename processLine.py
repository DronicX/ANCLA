import pickle
from analysis.sentimentAnalysis import runSentimentAnalysis
from analysis.liveSentimentAnalysis import runLiveSentimentAnalysis
from settingHandler import *

def processLine(function, specification, parameter):
    if function == "analyze":
            if specification == "sentiment":
                if len(parameter) == 1:
                    runSentimentAnalysis(parameter[0])
                elif len(parameter) == 2:
                    runSentimentAnalysis(parameter[0], parameter[1])
                else:
                    runSentimentAnalysis(parameter[0], parameter[1], parameter[2])

    if function == "live":
        if specification == "sentiment":
            if len(parameter) == 1:
                runLiveSentimentAnalysis(parameter[0])
            elif len(parameter) == 2:
                runLiveSentimentAnalysis(parameter[0], parameter[1])
            elif len(parameter) == 3:
                runLiveSentimentAnalysis(parameter[0], parameter[1], parameter[2])
            else:
                runLiveSentimentAnalysis(parameter[0], parameter[1], parameter[2], parameter[3])

    if function == "config":
        true = ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']
        false = ['false', '0', 'f', 'n', 'no', 'nop', 'nope', 'mm']

        if specification == "datalog":
            settings = loadSettings()
            
            if (parameter[0].lower() in true or parameter[0].lower() in false):
                settings["datalog"] = parameter[0].lower() in true
            else:
                print("Please type true or false only to change datalog configuration")
            updateSettings(settings)

        if specification == "verbose":
            settings = loadSettings()
            if (parameter[0].lower() in true or parameter[0].lower() in false):
                settings["verbose"] = parameter[0].lower() in true
            else:
                print("Please type true or false only to change verbose configuration")
            updateSettings(settings)

    if function == "help":
        if specification == "function":
            #TO DO
            #Delete return None after finished here
            return None

        if specification == "config":
            #TO DO
            #Delete return None after finished here
            return None