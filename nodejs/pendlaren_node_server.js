var admin = require("firebase-admin");
const http = require('http');
//let {PythonShell} = require('python-shell')
var serviceAccount = require("../../key/skanependlaren-firebase-adminsdk-xemd8-4c798104f8.json");
var fs = require('fs');
var savepath = '../../userdata/data/'
//var mltrainer = '../ml/pendlaren_FastAI.py'
//var mlpredictor = '../ml/pendlaren_FastAI_predict.py'
//verbose = true; //Sends more information to Node server
column_names = "detectedActivity,longitude,latitude,geoHash,locationAccuracy,time,minuteOfDay,weekday,monthday,detectedActivityConfidence,journey";
column_names_prediction = "detectedActivity,longitude,latitude,geoHash,locationAccuracy,time,minuteOfDay,weekday,monthday,detectedActivityConfidence,predictedjourney,accuracy";
console.log(new Date().toUTCString()+","+Date.now()+",,Node server starting")
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://skanependlaren.firebaseio.com"
});

var db = admin.database();
var userRef = db.ref("users");
var userSettingsRef = db.ref("userSettings");
var predictRef = db.ref("predict");
var refLearning = db.ref("learningdata");

//Listen for new user
userRef.on("child_added", function(snapshot) {
   userRef.child(snapshot.key).update({
          clear:false,
          train:false,
          update_training_settings:false,
        });
        db.ref("userSettings").child(snapshot.key).update({   //test to predict first time could check if model exists first but how??
            modelExists:true,
        });
});

