import tkinter as tk
from tkinter import *
import randfacts
import time

# function to add facts


def move():
    facts = randfacts.getFact(True)
    c = "*)"
    label = Label(root, text=c+facts)
    label.pack()

# function to close window


def destroy():
    root.destroy()


root = tk.Tk()

root.config(bg="White")
root.geometry("400x400")

button = tk.Button(root, text="click here to get facts", command=move)
button2 = tk.Button(root, text="clear and quit", command=destroy)

button.pack()
button2.pack()

root.mainloop()
