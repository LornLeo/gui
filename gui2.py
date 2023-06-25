from tkinter import messagebox
from tkinter import *
root=Tk()
root.geometry("500x500")
def add():
    if not e1.get():
        messagebox.showerror("error","please first number")
        return
    else:
        num1=int(e1.get())
    if not e2.get():
        messagebox.showerror("error","please enter second number")
        return
    else:
        num2=int(e2.get())
    result=num1+num2 
    lblresult.config(text=result)
def sub():
    if not e1.get():
        messagebox.showerror("error","please first number")
        return
    else:
        num1=int(e1.get())
    if not e2.get():
        messagebox.showerror("error","please enter second number")
        return
    else:
        num2=int(e2.get())
    result=num1-num2 
    lblresult.config(text=result)
def multiply():
    if not e1.get():
        messagebox.showerror("error","please first number")
        return
    else:
        num1=int(e1.get())
    if not e2.get():
        messagebox.showerror("error","please enter second number")
        return
    else:
        num2=int(e2.get())
    result=num1*num2 
    lblresult.config(text=result)

def div():
    if not e1.get():
        messagebox.showerror("error","please first number")
        return
    else:
        num1=int(e1.get())
    if not e2.get():
        messagebox.showerror("error","please enter second number")
        return
    else:
        num2=int(e2.get())
    result=num1/num2 
    lblresult.config(text=result)
    
lalel=Label(root,text="FirstNum")
lalel.pack()
e1=Entry(root)
e1.pack()

lale2=Label(root,text="SecondNum")
lale2.pack()
e2=Entry(root)
e2.pack()

lblresult=Label(root, text="", bg="yellow")
lblresult.pack()

btnadd=Button(root,text="add",command=add)
btnadd.pack()

btnadd=Button(root,text="subtract",command=sub)
btnadd.pack()

btnadd=Button(root,text="multiply",command=multiply)
btnadd.pack()

btnadd=Button(root,text="divide",command=div)
btnadd.pack()
root.mainloop()