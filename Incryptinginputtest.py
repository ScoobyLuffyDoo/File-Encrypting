import incryptionMod as IncMod
from cryptography.fernet import Fernet
import base64

# IncMod.writeKey()
key =  IncMod.loadkey()

message = "this is my message to be encrypted"
# encoding the valye that needs to be incrypted
message = message.encode()
# using the key for the moduel
f = Fernet(key)
# begin encrypting the value
encrypted_value = f.encrypt(message)
print (encrypted_value)

# decrypt thev incrypted value
decrypted_value = f.decrypt(encrypted_value)