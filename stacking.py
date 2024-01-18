import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title('Grid')
window.geometry('400x400')

#widgets
label1=ttk.Label(window,text='Label 1',background='green')
label2=ttk.Label(window,text='Label 2',background='red')
label3=ttk.Label(window,text='Label 3',background='blue')



button=ttk.Button(window,text='Button 1',command= lambda :label1.lift(aboveThis=label2))#above tylko idzie ponad 1 nie przeskoczy label3
button2=ttk.Button(window,text='Button2',command=lambda: label2.lift() )
button3=ttk.Button(window,text='Button3',command=lambda: label3.lift() )

#layout
label1.place(x=50,y=100,width=200,height=150)
label2.place(x=150,y=60,width=140,height=100)
label3.place(x=100,y=120,width=140,height=100)

button.place(relx=0.6,rely=1,anchor='se')
button2.place(relx=0.8,rely=1,anchor='se')
button3.place(relx=1,rely=1,anchor='se')

#run
window.mainloop()