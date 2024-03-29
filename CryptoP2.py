from cryptography.fernet import Fernet, MultiFernet
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

filePtr = open('file.txt', 'w')
filePtr.write("SECRET MESSAGE \n SUPER SECRET MESSAGE")
filePtr.close()

def encrypt():

    fileName = input("Please Enter File Name (file.txt): ")
    try:
        file = open(fileName, 'r')
        FILECONTENTS = file.read()
        file.close()
    except:
        print("Error Opening File")

    try:
        password = (input("Please Enter Password for Encryption: ")).encode('utf-8')
        salt = b"salt"
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=480000,)
        key2 = base64.urlsafe_b64encode(kdf.derive(password))
        f = Fernet(key2)
        token = f.encrypt(FILECONTENTS.encode('utf-8'))

        print("Token \n",token, "\n")
        return(token)

    except:
        print("Error Encrypting")

def decrypt(token):

    try:
        password = (input("Please Enter Password for Decryption: ")).encode('utf-8')
        salt = b"salt"
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=480000,)
        key2 = base64.urlsafe_b64encode(kdf.derive(password))
        f = Fernet(key2)

        return(f.decrypt(token).decode('utf-8'))
    
    except:
        print("Incorrect Password")

print("\n" + decrypt(encrypt()))
