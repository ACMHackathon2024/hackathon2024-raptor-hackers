from cryptography.fernet import Fernet, MultiFernet
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

filePtr = open('file.txt', 'w')
filePtr.write("MY SECRET MESSAGE")
filePtr.close()

def encrypt():

    fileName = input("Please Enter File Name (file.txt): ")
    file = open(fileName, 'r')
    FILECONTENTS = file.read()
    file.close()

    try:
        pswd = input("Please Enter Password for Encryption: ")
        password = pswd.encode('utf-8')
        salt = b"salt"
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=480000,)
        key2 = base64.urlsafe_b64encode(kdf.derive(password))
        f = Fernet(key2)
        token = f.encrypt(FILECONTENTS.encode('utf-8'))

        print("Token: " + token)
        return(token)

    except:
        print("Error Encrypting")

def decrypt(token):

    try:
        pswd = input("Please Enter Password for Encryption: ")
        password = pswd.encode('utf-8')
        salt = b"salt"
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=480000,)
        key2 = base64.urlsafe_b64encode(kdf.derive(password))
        f = Fernet(key2)

        return(f.decrypt(token).decode('utf-8'))
    
    except:
        print("Incorrect Password")

print(decrypt(encrypt()))
