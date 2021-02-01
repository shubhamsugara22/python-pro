from keras.models import Load_model
from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image

model = Load_model('mnist.h5')
