# twitterMapper
Webinterface on Javascript, Django(python) server. User enters a keyword in the GUI which is then send to the twiiter server to get a live stream of tweets. Tweets are then classified as Positive sentiment or negative sentiment and plotted to the GUI (Google Maps API) where the marker color represents the tweets polarity (green= positive sentiment, red=negative sentiment). The classification is done via Naive Bayes (using TextBlob Library, where the classifier has been trained on a movie review data set). For the Tweeter Stream we are using Tweepy which is a free tweeter API but has access to limited tweets. 
