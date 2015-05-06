<!DOCTYPE html>

<%@page import="twitterMap.Tweet"%>
<html>
<head>
<script
src="https://maps.googleapis.com/maps/api/js">
</script>
<body>
<div id="googleMap" style="width: 2000px; height: 950px;"></div>
<center>
<form>
<select name=option onchange='OnChange(this.form.option);'>
<option>Choose keyword...</option>
<option>food</option>
<option>beer</option>
<option>pizza</option>
<option>apple</option>
<option>music</option>
<option>soccer</option>
<option>modi</option>
</select>
</form>
</center>
</body>


<script src="https://sdk.amazonaws.com/js/aws-sdk-2.0.22.min.js"></script>
<script>
var mapProp = {
center:new google.maps.LatLng(0, 0),
zoom:3,
mapTypeId:google.maps.MapTypeId.HYBRID
};
var map=new google.maps.Map(document.getElementById("googleMap")
                            ,mapProp);
                           
var yellow = 'http://maps.google.com/mapfiles/ms/micons/yellow.png';
var red = 'http://maps.google.com/mapfiles/ms/micons/red.png';
var img_red = document.createElement('img');
var img_yellow = document.createElement('img');
img_red.src = red;
img_yellow.src = yellow;
function OnChange(dropdown)
{
    var myindex  = dropdown.selectedIndex
    var SelValue = dropdown.options[myindex].value
    console.log(SelValue);
    
    initialize(SelValue);
    <%@page language="java" import="java.util.*"%>
    <%@page import="twitter4j.*"%>
    
    <%Tweet tweet = new Tweet();%>
    <%tweet.start();%>
    return true;
}
markers = [];
function setAllMap(map) {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
    }
}
function clearMarkers() {
    setAllMap(null);
    markers = [];
}

function initialize(displayKeyword)
{
    
    
    AWS.config.update({accessKeyId: 'AKIAJV3QWERLWYEGS7UQ', secretAccessKey: '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'});
    AWS.config.region = 'us-east-1';
    var db = new AWS.DynamoDB();
    db.listTables( function (err, data) {
                  
                  if (err){
                  alert(err);
                  }
                  else {
                  console.log(data.TableNames);
                  
                  }
                  });
    lastEvalKey = 0;
    
    
    var params = {
    TableName: 'TwitterTable',
    AttributesToGet: ['tweetId', 'keyword', 'latitude', 'longitude', 'time'],
    Limit: 354,
       
    }
    
    coords = [];
    labels = [];
    iterator = 0;
    iterator_coords = 0;
    db.scan(params, function(err, data) {
            
            if (err)
            console.log(err);
            else
            console.log("last count: " + data.Count);
            
            
            for (var ii in data.Items) {
            var newTweet = data.Items[ii];
            var LatLong= new google.maps.LatLng(parseFloat(newTweet.latitude.S), parseFloat(newTweet.longitude.S));
            var tweetkeyword = newTweet.keyword.S
            if(tweetkeyword == displayKeyword) {
            
            coords.push(LatLong);
            labels.push(tweetkeyword);
            console.log("Coordinate" + coords[iterator_coords]);
            
            }
            iterator_coords++;
            }
            console.log("Coords length: " + coords.length);
            
            var i = 0;
            
            clearMarkers();
            
            for(i=0;i<coords.length;i++ ) {
            var cur_image = yellow;
            markers.push(new google.maps.Marker({
                                                position: coords[iterator],
                                                map: map,
                                                draggable: true,
                                                title: labels[iterator],
                                                icon: cur_image
                                                }));
            iterator++;
            }	  
            
            });
    
    
}
</script>
</head>
</html>
<!-- !DOCTYPE html> -->

<html>
<head>
<meta charset="UTF-8">
<title>TwittMap</title>
<script type="text/javascript">
//window.setTimeout(function(){ document.location.reload(true); }, 15000);
</script>
</head>
<body>

</body>
</html>