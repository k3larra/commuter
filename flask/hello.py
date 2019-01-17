from flask import Flask
from flask import request
import json
from fastai import *         
from fastai.tabular import *
sys.path.append("../code")
from commuter import *

data = TabularDataBunch.load_empty('../models/tnK534JMwwfhvUEycn69HPbhqkt2')
learn = tabular_learner(data, layers=[200,100])
learn.load('tnK534JMwwfhvUEycn69HPbhqkt2');
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Not so good"

@app.route('/retrain/<string:userId>')
def show_post(userId):
    # show the post with the given id, the id is an integer
    return 'Placebholder method for retraining %s' % userId


@app.route('/predict')
def data():
    probability = 0.53
    fromStation = "123456"
    toStation = 23439
    detectedActivity = request.args.get('detectedActivity')
    geoHash = request.args.get('geoHash')
    minuteOfDay = request.args.get('minuteOfDay')
    weekday = request.args.get('weekday')
    if detectedActivity != None and geoHash != None and minuteOfDay != None and weekday != None:
        prediction,accuracy = predict_journey(learn,4,1242481883,1163,6)
        #print json.dumps({"probability": probability, "fromStation": fromStation, "toStation": toStation}, sort_keys=True)
        return json.dumps({"probability": str(accuracy), "fromStation": str(prediction)[0:5], "toStation": str(prediction)[5:10]})
        #return json.dumps({"uoups":str(prediction)[0:5] })
    else:
        return json.dumps({"Undefined error":0 })