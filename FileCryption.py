from cryptography.fernet import Fernet
import binascii
def fileEncrypt(filename,key):
    f = Fernet(key)
    # read the fiels binary data
    with open(filename,"rb") as file :
        file_data = file.read()
        file.close()
    # encrypt the files Data
    encrypted_file_data = f.encrypt(file_data)
    # write the new ecryptin binary 
    print("data encrypted")

    with open(filename,"wb") as file :
        file.write(encrypted_file_data)
        file.close()
    print("file encrypted")



def fileDecrypt(filename,key):
    f = Fernet(key)
    with open(filename,"rb") as file :
        # read the encrypted files binary Data
        encrypted_file_data = file.read()
        file.close()
        print("data decrypted")
    # decrypt the file
    decrypted_file_data = f.decrypt(encrypted_file_data)
    # write the original file data
    with open(filename,"wb") as file:
        file.write(decrypted_file_data)
        file.close()
        print("file decrypted")