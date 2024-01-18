import tkinter as tk
from tkinter import ttk#window


window=tk.Tk()
window.title("canvas")
window.geometry('600x600')

#canvas
canvas=tk.Canvas(window,bg='white')
canvas.pack()

canvas.create_rectangle((20,20,100,200),fill='red',width=10,dash=(1,2),outline='green')#left top right bottom
canvas.create_oval(200,0,300,100,fill='green')#left top rigth bottom
canvas.create_line((0,0,100,100),fill='blue')#start_x,Start_y,end_x,end_y




window.mainloop()