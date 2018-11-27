#This is our help-config file reader. The user may input 'help-config' wih or without a parameter
#In doing so, the proper text file with detailed information will be printed onto the console

def showSettings(fileName="help-setting"):
    try:
        with open("help/" + fileName + ".txt", 'r') as helpFile:
            for line in helpFile:
                print(line)
    except FileNotFoundError:
        print("Configuration setting you are trying to access doesn't exist.\n")
        print("Try calling help-setting without parameters to see a list of all available settings.")
