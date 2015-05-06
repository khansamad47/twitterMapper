package twitterMap;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.model.AttributeDefinition;
import com.amazonaws.services.dynamodbv2.model.AttributeValue;
import com.amazonaws.services.dynamodbv2.model.PutItemRequest;
import com.amazonaws.services.dynamodbv2.model.PutItemResult;

import twitter4j.StallWarning;
import twitter4j.Status;
import twitter4j.StatusDeletionNotice;
import twitter4j.StatusListener;
import twitter4j.TwitterException;
import twitter4j.TwitterStream;
import twitter4j.TwitterStreamFactory;
import twitter4j.conf.ConfigurationBuilder;
import twitter4j.FilterQuery;

/**
 * <p>This is a code example of Twitter4J Streaming API - sample method support.<br>
 * Usage: java twitter4j.examples.PrintSampleStream<br>
 * </p>
 *
 * @author Yusuke Yamamoto - yusuke at mac.com
 */
public class Tweet {
	//static long count =0l;
    /**
     * Main entry of this application.
     *
     * @param args
     */
    public void start() throws TwitterException, IOException, InterruptedException {
    	//just fill this
    	
    /*	Token = new Token("token_access", "token_secret");
    	Credential c = new Credential("user_name", "consumer_key", "consumer_secret", token);
    	UserAccountManager m = UserAccountManager.getInstance(c); */
    	
    	
    	 ConfigurationBuilder cb = new ConfigurationBuilder();
         cb.setDebugEnabled(true)
           .setOAuthConsumerKey("ExxpplqIbj3hHAsr8ANfAS7kR")
           .setOAuthConsumerSecret("bu1tsoPEhT0l6lSWVu0zuzRFLAh6Ppnw4e2ngQrgHcD8NO85NK")
           .setOAuthAccessToken("398584805-7hzJmesi0yr8RxMlblEKkh9x7QqOeVB3InjklJvK")
           .setOAuthAccessTokenSecret("EeY1araZwR3MbnYkDycq74sG5I2Pog37C4pFQ68o7TXrh");
         
         Database db=new Database();
         db.create();
         
        TwitterStream twitterStream = new TwitterStreamFactory(cb.build()).getInstance();
        StatusListener listener = new StatusListener() {
            @Override
            public void onStatus(Status status) {
                
                if (status.getGeoLocation()!=null)
                {
                	System.out.println("@" + status.getUser().getScreenName() + " - " + status.getText());
                	db.insert(status);}
                
               // count=count+status.getText().length();
              //  if (count > 104857600)
                	
                
                      
            }

            @Override
            public void onDeletionNotice(StatusDeletionNotice statusDeletionNotice) {
                System.out.println("Got a status deletion notice id:" + statusDeletionNotice.getStatusId());
            }

            @Override
            public void onTrackLimitationNotice(int numberOfLimitedStatuses) {
                System.out.println("Got track limitation notice:" + numberOfLimitedStatuses);
            }

            @Override
            public void onScrubGeo(long userId, long upToStatusId) {
                System.out.println("Got scrub_geo event userId:" + userId + " upToStatusId:" + upToStatusId);
            }

            @Override
            public void onStallWarning(StallWarning warning) {
                System.out.println("Got stall warning:" + warning);
            }

            @Override
            public void onException(Exception ex) {
                ex.printStackTrace();
            }
        };
        
        
        FilterQuery fq = new FilterQuery();

        String keywords[] = {"food","soccer","modi","beer","pizza","apple","music"};

       // double[][] loc={{-122.75,36.8},{-121.75,37.8}};

        //fq.locations(loc);
        fq.track(keywords);         
        twitterStream.addListener(listener);
      //  twitterStream.sample();
        twitterStream.filter(fq);
        
        
    }
}
