import tkinter as tk
from tkinter import ttk

#windows
window=tk.Tk()
window.geometry('600x400+200+200')#width height left top 600x400+300x+00
window.title("custom the window")
#window.iconbitmap('') zmiana ikony programu

#window attributes
#window.minsize(200,100) #max zmniejszenia okna
#window.maxsize(800,700) #max zwiekszenia okna
#window.resizable(True,False) #rozszerzanie okna tylko poziomie

#screen attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

#window attributes
window.attributes('-alpha',1) #przezroczystość
window.attributes('-topmost',True) #zawsze na wierzchu/ponad innymi aplikacjami w tle

#security events
window.bind('<Escape>',lambda event:window.quit())

#window.attributes('-fullscreen',True)#fullscreen

#title bar
window.overrideredirect(True)# nie widzisz paska na górze okna
grip=ttk.Sizegrip(window)
grip.place(relx=1.0,rely=1.0,anchor='se') #prawy dolny do rozszerzania okna

window.mainloop()
