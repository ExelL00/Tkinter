import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x:{event.x} y:{event.y}')

#window
window=tk.Tk()
window.title("events")
window.geometry('600x600')

#widgets
text=tk.Text()
text.pack()

entry=tk.Entry()
entry.pack()

button=tk.Button(text='Button')
button.pack()

#events
button.bind('<Alt-KeyPress-a>',lambda event:print(event))
text.bind('<Motion>',get_pos)
window.bind('<KeyPress>',lambda event:print(f'a button press:({event.char})'))
entry.bind('<FocusIn>',lambda event:print('entry field was selected'))
entry.bind('<FocusOut>',lambda event:print('entry field was unselected'))
window.mainloop()