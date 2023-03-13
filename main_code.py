#IMPORT
from tkinter import *

#INICIJALIZACIJA

appWindow = Tk()
appWindow.geometry("300x150")
appWindow.title("PASSWORD MANAGER")
appWindow.configure(bg="#c7d1af")


def username_label():
    # username label and text entry box
    user_nameLabel = Label(appWindow, text="Username",bg="#bcbcbc").grid(row=0, column=0)
    user_name = StringVar()
    user_name_entry_box = Entry(appWindow,width='30',textvariable=user_name, bg="#bcbcbc").grid(row=0,column=1)


def password_first_time():
    #password label and text entry box
    passwordLabel = Label(appWindow, text ="Password",bg="#bcbcbc").grid(row=1, column=0)
    password = StringVar()
    password_entry_box = Entry(appWindow,width='30',textvariable=password, bg="#bcbcbc", show='*').grid(row=1, column = 1)

def password_second_time():
    #double_check_password label and text entry box
    double_check_passwordLabel = Label(appWindow, text="Re-enter",bg="#bcbcbc").grid(row=2,column=0)
    double_check_password = StringVar()
    double_check_password_entry_box = Entry(appWindow,width='30', textvariable=double_check_password, bg="#bcbcbc",show='*').grid(row=2, column=1)

def submit_button_logic():
    submit_button = Button(appWindow, text= "Submit", bd=3, activebackground="#3e6dbf").grid(row=4, column=0)
    pass




#POZIVANJE FUNKCIJA
username_label()
password_first_time()
password_second_time()
submit_button_logic()

appWindow.mainloop()