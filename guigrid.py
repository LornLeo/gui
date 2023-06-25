from tkinter import messagebox
from tkinter import *
root=Tk()
root.title('user details')
root.geometry("500x500")
def check():
    if int(wageentry.get())>=40000:
        messagebox.showinfo("Eligibility Status","You are eligible for a Credit Card")
    else:
        messagebox.showinfo("Eligibility Status","You are not eligible for a Credit Card")

lblun=Label(root,text="Name: ",font=('Arial 20'))
lblun.grid(row=0,column=0,pady=10)

lblage=Label(root,text="age: ",font=('Arial 20'))
lblage.grid(row=1,column=0,pady=10)

lblwages=Label(root,text="wages: ",font=('Arial 20'))
lblwages.grid(row=2,column=0,pady=10)

unentry=Entry(root,width=20,font=('Arial 15'))
unentry.grid(row=0,column=1,pady=10)

ageentry=Entry(root,width=20,font=('Arial 15'))
ageentry.grid(row=1,column=1,pady=10)

wageentry=Entry(root,width=20,font=('Arial 15'))
wageentry.grid(row=2,column=1,pady=10)

btnadd=Button(root,text="check",command=check)
btnadd.grid(row=2,column=2)

root.mainloop()