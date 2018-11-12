import pickle
from analysis.sentimentAnalysis import runSentimentAnalysis
from analysis.liveSentimentAnalysis import runLiveSentimentAnalysis
from settingHandler import *

#Our files
from help.functionHelp import showFunc

def processLine(action, specification, parameter):
    if action == "analyze":
            if specification == "sentiment":
                if len(parameter) == 1:
                    return runSentimentAnalysis(parameter[0])
                elif len(parameter) == 2:
                    return runSentimentAnalysis(parameter[0], parameter[1])
                else:
                    return runSentimentAnalysis(parameter[0], parameter[1], parameter[2])

    if action == "live":
        if specification == "sentiment":
            if len(parameter) == 1:
                return runLiveSentimentAnalysis(parameter[0])
            elif len(parameter) == 2:
                return runLiveSentimentAnalysis(parameter[0], parameter[1])
            elif len(parameter) == 3:
                return runLiveSentimentAnalysis(parameter[0], parameter[1], parameter[2])
            else:
                return runLiveSentimentAnalysis(parameter[0], parameter[1], parameter[2], parameter[3])

    if action == "config":
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

    if action == "help":
        if specification == "function":
            if len(parameter) == 0:
                showFunc()
            else:
                showFunc(parameter[0])

        if specification == "config":
            #TO DO
            #Delete return None after finished here
            return None
    if action == "help":
        if specification == "action":
            if len(parameter) == 0:
                showFunc()
            else:
                showFunc(parameter[0])