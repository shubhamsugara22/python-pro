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
# combinatio between intents and pattern
print(len(documents), "documents")

#classess= intents
print(len(classes), "classes", classes)

# words = all words , vocabulary
print(len(words), "unique lematized words", words)

pickle.dump(words, open('words.pkl', 'wb'))

pickle.dump(classes, open("classes.pkl", 'wb'))

# create your training data
training = []

# create an eempty array for your output
output_empty = [0]*len(classes)

for doc in documents:
    bag = []
    pattern_words = doc[0]

    pattern_words = [lemmatizer.lemmatize(
        word.lower()) for word in pattern_words]

for w in words:
    bag.append(1) if w in pattern_words else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])
# shuffle your features in np array
random.shuffle(training)
training = np.array(training)

train_x = list(training[:, 0])
train_y = list(training[:, 1])

print("training data created")
