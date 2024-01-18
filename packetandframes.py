import tkinter as tk
from tkinter import ttk

#pack and frames

#window
window=tk.Tk()
window.title('Pack')
window.geometry('400x600')

#widgets
    #topframe
top_frame=ttk.Frame(window)
label1=ttk.Label(top_frame,text='First Label',background='red')
label2=ttk.Label(top_frame,text='Label 2',background='blue')

    #middle frmae
label3=ttk.Label(window,text="middle Label",background='green')

    #bottom frame
bottom_frame=ttk.Frame(window)
label4=ttk.Label(bottom_frame,text="Last Label",background='orange')
button=tk.Button(bottom_frame,text='Button')
button2=tk.Button(bottom_frame,text='Another Button')

    #bottom farmes for a button
bottom_frame_burtton=ttk.Frame(bottom_frame)
button3=tk.Button(bottom_frame_burtton,text='Button3')
button4=tk.Button(bottom_frame_burtton,text='Button4')
button5=tk.Button(bottom_frame_burtton,text='Button5')

#layout
    #top widgets
label1.pack(side='left',fill='both',expand=True)
label2.pack(side='left',fill='both',expand=True)
top_frame.pack(fill='both',expand=True)

    #middle frame
label3.pack(expand=True)

    #bottom frame
button.pack(side='left',expand=True,fill='both')
label4.pack(side='left',expand=True,fill='both')
button2.pack(side='left',expand=True,fill='both')
bottom_frame.pack(expand=True,fill='both',pady=20,padx=20)

button3.pack(expand=True,fill='both')
button4.pack(expand=True,fill='both')
button5.pack(expand=True,fill='both')
bottom_frame_burtton.pack(side='left',expand=True,fill='both')




#run
window.mainloop()