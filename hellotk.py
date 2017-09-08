from tkinter import *

from tkinter import messagebox

root = Tk()

root.title("test")
root.geometry("300x300")

import sys

app = Frame(root)
app.grid()
button1 = Button(app, text = " exit " , width=2, command=sys.exit)
button1.grid(padx=110, pady=80)

def dialog():
    var = messagebox.showinfo("test" , "hello, world")

button2 = Button(app, text = " hello! " , width=4, command=dialog)
button2.grid()

app.pack()
root.mainloop()