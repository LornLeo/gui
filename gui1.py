from tkinter import *
root=Tk()
root.title('calculator')
root.geometry("500x500")
def add():
    total=int(numlentry.get())+int(num2lentry.get())
    lblresult.config(text=total)


lblnum1=Label(root,text="num1",fg="red",bg="yellow")
lblnum1.pack()

numlentry=Entry(root, fg="red",bg="yellow")
numlentry.pack()

lblnum2=Label(root,text="num2",fg="red",bg="yellow")
lblnum2.pack()

num2lentry=Entry(root, fg="red",bg="yellow")
num2lentry.pack()

btnadd=Button(root, text="+",fg="green",bg="pink",command=add)
btnadd.pack()

lblresult=Label(root,fg="red",bg="yellow")
lblresult.pack()

root.mainloop()