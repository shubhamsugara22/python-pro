from keras.models import Load_model
from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image

model = Load_model('mnist.h5')


def predict_digit(img):
    img = img.resize((28, 28))
    img = img.convert('L')
    img = np.array(img)
    img = img.reshape(1, 28, 28, 1)
    img = img/255.0
    res = model.predict([img])[0]
    return np.argmax(res), max(res)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.x = self.y = 0
        # creating elements
        self.canvas = tk.Canvas(
            self, width=300, height=300, bg="white", cursor="cross")
        self.label = tk.Label(self, text="thinking ...",
                              font=("Helvetica", 48))
        self.classify_btn = tk.Button(
            self, text="recognise", command=self.classify_handwriting)
        self.button_clear = tk.Button(
            self, text="clear", command=self.clear_all)

        self.canvas.grid(row=0, column=0, pady=2, sticky=W,)
        self.label.grid(row=0, column=1, pady=2, padx=2)
        self.classify_btn.grid(row=1, column=1, pady=2, padx=2)
        self.button_clear.grid(row=1, column=0, pady=2)
