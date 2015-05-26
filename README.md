Description
==========
In this project read tweets associated with an entered keyword by the user from the Twitter Python API and compute sentiments of the tweet text using a classification algorithm. Other information such as the location coodinates, handle of user are also stored and plotted on Google Maps. Each tweet is represented by a marker where the color of the marker highlights the sentiment of the tweet  (green – positive sentiment, red – negative sentiment). This enables us to have location wise sentiments for any input query given by the user.

Under The Hood
==============
We have developed the GUI on Javascript and user Google Maps API for the map. The server is created using Django(python). We have used Tweepy to get Twitter Data relating to the keyword. TextBlob for Sentiment Analysis. JSON library for transferring data between server and frontend.

Mechanics 
==========
User enters a keyword in the GUI which is then send to our python server. Python server then send the request to twitter server to get a live stream of tweets. Incoming Tweets are passed to a function of TextBlob library which calculates polarity from [-1,1] using Naive Bayes Tweets are then classified as positive, neutral or negative sentiment and plotted to the GUI (Google Maps API) where the marker color represents the tweets polarity (green= positive sentiment, red=negative sentiment).

How to use
==========
Make the following changes to twitterMapper/Backend/project/views.py
1) Enter appropriate information in the variables: access_key, access_secret,consumer_key, consumer_secret which can be aquired from Twitter's website.
2) Set variable setTweetCount to the number of tweets you want to grab (set to 3 by default)


Notes
=====
The classification is done via Naive Bayes (using TextBlob Library, where the classifier has been trained on a movie review data set).
For the Twitter Stream we are using Tweepy which is a free twitter API but has access to limited tweets.
