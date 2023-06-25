from tkinter import*
from tkinter import messagebox
window=Tk()
window.title("Radio Button Application")
window.geometry("300x300")

        

rad1=Radiobutton(window,tristatevalue=0,text="Python",value=1)
rad2=Radiobutton(window,tristatevalue=0,text="Java",value=2)
rad3=Radiobutton(window,tristatevalue=0,text="C++",value=3)

rad1.grid(row=0,column=0)
rad2.grid(row=1,column=0)
rad3.grid(row=2,column=0)

window.mainloop()