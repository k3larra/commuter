/* In this program various isolated test regarding the communication between nodejs server and flask server takes place */
const http = require('http');
//setInterval(pred1, 1000);
//setInterval(pred2, 2000);
//setInterval(pred3, 2500);
//setInterval(train1, 10000);
//setInterval(train2, 15000);
//setInterval(train3, 20000);

function getPrediction(id,detectedActivity,geoHash,minuteOfDay,weekday) {
    http.get('http://127.0.0.1:5000/predict?userId='+id+
        '&detectedActivity='+detectedActivity+
        '&geoHash='+geoHash+
        '&minuteOfDay='+minuteOfDay+
        '&weekday='+weekday, (resp) => {
            let data = '';
            // A chunk of data has been recieved.
            resp.on('data', (chunk) => {
                data += chunk;
            });

            // The whole response has been received. Print out the result.
            resp.on('end', () => {
                predictionResult = JSON.parse(data)
                    if (predictionResult.error == 0){
                        console.log("Prediction done for: "+id);
                        console.log("Accuracy: "+predictionResult.probability);
                        console.log("fromStation: "+predictionResult.fromStation);
                        console.log("toStation: "+predictionResult.toStation);
                    }else if(predictionResult.error == 1){
                        console.log("no id: "+id);
                    }else if (predictionResult.error == 2){
                        console.log("Prediction error or no trained mode found for: "+id);
                    }else{
                        console.log("Unknown training error for: "+id);
                    }
                    //console.log(data);
                });
            }).on("error", (err) => {
                console.log("Error in connection for: "+id);
            });
}

function doTraining(id) {
    http.get('http://127.0.0.1:5000/retrain?userId='+id, (resp) => {
    let data = '';
    resp.on('data', (chunk) => {
        data += chunk;
    });
    // The whole response has been received. Print out the result.
    resp.on('end', () => {
        console.log(data);
        trainingResult = JSON.parse(data)
        if (trainingResult.error == 0){
            console.log("Done training for: "+id);
        }else if(trainingResult.error == 1){
            console.log("Training file not found for: "+id);
        }else if (trainingResult.error == 2){
            console.log("Unknown training error for: "+id);
        }else{
            console.log("Unknown error for: "+id);
        }
    });
    }).on("error", (err) => {
      console.log("Error in connection for: "+id);
    });
}

function deleteUser(id){
     http.get('http://127.0.0.1:5000/delete?userId='+id, (resp) => {
    let data = '';
    // A chunk of data has been recieved.
    resp.on('data', (chunk) => {
        data += chunk;
    });
    resp.on('end', () => {
        console.log(data)
        trainingResult = JSON.parse(data)
        if (trainingResult.error == 0){
            console.log("Done deleting: "+id);
        }else if(trainingResult.error == 1){
            console.log("Unknown deleting error for: "+id);
        }else{
            console.log("Unknown error for: "+id);
        }
    });
    }).on("error", (err) => {
      console.log("Error in connection for: "+id);
    });
}
function pred1(){
    getPrediction('tnK534JMwwfhvUEycn69HPbhqkt2',2,3,1242479403,485,1)
}
function pred2(){
    getPrediction('ehaBtfOPDNZjzy1MEvjQmGo4Zv12',3,1242478163,840,1) //8115681079
}
function pred3(){
    getPrediction('hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2',7,1242199659,1165,3)
}
function train1(){
   doTraining('tnK534JMwwfhvUEycn69HPbhqkt2')
}
function train2(){
    doTraining('ehaBtfOPDNZjzy1MEvjQmGo4Zv12')
}
function train3(){
    doTraining('hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2')
}

//getPrediction('tnK534JMwwfhvUEycn69HPbhqkt2',2,3,1242479403,485,1)
//getPrediction('ehaBtfOPDNZjzy1MEvjQmGo4Zv12',3,1242478163,840,1) //8115681079
//getPrediction('hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2',7,1242199659,1165,3) //,8004980338
//doTraining('ehaBtfOPDNZjzy1MEvjQmGo4Zv12')
//doTraining('tnK534JMwwfhvUEycn69HPbhqkt2')
//doTraining('hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2')
//getPrediction()
deleteUser('eXJPoWYDxIc76uemE7Vk3ovBTEG2')