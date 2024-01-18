import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self,title,size):
        super().__init__()

        #main setup
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')#str(size[0])+'x'+str(size[1])
        self.minsize(size[0],size[1])

        #widgets
        self.menu=Menu(self)
        self.menu=Main(self)


        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.place(x=0,y=0,relwidth=0.3,relheight=1)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.menu_button1 = ttk.Button(self, text='Button1')
        self.menu_button2 = ttk.Button(self, text='Button2')
        self.menu_button3 = ttk.Button(self, text='Button3')

        self.menu_slider1 = ttk.Scale(self, orient='vertical')
        self.menu_slider2 = ttk.Scale(self, orient='vertical')

        self.toggle_frame = ttk.Frame(self)
        self.menu_toggle1 = ttk.Checkbutton(self.toggle_frame, text='check 1')
        self.menu_toggle2 = ttk.Checkbutton(self.toggle_frame, text='check 2')

        self.entry = ttk.Entry(self)

    def create_layout(self):

        #create a grid
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

        #place a widgets
        self.menu_button1.grid(row=0, column=0, sticky='nesw', columnspan=2)
        self.menu_button2.grid(row=0, column=2, sticky='nesw')
        self.menu_button3.grid(row=1, column=0, columnspan=3, sticky='nesw')

        self.menu_slider1.grid(row=2, column=0, rowspan=2, sticky='nesw', pady=20)
        self.menu_slider2.grid(row=2, column=2, rowspan=2, sticky='nesw', pady=20)

        # toggle layout
        self.toggle_frame.grid(row=4, column=0, columnspan=3, sticky='nesw')
        self.menu_toggle1.pack(side='left', expand=True)
        self.menu_toggle2.pack(side='left', expand=True)

        # entry layout
        self.entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor='center')

class Main(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        Entry(self,'Entry 1','Button1','red')
        Entry(self,'Entry 2','Button2','blue')

class Entry(ttk.Frame):
    def __init__(self,parent,label_text,button_text,label_background):
        super().__init__(parent)
        main_label1 = ttk.Label(self, text=label_text, background=label_background)
        main_button = ttk.Button(self, text=button_text)

        main_label1.pack(expand=True, fill='both')
        main_button.pack(expand=True, fill='both', pady=10)

        self.pack(side='left',expand=True,fill='both',padx=20,pady=20)




App('Combined layout class',(600,600))