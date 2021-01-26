import tkinter as tk
from tkinter import *
import tkinter.messagebox as msg

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mark = '' ``
count = 0
panels = ["panel"]*10


def win(panels, sign):
    return((panels[1] == panels[2] == panels[3] == sign)
           or (panels[1] == panels[4] == panels[7] == sign)
           or (panels[1] == panels[5] == panels[9] == sign)
           or (panels[2] == panels[5] == panels[8] == sign)
           or (panels[3] == panels[6] == panels[9] == sign)
           or (panels[3] == panels[5] == panels[7] == sign)
           or (panels[4] == panels[5] == panels[6] == sign)
           or (panels[7] == panels[8] == panels[9] == sign))


window = tk.Tk()

window.geometry("500x600")

window.title("TIC-TAC-TOE")


def Hello():
    print("Hello world")


button = Button(window, text="show hello", command="Hello").place(x=30, y=150)
window.mainloop()
