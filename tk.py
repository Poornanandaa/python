from tkinter import *
from pil import Image, ImageTk
root = Tk()
root.title('image') 
root.geometry('400x400')

upload - Image.open('image.png')
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, height=350, width=350)
label.place(x=50, y=0)
label2 = Label(root, text="his is the way to display an image in tkinter")
label2.place(x=40, y=360)
root.mainloop()