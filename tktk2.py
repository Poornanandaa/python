from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Alert", "This is a warning message, Virus is found")
button = Button(root, text="Scanning for virus", command=msg)    
button.place(x=40, y=80)
root.mainloop()