import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title('Grid')
window.geometry('400x400')

#widgets

    #place
# def toggle_label_place():
#     global label_visible
#
#     if label_visible:
#         label_visible=False
#         label.place_forget()
#     else:
#         label_visible=True
#         label.place(relx=0.5, rely=0.5, anchor='center')
#
# button=ttk.Button(window,text="toggle label",command=toggle_label_place)
# button.place(x=10,y=10)
#
# label_visible=True;
# label=ttk.Label(window,text="A label")
# label.place(relx=0.5,rely=0.5,anchor='center')

    #grid
# window.columnconfigure((0,1),weight=1,uniform='a')
# window.rowconfigure(0,weight=1,uniform='a')

# def toggle_label_grid():
#     global label_visible
#
#     if label_visible:
#         label.grid_forget()
#         label_visible=False
#     else:
#         label_visible=True
#         label.grid(row=0, column=1)
#
# button=ttk.Button(window,text="toggle label",command=toggle_label_grid)
# button.grid(row=0,column=0)
#
# label_visible=True;
# label=ttk.Label(window,text="A label")
# label.grid(row=0,column=1)

    #pack

def toggle_label_pack():
    global label_visible

    if label_visible:
        label.pack_forget()
        label_visible=False
        frame.pack(expand=True,befor=button)
    else:
        label_visible=True
        frame.pack_forget()
        label.pack(expand=True,befor=button)

label_visible=True;
label=ttk.Label(window,text="A label")
label.pack(expand=True)

button=ttk.Button(window,text="toggle label",command=toggle_label_pack)
#side bottom działa ale na yt zrobił z frame wiec leci to z yt heh

button.pack()

frame=ttk.Frame(window)

#run
window.mainloop()