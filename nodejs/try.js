let {PythonShell} = require('python-shell')
let options = {
  pythonOptions: ['-u'], // get print results in real-time
};
var pyshell = new PythonShell('try.py', options);


//setInterval(predict, 2000);

function predict() {
    console.log("Go");
    //pyshell.send(JSON.stringify([4,1242481883,1163,6]));
}

pyshell.send(JSON.stringify([4,1242481883,1163,6]));

pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
});

// end the input stream and allow the process to exit
pyshell.end(function (err) {
    if (err){
        throw err;
    };

    console.log('finished');
});


/*let {PythonShell} = require('python-shell')
var python_process;
var pyshell = new PythonShell('../code/commuter.py');
python_process = pyshell.childProcess;
console.log("hepp")
//python_process.from_to_id("journey")*/