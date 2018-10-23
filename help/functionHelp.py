#This is our help-function file reader. The user may input 'help-function' wih or without a parameter
#In doing so, the proper text file with detailed informtion will be printed onto the console

def showFunc(fileName="help-function"):
    try:
        with open("help/" + fileName + ".txt", 'r') as helpFile:
            for line in helpFile:
                print(line)
    except FileNotFoundError:
        print("Function doesn't exist.\nTry calling help-function without parameters to see a list of all available functions.")
