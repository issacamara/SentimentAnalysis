#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:20:51 2020

@author: IssaCamara
"""

import os
import pandas as pd
import wget
from zipfile import ZipFile

os.system('pip install kaggle')

os.system('kaggle datasets download -d kazanova/sentiment140')

os.system('mkdir data')
os.system('mv sentiment140.zip data/')
os.system('unzip data/sentiment140.zip -d data/')
os.system('rm -f data/sentiment140.zip')


os.system('echo y | pip uninstall kaggle')

sentiment = pd.read_csv('data/training.1600000.processed.noemoticon.csv', 
                        encoding = "ISO-8859-1", header=None)
sentiment.columns

sentiment.drop([1, 2, 3, 4], axis=1, inplace=True)

sentiment.rename(columns={0:'rating', 5:'comment'}, inplace=True)

sentiment.to_csv('data/tweets.csv')

wget.download('http://nlp.stanford.edu/data/glove.6B.zip', 'data/glove.6B.zip')

with ZipFile('data/glove.6B.zip', 'r') as zipObj:
   zipObj.extractall('data/')