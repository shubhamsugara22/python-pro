from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
from keras.models import Sequential
import random
import numpy as np
import nltk

import json

import pickle

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
