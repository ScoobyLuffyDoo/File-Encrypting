from cryptography.fernet import Fernet

def writeKey():
    """ Generates a Key and saves it""" 
    key =Fernet.generate_key()
    print(key)
    with open("key.key","wb") as key_file:
        key_file.write(key)


def loadkey():
    """ Loads the key from the current directory"""
    return open("key.key","rb").read()