from tkinter import *
from tkinter.ttk import Combobox

window=Tk()
window.geometry('500x500')
window.title("Combo box")

combo=Combobox(window)
combo['values']=(1,2,3,4,5,"text")#adding items to the combo
combo.current(3)#setting selected items
combo.grid(row=0,column=0)

window.mainloop()