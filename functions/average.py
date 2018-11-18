def average(data, action, specification, variable):
    if variable is not None:
        s = 0
        avg = 0
        for tweet in data["Tweets"]:
            s += tweet[variable]
        avg /= len(data["Tweets"])
        print("Average " + variable + ": " + str(avg))
    else:
        print("Average:")
        numbers = {}
        for tweet in data["Tweets"]:
            for variable in tweet:
                if type(variable) == int:
                    numbers[variable] += tweet[variable]

        print(numbers)
        for attr in numbers:
            print(attr + ": " + str(numbers[attr] / len(data["Tweets"])))
                    