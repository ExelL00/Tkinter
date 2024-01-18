import tkinter as tk
from tkinter import ttk

def button_fun():
    print('button a press')

def exercise_button_fun():
    print('button 2 a press')

#create a window
window=tk.Tk()
window.title('Window and widgets')
window.geometry('800x550')

#ttk label
label=ttk.Label(master=window,text='This is a test')
label.pack()

#tk text
text=tk.Text(master=window)
text.pack()

#ttk enrty
entry=ttk.Entry(master=window)
entry.pack(pady=5)

#exercise label
exercise_label=ttk.Label(master=window,text='My Label')
exercise_label.pack()

#ttk button
button=ttk.Button(master=window,text='A button',command=button_fun)
button.pack()
exercise_button=ttk.Button(master=window,text='exercise button',command=lambda: print('hello'))
exercise_button.pack(pady=5)

#run
window.mainloop()