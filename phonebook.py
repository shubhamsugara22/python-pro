import tkinter as tk
from tkinter import *
root = Tk()

root.geometry('400x400')
root.config(bg='SlateGray3')
root.resizable(0, 0)
root.title("Address book")

contact_list[
    ['Shubham', '8944653345'],
    ['shakuni', '666666666'],
    ['fomo', '5698356784'],
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


def Selected():
    return int(select.curselection()[0])


def AddContact():
    contact_list.append([Name.get(), Number.get()])
    Select_set()


def EDIT():
    contact_list[Selected()] = [Name.get(), Number.get()]
    Select_set()


def DELETE():
    del contact_list[Selected()]
    Select_set()


def VIEW():
    NAME, PHONE = contact_list[Selected()]
    Name.set(NAME)
    Number.set(PHONE)


def EXIT():
    root.destroy()


def RESET():
    Name.set('')
    Number.set('')


def Select_set():
    contact_list.sort()
    select.delete(0, END)
    for name, phone in contact_list:
        select.insert(END, name)


Select_set()
