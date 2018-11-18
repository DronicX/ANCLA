import pickle

def loadCreds():
    try:
        with open('TwitterAPICreds', 'rb') as f:  
            return pickle.load(f)
    
    except FileNotFoundError:
        print("Unable to load Twitter API Credentials! :(")