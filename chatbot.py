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

words = []

classes = []

documents = []

ignore_words = ['?', '!']

data_file = open('intents.json').read()

intents = json.load(data_file)

for intent in intents['intents']:
    for pattern in intent['patterns']:

        # tokenize each word

        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # add dcoument in corpus
        documents.append((w, intent['tag']))

        # add to our classes  list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# lemmatize , lower each word and remove duplicates
words = [lemmatizer.lemmatize(w.lower())
         for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# sort clasess
classes = sorted(list(set(classes)))
