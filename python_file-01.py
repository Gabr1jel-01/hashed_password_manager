import random
from tkinter import *
from cryptography.fernet import Fernet
from functools import partial


def validateLogin(user_name, user_password):
    print("Username entered: ", user_name.get())
    print("Password entered: ", user_password.get())

appWindow = Tk()
appWindow.geometry("300150")
appWindow.title("Login")


user_nameLabel = Label



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