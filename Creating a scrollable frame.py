import tkinter as tk
from tkinter import ttk
from random import randint,choice

class ListFrame(ttk.Frame):
    def __init__(self,parent,text_data,item_height):
        super().__init__(master=parent)
        self.pack(expand=True,fill='both')

        #widget data
        self.text_data=text_data
        self.item_number=len(text_data)
        self.list_height=item_height*self.item_number

        #cnvas
        self.canvas=tk.Canvas(self,background='red',scrollregion=(0,0,self.winfo_width(),self.list_height))
        self.canvas.pack(expand=True,fill='both')

        #display frame
        self.frame=ttk.Frame(self)

        for index,item in enumerate(text_data):
            self.create_item(index,item).pack(expand=True,fill='both',pady=4,padx=10)

        #scrollbar
        self.scrollbar=ttk.Scrollbar(self,orient='vertical',command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        #events
        self.bind('<Configure>',self.update_size)

    def update_size(self,event):

        if event.height < self.list_height:
            height=self.list_height
            self.canvas.bind_all('<MouseWheel>',lambda event:self.canvas.yview_scroll(-int(event.delta/60),"units"))
            self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
        else:
            height=event.height
            self.canvas.unbind_all('<MouseWheel>')
            self.scrollbar.place_forget()

        self.canvas.create_window(
            (0,0),
            window=self.frame,
            anchor='nw',
            width=event.width,
            height=height)

    def create_item(self,index,item):
        frame=ttk.Frame(self.frame)

        #grid
        frame.rowconfigure(0,weight=1)
        frame.columnconfigure((0,1,2,3,4),weight=1,uniform='a')

        #widgets
        ttk.Label(frame,text=f'#{index}').grid(row=0,column=0)
        ttk.Label(frame,text=f'{item[0]}').grid(row=0,column=1)
        ttk.Button(frame,text=f'{item[1]}').grid(row=0,column=2,columnspan=3,sticky='nesw')

        return frame




#setup
window=tk.Tk()
window.geometry('500x400')
window.title("Creating a scrollable frame")

text_list=[('Label','button'),('thing','click'),('third','something'),('Label1','button'),('Label2','button'),('Label3','button'),('Label3','button')]
ListFrame=ListFrame(window,text_list,100)

# #canvas
# canvas=tk.Canvas(window,background='white')
# canvas.create_window((20,50),window=ttk.Label(window,text='A label'))
# canvas.pack(expand=True,fill='both')

#run
window.mainloop()
