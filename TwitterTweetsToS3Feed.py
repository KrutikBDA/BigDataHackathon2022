#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 13:54:22 2022

@author: kpathak6448
"""

'''
Code to Fetch Data from Twitter --> Clean the Tweets --> Store in S3 Bucket
'''

#import necessary libraries
import tweepy
from textblob import TextBlob
import pandas as pd
import io
import os
import boto3

####### API KEYS FOR TWITTER ############
consumer_key='*****'
consumer_key_secret='********'
access_token='********'
access_token_secret='********'


###### API KEYS FOR AWS ################
AWS_S3_BUCKET = "<bucket name to be specified>"
AWS_ACCESS_KEY_ID = "*******"
AWS_SECRET_ACCESS_KEY = "*********"


#Function to create dataframe of tweets data
def createDataFrameForTwitterData():
    
    #Retrieve tweets through API
    auth=tweepy.OAuthHandler(consumer_key,consumer_key_secret)
    auth.set_access_token(access_token,access_token_secret)
    api=tweepy.API(auth)
    public_tweets=api.search_tweets('depression',lang="en",count=200)
    
    
    #Convert imported tweets into a pandas dataframe and returning it through the function
    tweets_df_list = []
    for tweet in public_tweets:
        row_text = tweet.text
        row_obj = [row_text]
        #print(row_obj)
        tweets_df_list.append(row_obj)
    
    tweets_df = pd.DataFrame(tweets_df_list, columns=['text'])
    return tweets_df



#Function to clean the tweets, keep relevant text and return cleaned dataFrame
def cleanTweets(raw_tweets_df):
    #Add Code Here
    return ''


#Function to upload clean data to a csv file in S3

def uploadCleanTweetsToCSV(clean_tweets_df):
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    
    with io.StringIO() as csv_buffer:
        clean_tweets_df.to_csv(csv_buffer, index=False)

        response = s3_client.put_object(
            Bucket=AWS_S3_BUCKET, Key="<name to be specified>", Body=csv_buffer.getvalue()
        )

        status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

        if status == 200:
            print(f"Successful S3 put_object response. Status - {status}")
        else:
            print(f"Unsuccessful S3 put_object response. Status - {status}")
            


raw_twitter_feed = createDataFrameForTwitterData()
cleanTweets(raw_twitter_feed)
uploadCleanTweetsToCSV(cleanTweets)