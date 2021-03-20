#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:22:41 2020

@author: IssaCamara
"""
class Config(object):
    DEBUG = False
    TESTING = False
    FLASK_APP = "flaskr"
#    PATH = '/Users/IssaCamara/Developer/Data_Science/Projects/Sentiment_Analysis/'
    PATH = ''
    MODEL = PATH + 'flaskr/model.h5'
    TWEETS = PATH + 'data/tweets.csv'
    SENTENCE_MAX_LENGTH = 53
    EMBEDDING_DIM = 200
    VOCABULARY_SIZE = 313441

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True


