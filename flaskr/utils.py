#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:24:21 2020

@author: IssaCamara
"""
import numpy as np
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

def vectorize(X_train, X_val, y_train, y_val, tokenizer, max_length):

    X_train_vect = tokenizer.texts_to_sequences(X_train)
    X_val_vect = tokenizer.texts_to_sequences(X_val)
    
    X_train_vect = pad_sequences(X_train_vect, max_length)
    X_val_vect = pad_sequences(X_val_vect, max_length)
    return (X_train_vect, X_val_vect)
    




def predict_sentiment(text, model, tokenizer, max_length):
    text_vect = tokenizer.texts_to_sequences(pd.Series(text))
    
    text_vect = pad_sequences(text_vect, max_length)
    
    y_pred = model.predict_classes(text_vect)
    
    return y_pred


def predict_proba(text, model, tokenizer, max_length):

    text_vect = tokenizer.texts_to_sequences(pd.Series(text))
    
    text_vect = pad_sequences(text_vect, max_length)
        
    proba = model.predict(text_vect)
    
    return proba
