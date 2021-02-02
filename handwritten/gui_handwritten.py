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
