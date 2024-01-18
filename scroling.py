import tkinter as tk
from tkinter import ttk
from random import randint,choice

window=tk.Tk()
window.geometry('600x400')
window.title("Scrolling")

#canvas
# canvas=tk.Canvas(window,bg='white',scrollregion=(0,0,2000,5000))#left top right bottom
# canvas.create_line(0,0,200,500,fill='green',width=10)
# for i in range(100):
#     l=randint(0,2000)
#     t=randint(0,5000)
#     r=l+randint(10,500)
#     b=t+randint(10,500)
#     color=choice(('red','green','blue','yellow','orange'))
#     canvas.create_rectangle(l,t,r,b,fill=color)
# canvas.pack(expand=True,fill='both')
#
#     #vertical
# #MouseScrolling
# canvas.bind('<MouseWheel>',lambda event:canvas.yview_scroll(-int(event.delta/60),"units"))# w 99% units
#
# #scrollbar
# scrollbar=ttk.Scrollbar(window,orient='vertical',command=canvas.yview)
# canvas.configure(yscrollcommand=scrollbar.set)
# scrollbar.place(relx=1,rely=0,relheight=1,anchor='ne')
#
#     #horizontal
# #mousceScrolling
# canvas.bind('<Control MouseWheel>',lambda event:canvas.xview_scroll(-int(event.delta/60),"units"))
#
# #scrollbar
# scrollbar_horiztonal=ttk.Scrollbar(window,orient='horizontal',command=canvas.xview)
# canvas.configure(xscrollcommand=scrollbar_horiztonal.set)
# scrollbar_horiztonal.place(relx=0,rely=1,relwidth=1,anchor='sw')

#text
# text=tk.Text(window)
# for i in range(1,200):
#     text.insert(f'{i}.0',f'text: {i}\n')
# text.pack(expand=True,fill='both')
#
# scrollbar_text=ttk.Scrollbar(window,orient='vertical',command=text.yview)
# text.configure(yscrollcommand=scrollbar_text.set)
# scrollbar_text.place(relx=1,rely=0,relheight=1,anchor='ne')

#treeview
tabel=ttk.Treeview(window,columns=(1,2),show='headings')
tabel.heading(1,text='First Name')
tabel.heading(2,text='Last Name')
first_names=['Bob','Maria','Robert','Mateusz','Bartek']
last_names=['nwm','cos','fhdsghjkf','hgfhdfghfgdh','cvbvcvbc']
for i in range(100):
    tabel.insert(parent='',index=tk.END,values=(choice(first_names),choice(last_names)))
tabel.pack(expand=True,fill='both')

scrollbar_tabel=ttk.Scrollbar(window,orient='vertical',command=tabel.yview)
tabel.configure(yscrollcommand=scrollbar_tabel.set)
scrollbar_tabel.place(relx=1,rely=0,relheight=1,anchor='ne')

#run
window.mainloop()