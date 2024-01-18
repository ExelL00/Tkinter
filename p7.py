import tkinter as tk
from tkinter import ttk
from random import choice

#windows
window=tk.Tk()
window.title("TreeView")
window.geometry('600x400')

#data
first_names=['Robert','Jan','Bob','Mateusz','Bartek','Anna','Liza']
last_names=['Kowalski','Chuj','Nwm','Gówno','Jaja','Słonce','Nwmv2']

table=ttk.Treeview(window,columns=('first','last','email'),show='headings')
table.heading('first',text='First name')
table.heading('last',text='Surname')
table.heading('email',text='Email')
table.pack(fill='both',expand=True)

#insert values in tabel
#table.insert(parent='',index=0,values=('John','Doe','gfhsdufius@gmail.com'))
for i in range(100):
    first=choice(first_names)
    last=choice(last_names)
    email=f'{first[0]}{last}@gmail.com'
    data=(first,last,email)
    table.insert(parent='', index=0, values=(data))

#events
def select_table(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i))

table.bind('<<TreeviewSelect>>',select_table)

def delete_items(_):
    print('delete')
    for i in table.selection():
        table.delete(i)
table.bind('<Delete>',delete_items)


window.mainloop()


