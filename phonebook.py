import tkinter as tk
from tkinter import *
root = Tk()

root.geometry('400x400')
root.config(bg='SlateGray3')
root.resizable(0, 0)
root.title("Address book")

contact_list[

]

Name = StringVar()
Number = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)
