/*Used for testing purposes
listens for added search and train data on the connected firebase db
saves to files named as the user uid.csv*/

var admin = require("firebase-admin");
var serviceAccount = require("../../key/skanependlaren-firebase-adminsdk-xemd8-4c798104f8.json");
var fs = require('fs');
results = "Node server starting"
console.log('results: %j', results);

admin.initializeApp({
 credential: admin.credential.cert(serviceAccount),
 databaseURL: "https://skanependlaren.firebaseio.com"
});

var db = admin.database();
var refLearning = db.ref("learningdata");
var added =0;
var saved=0;
var savepath = "saved/"

//New learning data requested to add to BigQuery
refLearning.on("child_added", function(snapshot, prevChildKey) {
  added=added+1;
    //console.log("Found: "+snapshot.val().uid+" not removed ");
    //console.log(snapshot.val());
    if (fs.existsSync(savepath+snapshot.val().uid+".csv")){
        addit(savepath+snapshot.val().uid+".csv",snapshot);
    }else{
        fs.appendFileSync(savepath+snapshot.val().uid+".csv","detectedActivity,geoHash,minuteOfDay,weekday,journey"+"\n");
        addit(savepath+snapshot.val().uid+".csv",snapshot);
    }
});

//The data is removed by another process (currently in pendlaren_node_ server.js) when it has been saved.
refLearning.on("child_removed", function(snapshot, prevChildKey) {
  saved=saved+1;
  var result = added-saved;
  //console.log("Search saved for user: "+snapshot.val().uid+" total saved in this session: "+ saved + " not removed "+ result);
  //When retrain timer is started
});

function addit(filepathname,snapshot){
    if(snapshot.val().monthday==-1){ //This indicates that the entry is created by the teaching interface
        fs.appendFileSync(filepathname,+
           snapshot.val().detectedActivity+","+
           //snapshot.val().longitude+","+
           //snapshot.val().latitude+","+
           snapshot.val().geoHash+","+
           //snapshot.val().locationAccuracy+","+
           //snapshot.val().time+","+
           snapshot.val().minuteOfDay+","+
           snapshot.val().weekday+","+
           
           //snapshot.val().detectedActivityConfidence+","+
           //snapshot.val().uid+
           snapshot.val().startStation+snapshot.val().endStation+
           "\n");
    }   
    //console.log("Wrote for user: "+snapshot.val().uid);
}