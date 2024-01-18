import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Extra(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Extra window')
        self.geometry('300x400')
        ttk.Label(self, text='A lable').pack()
        ttk.Button(self, text='A button').pack()
        ttk.Label(self, text='Another label').pack(expand=True)

def create_window():
    global extra_window
    extra_window=Extra()
def ask_yes_np():
    answer=messagebox.askquestion('Tittle','Body')
    print(answer)


def close_window():
    extra_window.destroy()

window=tk.Tk()
window.geometry('600x400')
window.title("Multiple windows")

button1=ttk.Button(window,text='Open a window',command=create_window)
button1.pack(expand=True)

button2=ttk.Button(window,text='Close a window',command=close_window)
button2.pack(expand=True)

button3=ttk.Button(window,text='Create yes no window',command=ask_yes_np)
button3.pack(expand=True)

#run
window.mainloop()