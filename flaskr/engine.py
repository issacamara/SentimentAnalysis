#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:45:46 2020

@author: IssaCamara
"""

from flask import Flask, jsonify, request
from model import SentimentModel
import requests
import pandas as pd
from utils import vectorize, predict_proba
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import nltk, re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from math import ceil
import config
#from tqdm import tqdm

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config.Config")

filename = app.config['MODEL']
max_length = app.config['SENTENCE_MAX_LENGTH']
embedding_dim = app.config['EMBEDDING_DIM']
vacab_size = app.config['VOCABULARY_SIZE']
model = SentimentModel(embedding_dim, vacab_size, max_length)
model.load_weights(filename)


def preprocess(text, stem=False):

    stemmer = SnowballStemmer('english')
    text_cleaning_re = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
    text = re.sub(text_cleaning_re, ' ', str(text).lower()).strip()
    tokens = []
    stop_words = stopwords.words('english')

    for token in text.split():
        if token not in stop_words:
            if stem:
              tokens.append(stemmer.stem(token))
            else:
              tokens.append(token)
    return " ".join(tokens)
df = pd.read_csv(app.config['TWEETS'])
print('Preprocessing ...')
#tqdm.pandas()
df['comment'] = df['comment'].apply(lambda x: preprocess(x))

tokenizer = Tokenizer()
print('Fitting the tokenizer on the tweets')
tokenizer.fit_on_texts(df['comment'])
print('data preparation done !')

    
#from . import submit
#app.register_blueprint(submit.bp)
@app.route('/engine', methods=['POST'])
def hello():
    if 'review' not in request.form:
        return jsonify({'error': 'no review in body'}), 400
    else:
        review = request.form['review']
        proba = predict_proba(review, model, tokenizer, max_length)[0,0]
        #output = len(review)
        #print(review, proba)
        return jsonify(ceil(proba * 100))

    #print(model.summary())

