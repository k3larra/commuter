var admin = require("firebase-admin");
var PythonShell = require('python-shell');
var serviceAccount = require("../../key/skanependlaren-firebase-adminsdk-xemd8-4c798104f8.json");
//const bigquery = require('@google-cloud/bigquery')();
//const dataset = bigquery.dataset('commuting');
verbose = true; //Sends more information to Node server

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://skanependlaren.firebaseio.com"
});

var db = admin.database();
var userRef = db.ref("users");
var predictRef = db.ref("predict");

//Listen for new user
userRef.on("child_added", function(snapshot) {
   console.log("User: "+snapshot.key+" added.");
   const tableId = snapshot.key;
   const table = dataset.table(tableId);
   table.exists().then(function(data){
       if(data[0]){
            console.log("Table for user: "+snapshot.key+" exists");
       }else{
           console.log("Table for user: "+snapshot.key+" exist and is created");
           createTable(tableId);
       }
   })
   //Starting server or new user resetting all setting data to false...
   //console.log("User: "+snapshot.key+" added.");
   userRef.child(snapshot.key).update({
          clear:false,
          train:false,
          update_training_settings:false,
        });
        db.ref("userSettings").child(snapshot.key).update({   //test to predict first time could check if model exists first but how??
            modelExists:true,
        });
});

userRef.on("child_changed", function(snapshot,prevChildKey) {
  var id = snapshot.key;
  if(id.length==28){  //Then it is a command node
      var clear = false;
      var train = false;
      var update_training_settings = false;
      snapshot.forEach(function(data) {
        //console.log("The " + data.key + " has value " + data.val());
            if(data.key=="clear"){
                clear = data.val();
            }else if(data.key=="train"){
                train = data.val();
            }else if(data.key=="update_training_settings"){
                update_training_settings=data.val();
            }
      });
      if(clear&&!train&&!update_training_settings){
        callDeleteUser(id);
      }else if(!clear && train && !update_training_settings){
        callTrain(id,false);
      }else if (!clear && !train && update_training_settings){
        callTrain(id,true);
      }else if (!clear && !train && !update_training_settings){
      }else{
        console.log("ERROR: The combination for user: "+id+" train="+train+
        " clear="+clear+" update_training_settings="+update_training_settings+" should not occur");
      }
  }
});

userRef.on("child_removed", function(snapshot) {
    console.log("User: " + snapshot.key+" removed");
});

//Listen for new prediction
predictRef.on("child_added", function(snapshot) {
  doPrediction(snapshot.key,snapshot.val());
  predictRef.child(snapshot.key).remove();
});

//Training incremental or retrain
function callTrain(id,retrain){
    //Perhaps check if user is in retrain list and remove it will retrain again otherwise. 
    //This ocurs if retrain is made manually.
    if (retrain){
        console.log("Retraining model for user : "+id+" with updated parameters started.");
    }else{
        console.log("Retraining model for user : "+id+" parameters not changed.");
    }
    var timeStart=Date.now();
    db.ref("userSettings").child(id).once("value")
        .then(function(snapshot){
            var useActivity = snapshot.child("useActivity").val();
            var useLocation = snapshot.child("useLocation").val();
            var useWeekday = snapshot.child("useWeekday").val();
            var useTime = snapshot.child("useTime").val();
            console.log("useActivity: "+useActivity+ " useLocation: "+useLocation+" useWeekday: "+useWeekday+" useTime: "+useTime);
            var options = {
                mode: 'text',
                pythonPath: '/usr/bin/python2.7',
                //pythonOptions: ['-u'],
                args: ['-i',id,'-a',useActivity,'-l',useLocation,'-w',useWeekday,'-t',useTime,'-r',retrain]
            };
            //console.log(options);
            PythonShell.run('pendlaren_TF16.py', options, function (err, results) {
              var timeTakenForTraining = (Math.round((Date.now()-timeStart)/(1000*60))); //In minutes  
              console.log("Model for user "+id+" created in "+timeTakenForTraining+" minutes");
              if (results){
                console.log('results: %j', results);
              }
              if (err) {
                  if (String(err).includes("Your CPU supports instructions")){
                        console.log("WARNING: No GPU on server");
                  }else{
                   console.log("Tensorflow returned with the error:"+err);
                  }
              }
              if(retrain){
                  db.ref("users").child(id).update({
                      update_training_settings:false,
                  });
              }else{
                    userRef.child(id).update({
                      train:false
                    });
              }
              db.ref("userSettings").child(id).update({   //test to predict
                    modelExists:true,
                    modelCreatedTime: admin.database.ServerValue.TIMESTAMP,
              });
            });

    });
}


