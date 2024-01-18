import tkinter as tk
from tkinter import ttk

#windows
window=tk.Tk()
window.geometry('600x400')
window.title("Menu")

#menu
menu=tk.Menu(window)

#sub menu
file_menu=tk.Menu(menu,tearoff=False)
menu.add_cascade(label='File',menu= file_menu)

file_menu.add_command(label='New',command=lambda :print('New file'))
file_menu.add_command(label='Open',command=lambda :print('Open file'))
file_menu.add_separator()

more_sub_menu=tk.Menu(menu,tearoff=False)
file_menu.add_cascade(label='More',menu=more_sub_menu)
more_sub_menu.add_command(label='more setting',command=lambda: print('more'))




#another sub menu
help_menu=tk.Menu(menu,tearoff=False)
menu.add_cascade(label='Help',menu=help_menu)

help_menu.add_command(label='Help entry',command=lambda :print(help_check_button.get()))

help_check_button=tk.StringVar()
help_menu.add_checkbutton(label='Check',onvalue='on',offvalue='off',variable=help_check_button)


window.config(menu=menu)

#menu button
menu_button=ttk.Menubutton(window,text='Menu button')
menu_button.pack()

button_sub_menu=tk.Menu(menu_button,tearoff=False)
button_sub_menu.add_command(label='entry 1',command=lambda :print('test1'))

menu_button.config(menu=button_sub_menu)
window.mainloop()