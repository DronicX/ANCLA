import pickle

def loadSettings():
    try:
        with open('data/settings', 'rb') as f:  
            return pickle.load(f)
    
    except FileNotFoundError:
        settings = {"datalog": False, "verbose": True}
        updateSettings(settings)
        return settings

def updateSettings(settings):
    with open('data/settings', 'wb+') as f:
        pickle.dump(settings, f, protocol=-1)