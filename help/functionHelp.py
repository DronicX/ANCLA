#This is our help-function file reader. The user may input 'help-function' wih or without a parameter
#In doing so, the proper text file with detailed information will be printed onto the console

def function_showFunc(fileName="help-function"):
    try:
        with open("help/" + fileName + ".txt", 'r') as helpFile:
            for line in helpFile:
                print(line)
    except FileNotFoundError:
        print("function doesn't exist.\nTry calling help-function without parameters to see a list of all available functions.")