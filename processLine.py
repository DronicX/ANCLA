from analysis.sentimentAnalysis import runSentimentAnalysis
from analysis.liveSentimentAnalysis import runLiveSentimentAnalysis


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