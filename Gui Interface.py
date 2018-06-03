
from tkinter import *


root=Tk()
topframe=Frame(root)
topframe.pack(side=TOP)
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)

button1= Button (topframe, Text="Login", fg="blue")
button2= Button (topframe, Text="Password", fg="blue")
button3= Button (bottomframe, Text="Submit", fg="red")

button1.pack()
button2.pack()
button3.pack()



root.mainloop()