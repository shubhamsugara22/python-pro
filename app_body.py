import random
import json
from keras.models import load_model
import pickle
import numpy as np
import nltk

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

model = load_model("chatbot_model.h5")

intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))

classes = pickle.load(open('classes.pkl', 'rb'))
