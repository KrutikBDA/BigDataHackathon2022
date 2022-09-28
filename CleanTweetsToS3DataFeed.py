#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 19:36:09 2022

@author: kpathak6448
"""

import io
import os

import boto3
import pandas as pd


AWS_S3_BUCKET = "prebuiltnodes"
AWS_ACCESS_KEY_ID = "*******"
AWS_SECRET_ACCESS_KEY = "*********"
#AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

books_df = pd.DataFrame(
    data={"Title": ["Book I", "Book II", "Book III"], "Price": [56.6, 59.87, 74.54]},
    columns=["Title", "Price"],
)


with io.StringIO() as csv_buffer:
    books_df.to_csv(csv_buffer, index=False)

    response = s3_client.put_object(
        Bucket=AWS_S3_BUCKET, Key="books.csv", Body=csv_buffer.getvalue()
    )

    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

    if status == 200:
        print(f"Successful S3 put_object response. Status - {status}")
    else:
        print(f"Unsuccessful S3 put_object response. Status - {status}")
