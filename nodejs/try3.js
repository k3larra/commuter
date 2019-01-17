const http = require('http');
//setInterval(predict, 2000);

function getPrediction() {
    console.log("Go");
    //pyshell.send(JSON.stringify([4,1242481883,1163,6]));
}

//getPrediction()


http.get('http://127.0.0.1:5000/predict?detectedActivity=3&geoHash=123456&minuteOfDay=234&weekday=7', (resp) => {
  let data = '';

  // A chunk of data has been recieved.
  resp.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    console.log(JSON.parse(data));
    //console.log(data);
  });

}).on("error", (err) => {
  console.log("Error: " + err.message);
});