from cryptography.fernet import Fernet
import FileCryption as FileC
import KeyCryption as KeyC

# if its a new project uncomment the write process
# KeyC.writekey()
#  load the key 
key = KeyC.loadkey()

file_load ="Input file path here"

# encrypt the file 
# FileC.fileEncrypt(file_load,key)
# FileC.fileDecrypt(file_load,key)