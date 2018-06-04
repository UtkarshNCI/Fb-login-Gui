from selenium import webdriver 
from time import sleep
from getpass import getpass
import os
import tkinter as tkk

text=str    
text2=str

class gui:
    root=tkk.Tk()
    root.title("Login APP")
    root.geometry("400x400")

    label1=tkk.Label(text="Enter details",fg="Black",font=("Open Sans",10))
    label1.grid(column=0,row=0)

    button1=tkk.Label(text="Username",bg="black",fg="white",font=("Open Sans",10))
    button1.grid(column=20,row=1)

    entry1=tkk.Entry(textvariable=usr1)
    entry1.grid(column=21,row=1)


    button2=tkk.Label(text="Password",bg="black",fg="white",font=("Open Sans",10))
    button2.grid(column=20,row=2)

    entry2=tkk.Entry(show="*",textvariable=pwd1)
    entry2.grid(column=21,row=2)
        
    button3=ttk.Button(window,text='Click me',command=clicked)
		 
		 
    window.bind("<Return>",clicked)

    root.mainloop() 
    
    def clicked () :
    	text=entry1.get() 
		text2=entry2.get()