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


def impactScore(follows, retwt_count, fav_count):
	#Users with many followers will report an impact score close to the # of retweets
	#Users with very few followers, have their impact score re-scaled to reflect the minimal penetration of their retweeting
	impact = 0.0
	try:
		impact = (retwt_count * follows) / (follows + retwt_count + fav_count)
	except ZeroDivisionError:
		impact = 0.0
	else:
		impact = (retwt_count * follows) / (follows + retwt_count + fav_count)
	
	return impact


def analysis(js):
	twt=json.loads(js)
	if(twt['lang']=='en'):
		txt=twt['text']
		
		#check if this is a retweet
		try:
			retwt_count=twt['retweeted_status']['retweet_count']
		#if it is, return its retweet count
		except KeyError:
			retwt_count=twt['retweet_count']
		#otherwise return the original tweet's retweet count
		else:
			retwt_count=twt['retweeted_status']['retweet_count']
		
		#do the same for favorites
		try:
			fav_count=twt['retweeted_status']['favorite_count']
		except KeyError:
			fav_count=twt['favorite_count']
		else:
			fav_count=twt['retweeted_status']['favorite_count']
		
		follows=twt['user']['followers_count']
		username=twt['user']['screen_name']
		blob=TextBlob(txt)
		pol=blob.sentiment.polarity
		print "Posted by ",username
		print "Seen by ",follows," users"
		print "Favorited by ",fav_count," users"
		print "Retweeted by ",retwt_count, " users"
		print "Polarity        : ",blob.sentiment.polarity
		score = impactScore(follows, retwt_count, fav_count)
		print "Impact Score is ",score
		#print "Average Polarity: ",avgpol
		#print "Magnification   : ",retwt_count + fav_count
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

