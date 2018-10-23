#This is our help-function file reader

def showFunc(fileName="help-function"):
    with open("help/" + fileName + ".txt", 'r') as helpFile:
        for line in helpFile:
            print(line)