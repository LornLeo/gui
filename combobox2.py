from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window=Tk()
window.geometry('500x500')
window.title("Combo box")
window.resizable(0,0)

frame=Frame(window)
frame.pack()

def confirm():
    if combo.get()=="Pick an Options":
        messagebox.showerror("Error","Please choose a subject")
    else:    
        messagebox.showinfo("Your option","You choose {} as your subject.".format(combo.get()))

options=['Maths','Calculus','Trignometry',"Chemistry","Physics"]
combo=ttk.Combobox(frame,state="readonly",value=options)
combo.set("Pick an Options")
combo.grid(row=0,column=0)

btnadd=Button(frame,text="check",command=confirm)
btnadd.grid(row=2,column=2)

window.mainloop()