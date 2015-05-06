The folder contains the following programs
            1. Tweet.java
            2. Database.java
            3. index.jsp

The file Database.java creates a DynamoDB table on AWS and stores the TweetID, keyword, latitude, longitude and time
The file Tweet.java generates the stream of tweets and Database.java stores the attributes of tweets mentioned above in the DynamoDB table
The file index.jsp creates an object of the class Tweet to get the tweets in real-time and plots the location based on latitiude
and longitude details fetched from the database on the google map. The plots are shown using markers.


To execute,
            build project
            run on AWS Tomcat Server
            



            