import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


#windows
window=tk.Tk()
window.geometry('600x400')
window.title("Frames and parenting")

#frame
frame=ttk.Frame(window,width=200,height=200,borderwidth=10,relief=tk.GROOVE)
frame.pack_propagate(False) #jesli damy true to frame zmieni rozmiar do "dziecka" czyli do label, na false ma stały rozmiar jaki podamy
frame.pack(side='left')

#master setting
label=ttk.Label(frame,text='Labe in frame')
label.pack()

button=ttk.Button(frame,text='button in a frame')
button.pack()

#example
label2=ttk.Label(window,text='Label outside frame')
label2.pack(side='left')


window.mainloop()