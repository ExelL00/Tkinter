import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


#windows
window=tk.Tk()
window.title("Sliders")

#sliders
scale_float=tk.DoubleVar(value=15)
scale=ttk.Scale(window,
                command=lambda value: proggres.stop(),
                from_=0,to=25,
                length=300,
                orient='vertical',
                variable=scale_float)
scale.pack()

#proggres bar
proggres=ttk.Progressbar(window,
                         variable=scale_float,
                         maximum=25,
                         orient='horizontal',
                         mode='indeterminate',# lub determinate
                         length=400)
proggres.pack()

#proggres.start(1000)

#ScrollText
scrolled_text=scrolledtext.ScrolledText(window,width=50,height=10)
scrolled_text.pack()

#exercise
max_int=tk.IntVar()
proggres1=ttk.Progressbar(window,orient='vertical',variable=max_int)
proggres1.pack()
proggres1.start()

label=ttk.Label(master=window,textvariable=max_int)
label.pack()

scale1=ttk.Scale(window,from_=0,to=100,variable=max_int)
scale1.pack()


window.mainloop()