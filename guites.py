from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image


window=Tk()
#
def open():
    window.filename=filedialog.askopenfilename(initialdir=r"C:\Users\ASUS\Documents\TBAlgeo2\Algeo02-21072\dataset",title="Choose file",filetypes=(("jpg files","*.jpg"),("all files","*.*")))
    my_label=Label(window, text=window.filename).pack()
    my_image=ImageTk.PhotoImage(Image.open(window.filename))
    my_image_label=Label(image=my_image).pack()

button = Button(window,text="Open",command=open)
button.pack()
window.mainloop()