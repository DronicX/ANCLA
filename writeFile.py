import json
import time
from datetime import datetime
from settingHandler import loadSettings

def writeToFile(data, folder):
    settings = loadSettings()
    if settings['datalog'] == True:
        name = str(datetime.today().strftime('%d-%m-%Y')) + "_" + str(time.strftime("%Hh-%Mm-%Ss"))+ ".json"
        with open("data/" + folder + "/" + name, 'w') as outfile:
            json.dump(data, outfile, indent=4)