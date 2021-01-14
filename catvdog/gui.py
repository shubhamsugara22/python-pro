import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy

from keras.models import load_model

model = load_model('model1_catVSdogs_10epoch.h5')

classes = {
    0: 'it is a cat',
    1: 'it is a dog',
}

top = tk.Tk()

top.geometry("800x600")

top.title("Cat vs Dogs classification")
top.configure(background="#CDCDCD")
label = Label(top, background="#CDCDCD", font=('arial', 15, 'bold'))

sign_image = Label(top)


def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((128, 128))
    image = numpy.expand_dims(image, axis=0)
    image = nmupy.array(image)
    image = image/255
