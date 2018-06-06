from selenium import webdriver 
from time import sleep
from getpass import getpass
import os
import tkinter as tkk


usr1=tkk.StringVar()
pwd1=tkk.Stringvar()

def cli(entry1,entry2):
     usr=entry1.get()
     pwd=entry2.get()
     driver=webdriver.Chrome("C:/Users/Utkarsh/Downloads/chromedriver_win32/chromedriver.exe")
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


class gui:
    def __init__ (self):
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
        
         button3=ttk.Button(window,text='Click me',command=self.clicked)
		 
		 
         window.bind("<Return>",self.clicked)

         root.mainloop() 
    
    def clicked (self, event) :
    	 text=self.entry1.get() 
		 text2=self.entry2.get()
		 


gui()