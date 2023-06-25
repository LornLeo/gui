from tkinter import*
from tkinter import messagebox
window=Tk()
window.title("Radio Button Application")
window.geometry("300x300")

def show():
    if option.get()==1:
        messagebox.showinfo("Python","Python is created by Guido van Rossum\n1.Simple and easy to learn\n2.Versatile\n3.Large standard library")
    elif option.get()==2:
        messagebox.showinfo("Java","Java is created by James Gosling\n1.Platform independence\n2.Object-oriented programming\n3.Security")
    elif option.get()==3:
        messagebox.showinfo("C++","C++ is created by Bjarne Stroustrup\n1.High performance\n2.Low-level access\n3.Cross-platform compatibility")
        
option=IntVar()
rad1=Radiobutton(window,text="Python",variable=option,value=1,command=show)
rad2=Radiobutton(window,text="Java",variable=option,value=2, command=show)
rad3=Radiobutton(window,text="C++",variable=option,value=3,command=show)

rad1.grid(row=0,column=0)
rad2.grid(row=1,column=0)
rad3.grid(row=2,column=0)

window.mainloop()