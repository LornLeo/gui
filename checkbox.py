from tkinter import *
window=Tk()
window.title('Check Button')
window.geometry("500x500")

def check():
    chk_state.set(True)

chk_state=BooleanVar()
chk1 = Checkbutton(window, text='mains',var=chk_state,command=check)
chk1.grid(column=0,row=0)

chk_state1=BooleanVar()
chk_state1.set(True)

chk2 = Checkbutton(window, text='drink',var=chk_state1)
chk2.grid(column=0,row=1)

chk_state2=BooleanVar()
chk_state2.set(True)

chk3 = Checkbutton(window, text='desert',var=chk_state2)
chk3.grid(column=0,row=2)

window.mainloop()

    