#This is our help-action file reader. The user may input 'help-action' wih or without a parameter
#In doing so, the proper text file with detailed information will be printed onto the console

def showFunc(fileName="help-action"):
    try:
        with open("help/" + fileName + ".txt", 'r') as helpFile:
            for line in helpFile:
                print(line)
    except FileNotFoundError:
        print("Action doesn't exist.\nTry calling help-action without parameters to see a list of all available actions.")
