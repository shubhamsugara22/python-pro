from tkinter import *
from pytube import Youtube


root = Tk()
root.geometry("500X400")
root.resizable(0, 0)
root.title("video downloader")

Label(root, text="Video downloader", font="arial 20 bold").pack()

link = StringVar()
Label(root, text="paste link here", font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)
