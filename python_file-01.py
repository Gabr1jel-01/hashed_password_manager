import random
from cryptography.fernet import Fernet

passlen = int(input("Enter how many characters: "))
s='''abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?
     abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ
     abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ
     abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ
    '''
password = "".join(random.sample(s,passlen ))

key = Fernet.generate_key()

fernet = Fernet(key)

encPassword = fernet.encrypt(password.encode())


print(password)
print(encPassword)


decPassword = fernet.decrypt(encPassword).decode()

print(decPassword)