//All stuff related to a users status change 
userRef.on("child_changed", function(snapshot,prevChildKey) {
  var id = snapshot.key;
  if(id.length==28){  //Then it is a command node
      var clear = false;
      var train = false;
      var update_training_settings = false;
      snapshot.forEach(function(data) {
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
        console.log(new Date().toUTCString()+","+Date.now()+","+id+",,ERROR: The combination for user: train="+train+
        " clear="+clear+" update_training_settings="+update_training_settings+" should not occur");
      }
  }
});

userRef.on("child_removed", function(snapshot) {
    console.log(new Date().toUTCString()+","+Date.now()+","+snapshot.key+",,:User removed");
});

//Listen for new prediction
predictRef.on("child_added", function(snapshot) {
  doPrediction(snapshot.key,snapshot.val());
  predictRef.child(snapshot.key).remove();
});

//Remove retrain??
function callTrain(id,retrain){
    if (retrain){
        console.log(new Date().toUTCString()+","+Date.now()+","+id+",callTrain,Retraining model for user with updated parameters started.");
    }else{
        console.log(new Date().toUTCString()+","+Date.now()+","+id+",callTrain,Retraining model for user.");
    }
    var timeStart=Date.now();
    db.ref("userSettings").child(id).once("value")
        .then(function(snapshot){
            http.get('http://127.0.0.1:5000/retrain?userId='+id, (resp) => {
            let data = '';
            resp.on('data', (chunk) => {
                data += chunk;
            });
            // The whole response has been received. Print out the result.
            resp.on('end', () => {
                var timeTakenForTraining = (Math.round((Date.now()-timeStart)/(1000))); //In seconds 
                //console.log(data);
                trainingResult = JSON.parse(data)
                if (trainingResult.error == 0){
                    console.log(new Date().toUTCString()+","+Date.now()+","+id+",callTrain,Done training");
                    if(retrain){
                        db.ref("users").child(id).update({
                            update_training_settings:false,
                        });
                    }else{
                        userRef.child(id).update({
                          train:false
                        });
                    }
                    db.ref("userSettings").child(id).update({
                        modelExists:true,
                        modelCreatedTime: admin.database.ServerValue.TIMESTAMP,
                    });
                }else if(trainingResult.error == 1){
                    console.log(new Date().toUTCString()+","+Date.now()+","+id+",callTrain,Training file not found");
                    userRef.child(id).update({
                        train:false
                    });
                }else if (trainingResult.error == 2){
                    console.log(new Date().toUTCString()+","+Date.now()+","+id+",callTrain,Unknown training error 1");
                    userRef.child(id).update({
                        train:false
                    });
                }else{
                    console.log(new Date().toUTCString()+","+Date.now()+","+id+",callTrain,Unknown training error 2");
                    userRef.child(id).update({
                        train:false
                    });
                }
            });
            }).on("error", (err) => {
              console.log(new Date().toUTCString()+","+Date.now()+","+id+",callTrain,Error in connection");
            });
    });
}


function callDeleteUser(id){
  console.log(new Date().toUTCString()+","+Date.now()+","+id+",callDeleteUser,Deleting user model data and firebase entry for user started.");
  http.get('http://127.0.0.1:5000/delete?userId='+id, (resp) => {
    let data = '';
    // A chunk of data has been recieved.
    resp.on('data', (chunk) => {
        data += chunk;
    });
    resp.on('end', () => {
        trainingResult = JSON.parse(data)
        if (trainingResult.error == 0){
            userRef.child(id).update({   //I have to do this first to get a handle so I can delet
              clear:false
            });
            userRef.child(id).remove();
            /*userSettingsRef.child(id).update({   //If removed everything gets back to standard UI so let this stay in firebase.
              modelExists:true
            });
            userSettingsRef.child(id).remove(); //Check if works....*/
        }else if(trainingResult.error == 1){ //IF no training has taken place we are here 
            console.log(new Date().toUTCString()+","+Date.now()+","+id+",callDeleteUser,Unknown deleting error 1 no data saved remove other stuff");
        }else{
            console.log(new Date().toUTCString()+","+Date.now()+","+id+",callDeleteUser,Unknown deleting error 2 callDeletUser");
        }
        
    });
    }).on("error", (err) => {
      console.log(new Date().toUTCString()+","+Date.now()+","+id+",callDeleteUser,Error in connection callDeletUser");
    });
}


function doPrediction(id,val){
//Check which parameters are active and that no training is currently active or just try????.
    db.ref("userSettings").child(id).once("value")
        .then(function(snapshot){
            var modelExists = snapshot.child("modelExists").val();
            var timeStart=Date.now();
            //'&geoHash='+val.geoHash+
            if (modelExists){
                console.log(new Date().toUTCString()+","+Date.now()+","+id+",doPrediction,Model exists");
                http.get('http://127.0.0.1:5000/predict?userId='+id+
                '&detectedActivity='+val.detectedActivity+
                '&longitude='+val.longitude+
                '&latitude='+val.latitude+
                '&minuteOfDay='+val.minuteOfDay+
                '&weekday='+val.weekday, (resp) => {
                    let data = '';
                    // A chunk of data has been recieved.
                    resp.on('data', (chunk) => {
                        data += chunk;
                    });
                    resp.on('end', () => {
                        predictionResult = JSON.parse(data)
                        var timeTakenForPrediction = (Math.round((Date.now()-timeStart)/(1000))); //In seconds 
                            if (predictionResult.error == 0){
                                /*console.log("Predicted for :"+id+
                                            " at time: "+new Date().toUTCString()+
                                            " from: "+predictionResult.fromStation+
                                            " to: "+predictionResult.toStation+
                                            " with probability: "+predictionResult.probability+
                                            " prediction took: "+timeTakenForPrediction+"s");*/
                                console.log(new Date().toUTCString()+","+Date.now()+","+id+",doPrediction,predicted");
                                savePrediction(id,val,predictionResult)
                                db.ref("result").child(id).child("new").set({
                                    probability: Math.round(predictionResult.probability*100),
                                    from:predictionResult.fromStation,
                                    to:predictionResult.toStation,
                                    time:admin.database.ServerValue.TIMESTAMP,
                                    timeTaken:timeTakenForPrediction
                                });
                                db.ref("userSettings").child(id).update({   //PRediction worked som model exists
                                    modelExists:true,
                                });
                            }else if(predictionResult.error == 1){
                                console.log(new Date().toUTCString()+","+Date.now()+","+id+",doPrediction,no id");
                            }else if (predictionResult.error == 2){
                                console.log(new Date().toUTCString()+","+Date.now()+","+id+",doPrediction,Prediction error or no trained mode found");
                                db.ref("userSettings").child(id).update({   //Disable prediction for user
                                    modelExists:false,
                                });
                            }else{
                                console.log(new Date().toUTCString()+","+Date.now()+","+id+",doPrediction,Unknown prediction error");
                            }
                            //console.log(data);
                        });
                    }).on("error", (err) => {
                        console.log(new Date().toUTCString()+","+Date.now()+","+id+",doPrediction,Error in connection doPrediction");
                    });
            }else{
                console.log(new Date().toUTCString()+","+Date.now()+","+id+",doPrediction,No model exists");
                db.ref("userSettings").child(id).update({   //test to predict
                    modelExists:false,
                });
            }
    });
}


//New learning or teaching data arrived below this point 

var added =0;
var saved=0;
refLearning.on("child_added", function(snapshot, prevChildKey) {
    added=added+1;
    if(snapshot.val().monthday==-1){  //This is teaching data
        if (fs.existsSync(savepath+snapshot.val().uid+"_teach.csv")){
            addit(savepath+snapshot.val().uid+"_teach.csv",snapshot);
        }else{
            fs.appendFileSync(savepath+snapshot.val().uid+"_teach.csv",column_names+"\n");
            addit(savepath+snapshot.val().uid+"_teach.csv",snapshot);
        }
    }else{ //Search data
        if (fs.existsSync(savepath+snapshot.val().uid+".csv")){
            addit(savepath+snapshot.val().uid+".csv",snapshot);
        }else{
            fs.appendFileSync(savepath+snapshot.val().uid+".csv",column_names+"\n");
            addit(savepath+snapshot.val().uid+".csv",snapshot);
        }
    }
    refLearning.child(snapshot.key).remove()
    .then(function() {
      //console.log("Remove succeeded.")
    }).catch(function(error) {
      //console.log("Remove failed: " + error.message)
    });
});


//New learning data added
refLearning.on("child_removed", function(snapshot, prevChildKey) {
  saved=saved+1;
  var result = added-saved;
  //console.log("Data saved for user: "+snapshot.val().uid+" total saved in this session: "+ saved + " not removed "+ result);
  //When retrain timer is started
  //updateTimeOrAddNewTraining(snapshot.val().uid);
});

function addit(filepathname,snapshot){
        fs.appendFileSync(filepathname,+
           snapshot.val().detectedActivity+","+
           snapshot.val().longitude+","+
           snapshot.val().latitude+","+
           snapshot.val().geoHash+","+
           snapshot.val().locationAccuracy+","+
           snapshot.val().time+","+
           snapshot.val().minuteOfDay+","+
           snapshot.val().weekday+","+
           snapshot.val().monthday+","+
           snapshot.val().detectedActivityConfidence+","+
           //snapshot.val().uid+
           snapshot.val().startStation+snapshot.val().endStation+
           "\n");
}   

function savePrediction(id,val,predictionResult){
    var filenamePath = savepath+id+"_predict.csv";
    if (!fs.existsSync(filenamePath)){
            fs.appendFileSync(filenamePath,column_names_prediction+"\n");
    }
    fs.appendFileSync(filenamePath,+
        val.detectedActivity+","+
        val.longitude+","+
        val.latitude+","+
        val.geoHash+","+
        val.locationAccuracy+","+
        val.time+","+
        val.minuteOfDay+","+
        val.weekday+","+
        val.monthday+","+
        val.detectedActivityConfidence+","+
        predictionResult.fromStation+predictionResult.toStation+","+
        predictionResult.probability+
        "\n");
}
//*************************************************************//
//MISC
//FIX handles automatic retraining of the model
//Should not be active for now.
//Timer code
var timerObjects = [];
minute = 60*1000;
hour = minute*60;
retrainAge = hour*1.5; //Retrain if age is > retrainAge
//Start the timertask
//var guid = setInterval(retrainModel,minute) ;

function TimerObject(id, retrainTime) {
    this.id = id;
    this.retrainTime = retrainTime;
    this.getId = function() {
        return id;
    }
}

/*Searches for a saved retrain command for a pendlarUser (the user is identified with id)
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
  //console.log("Checking if retrain is needed (for users with last OD search older than "+Math.round(retrainAge/minute)+ " minutes) time now: "+ new Date());
    for (var i = timerObjects.length; i --;){
      var diff = new Date().getTime()-timerObjects[i].retrainTime;
      //console.log("Last search from user : "+timerObjects[i].id+" was made : "+Math.round(diff/(1000*60))+ " minutes ago.");
      if(diff>retrainAge){
        //console.log("Time to train and remove: "+timerObjects[i].id);
        //This is a auomatic retrain an should not include retrain
        userRef.child(timerObjects[i].id).update({
          train:true
        });
        timerObjects.splice(i,1);
      }
    }
}
