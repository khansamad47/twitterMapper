from django.http import HttpResponse
import tweepy
import json
from textblob import TextBlob

access_key = "2864513512-1JkMkwIRHMjSBLdNgh1zIGiSX2ZJMnhoZZ3b8uR"
access_secret = "vpBlz4E2eSZnw7TVlUAGcmwI4AZ6Hf2Z9CBhin3S7HZSl"
consumer_key = "50n8PRe0MTuC6NyYEqUqnwJsf"
consumer_secret = "ZCFFAbNZfJqwsM1QuPPPBC5ahSX3F8Xsm3PVY4p0PKexO89ygt"

class tweetDump:
	dumped=0;
	def __init__(self):
		self.dumped=[]
	def addto(self,tweet):
		self.dumped.append(tweet)
	def getJSON(self):
		dict={"data":self.dumped}
		return(json.dumps(dict))
	def cleanTweets(self):
		self.dumped=[]

allData=tweetDump()

def analysis(js,count):	
	twt=json.loads(js)
	name=""
	try:
		name=twt['user']['screen_name']
	except:
		name="Name:Execption"
	try: 
		if(twt['lang']=='en' and twt['geo']!=None):
			
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

			txt=twt['text']
			loc=twt['geo']
			date=twt['created_at']
			blob=TextBlob(txt)
			pol=blob.sentiment.polarity
			Lat=loc['coordinates'][0]
			Long=loc['coordinates'][1]
			print "Location        : ",loc
			print "Lat             : ",Lat
			print "Long            : ",Long
			print "Name            : ",name
			print "Date            : ",date
			print "Tweet           : ",txt
			print "Seen by ",follows," users"
			print "Favorited by ",fav_count," users"
			print "Retweeted by ",retwt_count, " users"
			score = impactScore(follows, retwt_count, fav_count)
			print "Impact Score is ",score
		
			print "Polarity        : ",blob.sentiment.polarity
			tmp={'lat' : Lat,'long' : Long,'handle' : name,'text' : txt,'date' : date,'score' : pol}
			allData.addto(tmp)
			return (count+1) 
		else:
			print "Geo location,en: ",twt['geo'],twt['lang']		
			return (count)
	except:
		print "Exception"
		return (count)

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


class CustomStreamListener(tweepy.StreamListener):
	num_tweets=0
	maxTweets=0

	def __init__(self,api=None):
		super(CustomStreamListener, self).__init__()
		self.num_tweets=0
		self.maxTweets=3

	def on_status(self, status):
		print status.text

	def on_data(self, data):
		self.num_tweets=analysis(data,self.num_tweets)
		print "Tweet count: ",self.num_tweets			
		if(self.num_tweets < self.maxTweets):
        		return True
    		else:
        		return False

	def on_error(self, status_code):
		print >> sys.stderr, 'Encountered error with status code:', status_code
		return True # Don't kill the stream

	def on_timeout(self):
		print >> sys.stderr, 'Timeout...'
		return True #Don't kill the stream


def main(keyword):
	auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api=tweepy.API(auth)
	engine=tweepy.streaming.Stream(auth, CustomStreamListener())
	engine.filter(track=list([keyword]))
	
		

def tweetcode(request,keyword):
	allData.cleanTweets()
	main(keyword)
	return HttpResponse(allData.getJSON())
