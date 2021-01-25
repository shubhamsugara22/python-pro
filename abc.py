import tkinter as tk
from tkinter import *

window = tk.Tk()

window.geometry("500x600")

window.title("New Project")


def Hello():
    print("Hello world")


button = button(window, text="show hello" command="Hello").place(x=30, y=150)
window.mainloop()
