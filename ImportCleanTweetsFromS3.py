#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:05:34 2022

@author: kpathak6448
"""


import os

import boto3
import pandas as pd

AWS_S3_BUCKET = "prebuiltnodes"
AWS_ACCESS_KEY_ID = "AKIAQ53INSGAWRSXLBOU"
AWS_SECRET_ACCESS_KEY = "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"


s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    
)

response = s3_client.get_object(Bucket=AWS_S3_BUCKET, Key="books.csv")

status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

if status == 200:
    print(f"Successful S3 get_object response. Status - {status}")
    books_df = pd.read_csv(response.get("Body"))
    print(books_df)
else:
    print(f"Unsuccessful S3 get_object response. Status - {status}")