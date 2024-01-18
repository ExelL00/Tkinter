import tkinter as tk
from tkinter import ttk

#window
window=tk.Tk()
window.title("Tkinter variables ")
window.geometry('200x200')

#tk variables
string_var=tk.StringVar(value='Start value')

#ttk label
label=ttk.Label(master=window,text='This is a test',textvariable=string_var)
label.pack()

#ttk enrty
entry=ttk.Entry(master=window,textvariable=string_var)
entry.pack(pady=5)

#run
window.mainloop()