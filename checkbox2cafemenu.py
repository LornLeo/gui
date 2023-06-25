from tkinter import *
window=Tk()
window.title("Food Ordering App")
window.geometry("500x500")
mains_var=BooleanVar()
mains_var.set(False)

drinks_var=BooleanVar()
drinks_var.set(False)

desserts_var=BooleanVar()
desserts_var.set(False)
selection=[]
def show_selection():
    
    if mains_var.get():
        selection.append('mains')
    if drinks_var.get():
        selection.append('drinks')
    if desserts_var.get():
        selection.append('desserts')
    if selection:
        selected_item=', '.join(selection)
        label.config(text="You have selected: {}".format(selected_item))
        mains_var.set(False)
        drinks_var.set(False)
        desserts_var.set(False)
    else:
        label.config(text="select at least one item")
    
chk1=Checkbutton(window, text="Mains", var=mains_var)
chk1.grid(row=0,column=0)

chk2=Checkbutton(window,text="Drinks",var=drinks_var)
chk2.grid(row=1,column=0)

chk3=Checkbutton(window,text="Desserts",var=desserts_var)
chk3.grid(row=2,column=0)

button=Button(window,text="Submit", command=show_selection)
button.grid(row=3,column=0)

label=Label(window,text="")
label.grid(row =4,column=0)

window.mainloop()