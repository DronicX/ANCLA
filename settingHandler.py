import pickle

def loadSettings():
    try:
        with open('settings', 'rb') as f:  
            return pickle.load(f)
    
    except FileNotFoundError:
        settings = {"datalog": False, "verbose": True}
        updateSettings(settings)
        return settings

def updateSettings(settings):
    with open('settings', 'wb+') as f:
        pickle.dump(settings, f, protocol=-1)