import random
from tkinter import *
from cryptography.fernet import Fernet
from functools import partial


def validateLogin(user_name, user_password):
    print("Username entered: ", user_name.get())
    print("Password entered: ", user_password.get())

appWindow = Tk()
appWindow.geometry("300x150")
appWindow.title("Login")
appWindow.configure(bg="#c7d1af")

# username label and text entry box
user_nameLabel = Label(appWindow, text="Username",bg="#bcbcbc").grid(row=0, column=0)
user_name = StringVar()
user_name_entry_box = Entry(appWindow,textvariable=user_name, bg="#bcbcbc").grid(row=0,column=1)

#password label and text entry box
passwordLabel = Label(appWindow, text ="Password",bg="#bcbcbc").grid(row=1, column=0)
password = StringVar()
password_entry_box = Entry(appWindow,textvariable=password, bg="#bcbcbc").grid(row=1, column = 1)

#double_check_password label and text entry box
double_check_passwordLabel = Label(appWindow, text="Re-enter",bg="#bcbcbc").grid(row=2,column=0)
double_check_password = StringVar()
double_check_password_entry_box = Entry(appWindow, textvariable=double_check_password, bg="#bcbcbc").grid(row=2, column=1)

def window_after_submit():
    
    pass



#submit button

submit_button = Button(appWindow, text= "Submit", bd=3, activebackground="#3e6dbf").grid(row=4, column=0)




"""
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


"""
appWindow.mainloop()