
from tkinter import *


root=Tk()
root.title("Login APP")
root.geometry("400x400")

label1=Label(text="Enter details")
label1.grid(column=0,row=0)

button1=Label(text="Username")
button1.grid(column=20,row=1)
entry1=Entry()
entry1.grid(column=21,row=1)

button2=Label(text="Password")
button2.grid(column=20,row=2)
entry2=Entry()
entry2.grid(column=21,row=2)

button3=Button(text="Login")
button3.grid(column=20,row=3)








root.mainloop()