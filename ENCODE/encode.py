from tkinter import *
import base64


root = Tk()
root.geometry("500x300")
root.resizable(0, 0)
root.title("Message encoder and decoder")


Label(root, text="ENCODE DECODE", font='arial 20 bold').pack()
Label(root, text="Shubham project", font='arial 20 bold').pack(side=BOTTOM)

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


def Encode(key, message):
    enc = []

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i])+ord(key_c)) % 256))

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr(256+ord(message[i])-ord(key_c)) % 256)

    return " ".join(dec)


def mode():
    if (mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif (mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set("Invalid mode")


def Exit():
    root.destroy()


def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


Label()
Entry()

Label()
Entry()

Label()
Entry()
Entry()

Button()
Button()
Button()

root.mainloop()
