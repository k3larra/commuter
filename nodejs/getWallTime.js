const http = require('http');
//setInterval(predict, 2000);

function getPrediction(id,detectedActivity,geoHash,minuteOfDay,weekday) {
    console.log("Go");
    http.get('http://127.0.0.1:5000/predict?userId='+id+'&detectedActivity='+detectedActivity+'&geoHash='+geoHash+'&minuteOfDay='+minuteOfDay+'&weekday='+weekday, (resp) => {
    let data = '';
    // A chunk of data has been recieved.
    resp.on('data', (chunk) => {
        data += chunk;
    });

    // The whole response has been received. Print out the result.
    resp.on('end', () => {
        //console.log(JSON.parse(data));
        console.log(data);
    });
    }).on("error", (err) => {
      console.log("Error:0");
    });
}

function doTraining(id) {
    console.log("DoIt");
    http.get('http://127.0.0.1:5000/retrain?userId='+id, (resp) => {
    let data = '';
    // A chunk of data has been recieved.
    resp.on('data', (chunk) => {
        data += chunk;
    });

    // The whole response has been received. Print out the result.
    resp.on('end', () => {
        //console.log(JSON.parse(data));
        console.log(data);
    });
    }).on("error", (err) => {
      console.log("Error:0");
    });
}

//getPrediction('tnK534JMwwfhvUEycn69HPbhqkt2',2,3,1242479403,485,1)
//getPrediction('ehaBtfOPDNZjzy1MEvjQmGo4Zv12',3,1242478163,840,1) //8115681079
//getPrediction('hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2',7,1242199659,1165,3) //,8004980338
doTraining('ehaBtfOPDNZjzy1MEvjQmGo4Zv12')
//doTraining('tnK534JMwwfhvUEycn69HPbhqkt2')