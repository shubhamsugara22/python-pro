import cv2  # used fro image processing
from cv2 import *
import easygui  # to open fileobx

import numpy as np  # to store image

import imageio  # to read iamge stored at particular path

import sys

import matplotlib.pyplot as plt

import os

import tkinter as tk

from tkinter import filedialog

from tkinter import *

from PIL import ImageTk, Image

top = tk.Tk
top.geometry('400x400')
top.title('Cartoonify your image!')
top.configure(background='white')
label = Label(top, background='#CDCDCD', font=('calibri', 20, 'bold'))

'''fileopen box to open the box to choose file
   and help us store file path as string '''


def upload():
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)


def cartoonify(ImagePath):
    originalImage = cv2.imread(ImagePath)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)

    # print(image)

    if originalImage is None:
        print("cannot find any image .Choose appropriate file")
        sys.exit()

    Resized1 = cv2.resize(originalImage, (960, 540))
    #plt.imshow(Resized1,cmap = gray)

# converting image to grayscale
    grayScaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    Resized2 = cv2.resize(grayScaleImage, (960, 540))

    #plt.imshow(Resized2,cmap = gray)

# smoothering a grayscale image
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    Resized3 = cv2.resize(smoothGrayScale, (960, 540))

    #plt.imshow(Resized3,cmap = gray)
# retrieving the edges for cartoon effect
    getEdge = cv2.adaptiveThreshold(
        smoothGrayScale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    Resized4 = cv2.resize(getEdge, (960, 540))
    #plt.imshow(Resized4,cmap = gray)

# applying a bilateral filter to remove noise

    colorImage = cv2.bilateralFilter(originalImage, 9, 300, 300)
    Resized5 = cv2.resize(colorImage, (960, 540))

    #plt.imshow(Resized5,cmap = gray)

# give a cartoon effect

    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
    Resized6 = cv2.resize(cartoonImage, (960, 540))
    #plt.imshow(Resized6,cmap = gray)

    images = [Resized1, Resized2, Resized3, Resized4, Resized5, Resized6]
    fig, axes = plt.subplots(3, 2, figsize=(8, 8), subplot_kw={
                             'xticks': [], 'yticks': []}, gridspec_kw=dict(hspace=0.1, wspace=0.1))

    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap=gray)

    plt.show()


def save(Resized6, ImagePath):

    new_name = "cartoonified_Image"
    path1 = os.path.dirname(ImagePath)
    extensions = os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, new_name+extensions)
    cv2.imwrite(path, cv2.cvtColor(Resized6, cv2, COLOR_RGB2BGR))
    I = "Image saved by name " + new_name + " at " + path

    tk.messagebox.showinfo(title=None, message=I)
