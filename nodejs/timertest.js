var admin = require("firebase-admin");
var serviceAccount = require("./key/skanependlaren-firebase-adminsdk-xemd8-4c798104f8.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://skanependlaren.firebaseio.com"
});

var timerObjects = [];
minute = 60*1000;
hour = minute*60;
retrainAge = hour*1.5 //Retrain if age is > retrainAge

function TimerObject(id, retrainTime) {
    this.id = id;
    this.retrainTime = retrainTime;
    this.getId = function() {
        return id;
    }
}

/*Seraches for a saved retrain command for a pandlarUser (the user is identified with id)
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
  console.log("now: "+ new Date());
    for (var i = timerObjects.length; i --;){
      var diff = new Date().getTime()-timerObjects[i].retrainTime;
      console.log("Age in minutes for : "+timerObjects[i].id+" : "+diff/(1000*60));
      if(diff>retrainAge){
        console.log("Train and remove: "+timerObjects[i].id);
        //ToDo add this
        // userRef.child(id).update({
        //  train:true
        //});
        timerObjects.splice(i,1);
      }
    }
  //Remove from here
  //Add a new item
  timerObjects.push(new TimerObject("Alla", new Date().getTime()));
  //update an existing item
  updateTimeOrAddNewTraining("bGUeAsAsLATpsOirdLCkcrtMNAAA");
  //To here
}


//Test part from here
//Add some stuff
timerObjects.push(new TimerObject("XxAWbasBlaP5iiDYGimlQA2rJVE3",1529587750684));
timerObjects.push(new TimerObject("bGUeAsAsLATpsOirdLCkcrtMN323",1529577330241));
timerObjects.push(new TimerObject("kewknfIHuZSkwzQaSwlVTAbQZhy1",1529587750645));
timerObjects.push(new TimerObject("klJPtQ9fGjghoP7HUDY1pB8dUGj2",1529587750643));
timerObjects.push(new TimerObject("oeLUEfxVr3fENaKX5MVNtDvbzUm2",1529587750685));
// Update time on some
updateTimeOrAddNewTraining("bGUeAsAsLATpsOirdLCkcrtMN323");
// Add some 
updateTimeOrAddNewTraining("bGUeAsAsLATpsOirdLCkcrtMNAAA");
updateTimeOrAddNewTraining("bGUeAsAsLATpsOirdLCkcrtMNBBB");
//Test part to here

//Start it runs every minute
var guid = setInterval(retrainModel,minute) ;

//clearInterval(guid)?????
