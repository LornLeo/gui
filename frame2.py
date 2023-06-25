import tkinter as tk


class MYGUI:
    def __init__(self,master):
        self.master=master
        self.frame1=tk.Frame(self.master,bg='red')
        self.frame2=tk.Frame(self.master,bg='green')
        self.frame3=tk.Frame(self.master,bg='blue')
        self.create_widgets()
    def create_widgets(self):
        self.button1=tk.Button(self.master,text='Frame1',command=self.show_frame1)
        self.button2=tk.Button(self.master,text='Frame2',command=self.show_frame2)
        self.button3=tk.Button(self.master,text='Frame3',command=self.show_frame3)
        self.button1.pack(side='left')
        self.button2.pack(side='left')
        self.button3.pack(side='left')
        self.label1=tk.Label(self.frame1,text="This is frame1")
        self.label2=tk.Label(self.frame1,text="This is frame2")
        self.label3=tk.Label(self.frame1,text="This is frame3")
        self.label1.config(fg="black")
        self.label2.config(fg="black")
        self.label3.config(fg="black")
        self.label1.pack(pady=20)
        self.label2.pack(pady=20)
        self.label3.pack(pady=20)
        self.frame1.pack(fill='both',expand=True)
        self.frame2.pack(fill='both',expand=True)
        self.frame3.pack(fill='both',expand=True)
        self.show_frame1()
    def show_frame1(self):
        self.frame1.pack(fill='both',expand=True)
        self.frame2.forget()
        self.frame3.forget()
    def show_frame2(self):
        self.frame2.pack(fill='both',expand=True)
        self.frame1.forget()
        self.frame3.forget()
    def show_frame3(self):
        self.frame3.pack(fill='both',expand=True)
        self.frame1.forget()
        self.frame2.forget()
if __name__=='__main__':
    master=tk.Tk()
    my_gui=MYGUI(master)
    master.mainloop()