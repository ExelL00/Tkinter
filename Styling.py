import tkinter as tk
from tkinter import ttk,font


window=tk.Tk()
window.geometry('400x300')
window.title("Styling")

# print(font.families())

#style
style=ttk.Style()
# print(style.theme_names())
# style.theme_use('winnative')

# style.configure('TButton',background='green', foreground='green',font=('Courier',20),)
style.configure('new.TButton',background='green', foreground='green',font=('Courier',20),)
style.map('new.TButton',
          foreground=[('pressed','red'),('disabled','yellow')],
          background=[('pressed','green'),('active','blue')])

style.configure('TFrame',background='yellow')

Label=ttk.Label(
    window,
    text='A laber\nanother line fdsfdsfsd',
    background='red',
    foreground='white',
    font=('Courier',20),
    justify='left')
Label.pack()

button1=ttk.Button(window,text='Open a window',style='new.TButton')#nie ma styli, state= zawsze wyłączony
button1.pack()

frame=ttk.Frame(window,height=200,width=200)
frame.pack()


#run
window.mainloop()