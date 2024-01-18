import tkinter as tk
from tkinter import ttk

def button_fun():
    text=entry_string.get()
    label.config(text=text)
    #label['text']=text opcjonalnie to na górze lub to zakomendowane :)
    entry['state']='disable'

def button2_fun():
    label['text']='befor change'
    entry['state']='normal'
#window
window=tk.Tk()
window.title("label")
window.geometry('200x200')

entry_string=tk.StringVar()
label=tk.Label(master=window,text='befor change')
entry=tk.Entry(master=window,textvariable=entry_string)
button=tk.Button(master=window,text='A button',command=button_fun)
exercise_button=tk.Button(master=window,text='A exercise_button',command=button2_fun)

label.pack()
entry.pack()
button.pack()
exercise_button.pack()

#run
window.mainloop()