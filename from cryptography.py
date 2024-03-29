from cryptography.fernet import Fernet, MultiFernet
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = b"password"
salt = b"salt"
#key1 = Fernet(Fernet.generate_key())
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=480000,)
key2 = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key2)
token = f.encrypt(b"Secret message!")

print(f.decrypt(token))


#key3 = Fernet(Fernet.generate_key())
#f2 = MultiFernet([key3, key1, key2])
#rotated = f2.rotate(token)
#f2.decrypt(rotated)
