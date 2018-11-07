def printData(data, action, specification, variable = None):
    if variable is not None:
        for tweet in data["Tweets"]:
            print(tweet[variable])
    else:
        print(data["Tweets"])