function callDeleteUser(id){
  console.log("Deleting user, model and BigQuery dat for user : "+id+" started.");
        var options = {
          mode: 'text',
          pythonPath: '/usr/bin/python2.7',
          pythonOptions: ['-u'],
          args: ['-u',id]
        };

    PythonShell.run('pendlaren_deleteUser.py', options, function (err, results) {
      console.log('results: %j', results);
      if (err) {
        console.log("Tensorflow threw the error:"+err);
      }
      userRef.child(id).update({
          clear:false
            });
            userRef.child(id).remove();
      });
}



function doPrediction(id,val){
//Check which parameters are active and that no training is currently active or just try????.
    db.ref("userSettings").child(id).once("value")
        .then(function(snapshot){
            var useActivity = snapshot.child("useActivity").val();
            var useLocation = snapshot.child("useLocation").val();
            var useWeekday = snapshot.child("useWeekday").val();
            var useTime = snapshot.child("useTime").val();
            var modelExists = snapshot.child("modelExists").val();
            //console.log("useActivity: "+useActivity+ " useLocation: "+useLocation+" useWeekday: "+useWeekday+" useTime: "+useTime);
            //Only use prediction settings asked for
            if(!useActivity){
               delete val["detectedActivity"]
            }
            if(!useLocation){
               delete val["geoHash"]
            }
            if(!useTime){
               delete val["minuteOfDay"]
            }
            if(!useWeekday){
               delete val["weekday"]
            }
            var timeStart=Date.now();
            const exec = require('child_process').exec;
            fs = require('fs');
            fs.writeFile('pendlaren/'+id+'/pred.json', JSON.stringify(val), function (err) {
                if (err)
                    return console.log("The file could not be written a probable cause is that no training has taken place");
                console.log('Asking prediction for user '+id+" using data "+JSON.stringify(val));
            });
            if(modelExists){
                const testscript = exec('./pendlaren_prediction_local.sh pendlaren/'+id+"/");
                //Run the script and write data to firebase
                testscript.stdout.on('data', function(data){
                    try {
                        var myJSONObj = JSON.parse(data);
                        var probArray = myJSONObj.predictions[0].probabilities
                        var result = myJSONObj.predictions[0].classes
                        var ids = myJSONObj.predictions[0].class_ids
                        var prediction = result[0]
                        var maxProbability = probArray[ids[0]]
                        var fromStation = (prediction).substring(0,5);
                        var toStation = (prediction).substring(5,10);
                        var timeTakenForPrediction = (Math.round((Date.now()-timeStart)/1000));
                        console.log("Predicted for :"+id+" from: "+fromStation+" to: "+toStation+" with probability: "+
                                    maxProbability+" prediction took: "+timeTakenForPrediction+"s");
                        db.ref("result").child(id).child("new").set({
                                    probability: Math.round(maxProbability*100),
                                    from:fromStation,
                                    to:toStation,
                                    time:admin.database.ServerValue.TIMESTAMP,
                                    timeTaken:timeTakenForPrediction
                            });
                         db.ref("userSettings").child(id).update({   //test to predict
                            modelExists:true,
                         });
                    } catch (e){
                        console.log(e);
                        console.log("Set modelExists to false for user: "+id);
                        db.ref("userSettings").child(id).update({   //test to predict
                            modelExists:false,
                        });
                    }
                });
                testscript.stderr.on('data', function(data){
                    if(data.includes("Failed to load model")){
                        console.log("ERROR: Failed to load model for user: "+id+" set modelExists to false");
                        console.log(data);
                        db.ref("userSettings").child(id).update({   //test to predict
                             modelExists:false,
                        });
                    }else if (data.includes("Your CPU supports instructions")){
                        console.log("WARNING: No GPU on server");
                    }else if (data.includes("Unable to read file")){
                        //console.log("No trained model");
                    }else if (data.includes("WARNING")){
                        console.log("WARNING: Prediction for user: "+id+" failed with data "+data);
                    }else if (data.includes("ERROR")){
                        console.log("ERROR: Prediction for user: "+id+" failed with data "+data);
                    }else{
                       console.log("Prediction for user: "+id+" failed with data "+data);
                    }
                });
            }else{
                 console.log("No model exists");
            }
    });
}

