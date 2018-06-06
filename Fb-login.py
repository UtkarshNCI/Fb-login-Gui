#https://github.com/RandomQWE 
#Gui Login app for facebook
#created by Utkarsh
import tkinter as tkk
from selenium import webdriver 
from time import sleep
from getpass import getpass
import os

text1=str       
text2=str


def clicked(*args):
    text1=entry1.get()
    text2=entry2.get()
    cli(text1,text2)


def cli(usr,pwd):
    cwd=os.getcwd()
    ok=os.path.join(cwd,'chromedriver.exe')
    driver=webdriver.Chrome(ok)
    driver.get("https://www.facebook.com/")
    print("Opened Facebook")
    sleep(1)

    username=driver.find_element_by_id('email')
    username.send_keys(usr)
    print("Username entered")
    sleep(1)

    password=driver.find_element_by_id('pass')
    password.send_keys(pwd) 
    print("Password entered")
    sleep(1)

    login_click=driver.find_element_by_id("loginbutton")
    login_click.click()


    print("All Done")
    input("if sucessfull input anything")
    driver.quit()
    print("Finished")        



root=tkk.Tk()
root.title("Login APP")
root.geometry("300x200")

label1=tkk.Label(text="Enter details",fg="Black",font=("Open Sans",10))
label1.grid(column=0,row=0)

button1=tkk.Label(text="Username",bg="black",fg="white",font=("Open Sans",10))
button1.grid(column=20,row=1)

entry1=tkk.Entry()
entry1.grid(column=21,row=1)

button2=tkk.Label(text="Password",bg="black",fg="white",font=("Open Sans",10))
button2.grid(column=20,row=2)

entry2=tkk.Entry(show="*")
entry2.grid(column=21,row=2)

button3=tkk.Button(text="Login",command=clicked)
button3.grid(column=20,row=3)
root.bind("<Return>", clicked)
root.bind("button3","<Button-1>",clicked)
root.mainloop()
