#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:18:18 2020

@author: IssaCamara
"""
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Conv1D, Bidirectional, Dense, Input, Dropout
from keras.regularizers import l2
from keras import Model


class SentimentModel(Sequential):


    def __init__(self, EMBEDDING_DIM, vocab_size, max_length): 
        #super().__init__()
        super(SentimentModel, self).__init__()
        # Model.__init__(self)
        # self.add(Embedding(vocab_size, EMBEDDING_DIM, input_length=max_length+1))
        # self.add(Conv1D(128, 5, activation='relu', kernel_regularizer=l2(0.05)))    
        # self.add(GlobalMaxPooling1D())
        
        # self.add(Flatten())
        # #model.add(LSTM(units=128, kernel_regularizer=l2(0.01), dropout=0.1))
        # self.add(Dense(256, activation='relu', kernel_regularizer=l2(0.01)))
        # self.add(Dense(5, activation='softmax'))
        #super().__init__(self)

        # ---------------------o---------------------
        # self.add(Input(shape=(max_length,), dtype='int32'))
        # self.add(Embedding(vocab_size, EMBEDDING_DIM, input_length=max_length))
        # self.add(Conv1D(64, 5, activation='relu'))
        # self.add(Bidirectional(LSTM(64, dropout=0.1, recurrent_dropout=0.25)))
        # self.add(Dense(1024, activation='relu'))
        # self.add(Dropout(0.2))
        # self.add(Dense(512, activation='relu'))
        # self.add(Dense(1, activation='sigmoid'))
        # ---------------------o---------------------
         
        embedding_layer = Embedding(vocab_size, EMBEDDING_DIM,input_length=max_length, trainable=False)
        self.add(Input(shape=(max_length,), dtype='int32'))
        self.add(embedding_layer) 
        self.add(Conv1D(64, 5, activation='relu'))
        self.add(Bidirectional(LSTM(64, dropout=0.1, recurrent_dropout=0.25)))
        self.add(Dense(1024, activation='relu'))
        self.add(Dropout(0.2))
        self.add(Dense(512, activation='relu'))
        self.add(Dense(1, activation='sigmoid'))
        # Model.__init__(self,sequence_input, outputs)
    



