import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'Mu5ydM98YvvfH4Ufkw8mcBUuk'
consumer_secret = 'F47DE9ER7Ipwkq4bgAqIbx009qgPjzpXCriXFdCHEN11uFPdiQ'
access_token = '3221307760-IvQGiIW7vg5TwJO4iW80W2PgpyClRP6mXfiUOEE'
access_token_secret = 'FwY5Jx6U5Nd3041jf3uaogKnIFzPr1jU3jjGHuj18mgdb'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=100,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])