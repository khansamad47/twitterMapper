package twitterMap;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import twitter4j.Status;

import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClient;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.dynamodbv2.model.AttributeDefinition;
import com.amazonaws.services.dynamodbv2.model.AttributeValue;
import com.amazonaws.services.dynamodbv2.model.ComparisonOperator;
import com.amazonaws.services.dynamodbv2.model.Condition;
import com.amazonaws.services.dynamodbv2.model.CreateTableRequest;
import com.amazonaws.services.dynamodbv2.model.KeySchemaElement;
import com.amazonaws.services.dynamodbv2.model.KeyType;
import com.amazonaws.services.dynamodbv2.model.ProvisionedThroughput;
import com.amazonaws.services.dynamodbv2.model.PutItemRequest;
import com.amazonaws.services.dynamodbv2.model.PutItemResult;
import com.amazonaws.services.dynamodbv2.model.ScanRequest;
import com.amazonaws.services.dynamodbv2.model.ScanResult;
import com.amazonaws.services.dynamodbv2.util.Tables;


public class Database {
	long tweetID;
	String[] keyWords={"food","soccer","modi","beer","pizza","apple","music"};
	double latitude;
	double longitude;
	static String tablename="TwitterTable";
	static AmazonDynamoDBClient dynamo = new AmazonDynamoDBClient(new BasicAWSCredentials("AKIAJV3QWERLWYEGS7UQ","8Jfu+3sTSV7m/R2GVKwvDxejMOqitRy/YVAmJImT"));;
	

	static DynamoDB dynamoDB = new DynamoDB(dynamo);

	public static void createDB() {
		ArrayList<AttributeDefinition> attributeDefinitions= new ArrayList<AttributeDefinition>();
		attributeDefinitions.add(new AttributeDefinition().withAttributeName("tweetID").withAttributeType("S"));
		
		ArrayList<KeySchemaElement> keySchema = new ArrayList<KeySchemaElement>();
		keySchema.add(new KeySchemaElement().withAttributeName("tweetID").withKeyType(KeyType.HASH));


		CreateTableRequest request = new CreateTableRequest()
		.withTableName(tablename)
		.withKeySchema(keySchema)
		.withAttributeDefinitions(attributeDefinitions)
		.withProvisionedThroughput(new ProvisionedThroughput()
		.withReadCapacityUnits(5L)
		.withWriteCapacityUnits(6L));
		boolean check = Tables.doesTableExist(dynamo, tablename);
		if (!check)
		{Table table = dynamoDB.createTable(request);

		try {
			table.waitForActive();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}


		System.out.println("Table Created");

		}}



	public DynamoDB create() {
		createDB();
		return this.dynamoDB;
	}


	public void insert(Status newtweet)
	{
		
		Map<String, AttributeValue> item = new HashMap <String, AttributeValue>();
		item.put("tweetID", new AttributeValue(Long.toString(newtweet.getId())));
		item.put("keyword", new AttributeValue(keywords(newtweet)));
		item.put("latitude", new AttributeValue(Double.toString(newtweet.getGeoLocation().getLatitude())));
		item.put("longitude", new AttributeValue(Double.toString(newtweet.getGeoLocation().getLongitude())));
		item.put("time", new AttributeValue(newtweet.getCreatedAt().toString()));
		

		PutItemRequest putItemRequest = new PutItemRequest(tablename, item);
		PutItemResult putItemResult = dynamo.putItem(putItemRequest);
		try{
			putItemResult = dynamo.putItem(putItemRequest);
		}
		catch (Exception e){
			System.out.println("Unable to insert record");
		

		}
		System.out.println("Entry inserted");
	}

	public String keywords(Status tweet)
	{
		String tweet1=tweet.getText();
		String keyword1=null;
		for (int i=0;i<keyWords.length;i++)
		{

			if(tweet1.contains(keyWords[i]))
			{ keyword1=keyWords[i];
			break;}
		}
		if (keyword1==null)
			keyword1="no keyword";
		return keyword1;

	}


	/*public void getitems(String givekeyword)
	{
		HashMap<String, Condition> scanFilter = new HashMap<String, Condition>();
		Condition condition = new Condition()
		.withComparisonOperator(ComparisonOperator.EQ.toString())
		.withAttributeValueList(new AttributeValue().withS(givekeyword));
		scanFilter.put("keyword", condition);
		ScanRequest scanRequest = new ScanRequest(tablename).withScanFilter(scanFilter);
		ScanResult scanResult = dynamo.scan(scanRequest);
		System.out.println("Count "+scanResult.getCount());
		for (Map<String,AttributeValue> entry : scanResult.getItems())
		{
			AttributeValue lat = entry.get("latitude");
			AttributeValue lon = entry.get("longitude");
			System.out.println("Latitude "+lat.toString()+" Longitude "+lon.toString());
		}

	}

	public static void main(String[] args)
	{
		Database db1=new Database();
		db1.getitems("food");
	} */
}




