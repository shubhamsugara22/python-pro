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
