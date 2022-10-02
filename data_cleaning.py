# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re
import pandas as pd
from langdetect import detect
import spacy
#loading the english language small model of spacy
en = spacy.load('en_core_web_sm')
sw_spacy = en.Defaults.stop_words


def clean_data(x):
    x=re.sub(r'http\S+', ' ', x)
    x=re.sub(r"([#@]\S+)|'https?://\S+'|[A-Za-z0-9]*@[A-Za-z]*\.?[A-Za-z0-9]*|[^A-Za-z]", " ",x)
    x=re.sub(r"\s+"," ",x)
    not_stop_words=[w for w in x.split() if w.lower() not in sw_spacy]
    x=" ".join(not_stop_words)
    return x

def detect_my(text):
   try:
       return detect(text)
   except:
       return 'unknown'

path=r"C:\Users\jaysh\OneDrive\Desktop\archive\anon_disorder_tweets.csv"
unclean_tweets=pd.read_csv(path)
unclean_tweets=unclean_tweets.drop('user_id',axis=1)
pd.set_option('display.max_colwidth',None)
unclean_tweet_mil=unclean_tweets.iloc[:10000,:]
unclean_tweet_mil['clean_tweets']=unclean_tweet_mil['text'].map(lambda x:clean_data(x))
#unclean_tweet_mil['lang_detect']=unclean_tweet_mil['text'].map(detect_my)
unclean_tweet_mil.head()
#unclean_tweet_5=unclean_tweet_mil.iloc[:100000,]

#clean_text_csv=unclean_tweet_mil.to_csv('clean_text_csv')

#unclean_tweets['disorder'].unique()





