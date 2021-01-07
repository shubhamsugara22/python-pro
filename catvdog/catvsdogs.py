from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation, BatchNormalization
from keras.models import Sequential
import numpy as np

import pandas as pd

from keras.preprocessing.image import ImageDataGenerator, load_img
from keras.utils import to_categorical

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

import random

import os
# image properties

Image_Width = 128
Image_Height = 128
Image_Size = (Image_Width, Image_Height)
Image_Channels = 3

# preparing data set for model
filenames = os.listdir("/train")

categories = []

for f_name in filenames:
    category = f_name.split('.')[0]
    if category == 'dog':
        categories.append(1)
    else:
        categories.append(0)

df = pd.DataFrame({
    'filename': filenames,
    'category': categories,
})

# prepare model
model = Sequential()

model.add()
model.add()
model.add()
model.add()

model.add()
model.add()
model.add()
model.add()

model.add()
model.add()
model.add()
model.add()

model.add()
model.add()
model.add()
model.add()
model.add()
