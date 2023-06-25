import tkinter as tk
import tkinter

class MYGUI:
    def __init__(self,master):
        self.frame1=tk.Frame

window=tkinter.Tk()
window.title('Frames')
window.geometry('500x500')

top_frame=tkinter.Frame(window).pack()
bottom_frame=tkinter.Frame(window).pack(side='bottom')

btn1=tkinter.Button(top_frame,text='Button1',fg='red').pack()
btn1=tkinter.Button(top_frame,text='Button2',fg='green').pack()
btn1=tkinter.Button(top_frame,text='Button3',fg='purple').pack(side='left')
btn1=tkinter.Button(top_frame,text='Button4',fg='orange').pack(side='left')

window.mainloop()