function createTable(tableId){
    //const dataset = bigquery.dataset('commuting');
    const options = {"schema": {
        "fields":[
          {
            "mode": "NULLABLE",
            "name": "detectedActivity",
            "type": "INTEGER"
          },
          {
            "mode": "NULLABLE",
            "name": "startStation",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "endStation",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "longitude",
            "type": "FLOAT"
          },
          {
            "mode": "NULLABLE",
            "name": "latitude",
            "type": "FLOAT"
          },
          {
            "mode": "NULLABLE",
            "name": "geoHash",
            "type": "INTEGER"
          },
          {
            "mode": "NULLABLE",
            "name": "locationAccuracy",
            "type": "INTEGER"
          },
          {
            "mode": "NULLABLE",
            "name": "time",
            "type": "INTEGER"
          },
          {
            "mode": "NULLABLE",
            "name": "detectedActivityConfidence",
            "type": "INTEGER"
          },
          {
            "mode": "NULLABLE",
            "name": "uid",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "minuteOfDay",
            "type": "INTEGER"
          },
          {
            "mode": "NULLABLE",
            "name": "weekday",
            "type": "INTEGER"
          },
          {
            "mode": "NULLABLE",
            "name": "monthday",
            "type": "INTEGER"
          }
        ]
    }
    }
    dataset.createTable(tableId,options).then(function(data){
        if(data[0]){
            console.log("Table: "+tableId+" created");
        }else{
            console.log("Could not create: "+tableId);
        }
    });
}


var refLearning = db.ref("learningdata");
var added =0;
var saved=0;

//New learning data requested to add to BigQuery
refLearning.on("child_added", function(snapshot, prevChildKey) {
  added=added+1;
  //Here I could clean up Firebase and remove stray entries.
});

//New learning data addded BigQuery
refLearning.on("child_removed", function(snapshot, prevChildKey) {
  saved=saved+1;
  var result = added-saved;
  console.log("Search saved for user: "+snapshot.val().uid+" total saved in this session: "+ saved + " not removed "+ result);
  //When retrain timer is started
  updateTimeOrAddNewTraining(snapshot.val().uid);
});

//Timer code
var timerObjects = [];
minute = 60*1000;
hour = minute*60;
retrainAge = hour*1.5; //Retrain if age is > retrainAge
//Start the timertask
var guid = setInterval(retrainModel,minute) ;
//if I need to stop it
//clearInterval(guid)?????

function TimerObject(id, retrainTime) {
    this.id = id;
    this.retrainTime = retrainTime;
    this.getId = function() {
        return id;
    }
}

/*Searaches for a saved retrain command for a pandlarUser (the user is identified with id)
if the user is found in the list the retrainTime is updated (This reflects that the app is in use)
adds a new retrain command if no exists. (Reflects that new searches are done)*/
function updateTimeOrAddNewTraining(id){
  var found = false;
  for (var i = 0; i < timerObjects.length; i = i + 1){
    if (timerObjects[i].id===id){
      found = true;
      timerObjects[i].retrainTime = new Date().getTime();
    }
  }
  if(found===false){
    timerObjects.push(new TimerObject(id,new Date().getTime()));
  }
}

/*Time it is time for retraining model
This is done if entry is older than retrainTime*/
function retrainModel(){
    
  console.log("Checking if retrain is needed (for users with last OD search older than "+Math.round(retrainAge/minute)+ " minutes) time now: "+ new Date());
    for (var i = timerObjects.length; i --;){
      var diff = new Date().getTime()-timerObjects[i].retrainTime;
      console.log("Last search from user : "+timerObjects[i].id+" was made : "+Math.round(diff/(1000*60))+ " minutes ago.");
      if(diff>retrainAge){
        console.log("Time to train and remove: "+timerObjects[i].id);
        //This is a auomatic retrain an should not include retrain
        userRef.child(timerObjects[i].id).update({
          train:true
        });
        timerObjects.splice(i,1);
      }
    }
}


