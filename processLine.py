import pickle
from analysis.sentimentAnalysis import runSentimentAnalysis
from analysis.liveSentimentAnalysis import runLiveSentimentAnalysis
from settingHandler import updateSettings
from settingHandler import *

def processLine(function, specification, parameter):
    if function == "analyze":
            if specification == "sentiment":
                if len(parameter) == 1:
                    runSentimentAnalysis(parameter[0])
                else:
                    runSentimentAnalysis(parameter[0], parameter[1])

    if function == "live":
        if specification == "sentiment":
            if len(parameter) == 1:
                runLiveSentimentAnalysis(parameter[0])
            elif len(parameter) == 2:
                runLiveSentimentAnalysis(parameter[0], parameter[1])
            else:
                runLiveSentimentAnalysis(parameter[0], parameter[1], parameter[2])

    if function == "config":
        if specification == "datalog":
            settings = loadSettings()
            if (parameter[0].lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh'] or parameter[0].lower() in ['false', '0', 'f', 'n', 'no', 'nop', 'nope', 'mm']):
                settings["datalog"] = parameter[0].lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']
            else:
                print("Please type true or false only to change datalog configuration")
            updateSettings(settings)
        
        if specification == "verbose":
            settings = loadSettings()
            if (parameter[0].lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh'] or parameter[0].lower() in ['false', '0', 'f', 'n', 'no', 'nop', 'nope', 'mm']):
                settings["verbose"] = parameter[0].lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']
            else:
                print("Please type true or false only to change verbose configuration")
            updateSettings(settings)

            