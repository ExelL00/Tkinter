

#tab widgets
notebook=ttk.Notebook(window)

#tab1
tab1=ttk.Frame(notebook)
label1=ttk.Label(tab1,text='Text in a tab1')
label1.pack()
button1=ttk.Button(tab1,text='A button in tab1')
button1.pack()

tab2=ttk.Frame(notebook)
label2=ttk.Label(tab2,text='Text in a tab2')
label2.pack()
entry2=ttk.Entry(tab2)
entry2.pack()

notebook.add(tab1,text='Tab1')
notebook.add(tab2,text='Tab2')
notebook.pack()

window.mainloop()