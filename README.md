# twitterMapper
Tweet Sentiment Classifier and Mapper

OVERVIEW:
The user enters a keyword in a text box on our web interface. Our applications takes that keywords and plots tweets related to that keyword on the map embedded into the GUI. Each tweet is represented by a marker and color of the marker highlights the sentiment of the tweet.

UNDER THE HOOD:
We have developed the GUI on Javascript and user Google Maps API for the map.
The server is created using Django(python).
We have used Tweepy to get Twitter Data relating to the keyword.
TextBlob for Sentiment Analysis.
JSON library for transferring data between server and frontend.

MECHANICS
User enters a keyword in the GUI which is then send to our python server.
Python server then send the request to twitter server to get a live stream of tweets.
Incoming Tweets are passed to a function of TextBlob library which calculates polarity from [-1,1] using Naive Bayes
Tweets are then classified as positive, neutral or negative sentiment and plotted to the GUI (Google Maps API) where the marker color represents the tweets polarity (green= positive sentiment, red=negative sentiment).

* The classification is done via Naive Bayes (using TextBlob Library, where the classifier has been trained on a movie review data set). 
* For the Twitter Stream we are using Tweepy which is a free twitter API but has access to limited tweets.


