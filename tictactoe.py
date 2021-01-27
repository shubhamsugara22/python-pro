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


def checker(digit):
    global count, mark, digits
    if digit == 1 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = 'x'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'o'
            panels[digit] = mark
        button1.config(text=mark)
        count = count + 1
        sign = mark
        if(win(panels, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            root.destroy()
        elif(win(panels, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            root.destroy()

    if digit == 2 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = 'x'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'o'
            panels[digit] = mark
        button1.config(text=mark)
        count = count + 1
        sign = mark
        if(win(panels, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            root.destroy()
        elif(win(panels, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            root.destroy()

    if digit == 3 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = 'x'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'o'
            panels[digit] = mark
        button1.config(text=mark)
        count = count + 1
        sign = mark
        if(win(panels, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            root.destroy()
        elif(win(panels, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            root.destroy()

    if digit == 4 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = 'x'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'o'
            panels[digit] = mark
        button1.config(text=mark)
        count = count + 1
        sign = mark
        if(win(panels, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            root.destroy()
        elif(win(panels, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            root.destroy()

    if digit == 5 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = 'x'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'o'
            panels[digit] = mark
        button1.config(text=mark)
        count = count + 1
        sign = mark
        if(win(panels, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            root.destroy()
        elif(win(panels, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            root.destroy()

    if digit == 6 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = 'x'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'o'
            panels[digit] = mark
        button1.config(text=mark)
        count = count + 1
        sign = mark
        if(win(panels, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            root.destroy()
        elif(win(panels, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            root.destroy()

    if digit == 7 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = 'x'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'o'
            panels[digit] = mark
        button1.config(text=mark)
        count = count + 1
        sign = mark
        if(win(panels, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            root.destroy()
        elif(win(panels, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            root.destroy()

    if digit == 8 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = 'x'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'o'
            panels[digit] = mark
        button1.config(text=mark)
        count = count + 1
        sign = mark
        if(win(panels, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            root.destroy()
        elif(win(panels, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            root.destroy()

    if digit == 9 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = 'x'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'o'
            panels[digit] = mark
        button1.config(text=mark)
        count = count + 1
        sign = mark
        if(win(panels, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            root.destroy()
        elif(win(panels, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            root.destroy()

    if(count > 8 and win(panels, 'X') == False and win(panels, 'O') == False):
        msg.showinfo("Result", "Match Tied")
        root.destroy()


window = tk.Tk()

window.geometry("500x600")

window.title("TIC-TAC-TOE")


def Hello():
    print("Hello world")


button = Button(window, text="show hello", command="Hello").place(x=30, y=150)
window.mainloop()
