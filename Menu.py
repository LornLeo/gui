from tkinter import *
def openFile():
    print("File has been opened")
def saveFile():
    print("File has been saved")
def cut():
    print("File has been cut")
def copy():
    print("you copied some text")
def paste():
    print("you pasted some text")



window=Tk()
window.geometry("500x500")
menubar=Menu(window)
window.config(menu=menubar)

fileMenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_separator()
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)
fileMenu.add_separator()

editMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_separator()
editMenu.add_command(label="Copy",command=copy)
editMenu.add_separator()
editMenu.add_command(label="Paste",command=paste)
editMenu.add_separator()

window.mainloop()