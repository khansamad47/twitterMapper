#code to save tweets in json
import sys
import tweepy
import json
import csv
from textblob import TextBlob

import os
import time
from datetime import datetime
from threading import Timer

access_key = "2864513512-1JkMkwIRHMjSBLdNgh1zIGiSX2ZJMnhoZZ3b8uR"
access_secret = "vpBlz4E2eSZnw7TVlUAGcmwI4AZ6Hf2Z9CBhin3S7HZSl"
consumer_key = "50n8PRe0MTuC6NyYEqUqnwJsf"
consumer_secret = "ZCFFAbNZfJqwsM1QuPPPBC5ahSX3F8Xsm3PVY4p0PKexO89ygt"


def analysis(js):
	twt=json.loads(js)
	if(twt['lang']=='en'):
		txt=twt['text']
		blob=TextBlob(txt)
		pol=blob.sentiment.polarity
		#avgpol=(avgpol*n+pol)/(n+1)
		#n=n+1
		#print "Tweet           : ",txt
		print "Tweet           : ",twt
		print "Polarity        : ",blob.sentiment.polarity
		#print "Average Polarity: ",avgpol
		raw_input("Continue.")
		#time.delay(1)

class CustomStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		print status.text

	def on_data(self, data):
		analysis(data)

	def on_error(self, status_code):
		print >> sys.stderr, 'Encountered error with status code:', status_code
		return True # Don't kill the stream

	def on_timeout(self):
		print >> sys.stderr, 'Timeout...'
		return True #Don't kill the stream


keyword=raw_input("Please Enter a Keyword: ")
auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api=tweepy.API(auth)
while True: 
        engine=tweepy.streaming.Stream(auth, CustomStreamListener())
	engine.filter(track=list([keyword]))	
	#engine.filter(track=['Nike'])	

