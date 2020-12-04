from cryptography.fernet import Fernet



# Generates Key to be stored
def writeKey():
    """ Generates a Key and saves it""" 
    key =Fernet.generate_key()
    print(key)
    with open("key.key","wb") as key_file:
        key_file.write(key)

# Loads Encryption Key
def loadkey():
    """ Loads the key from the current directory"""
    return open("key.key","rb").read()
    