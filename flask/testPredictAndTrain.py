from flask import Flask
from flask import request
import json
import shutil
from fastai import *         
from fastai.tabular import *
sys.path.append("../code")
from commuter import *
#model_dir = '../models/'
#data_dir = '../data/'
model_dir = '../../userdata/models/'
data_dir = '../../userdata/data/'
import os
#userId = "tnK534JMwwfhvUEycn69HPbhqkt2"
#data = TabularDataBunch.load_empty(model_dir+userId)
#learn = tabular_learner(data, layers=[200,100])
#learn.load(userId)


dep_var = 'journey'
cat_names = ["detectedActivity","weekday"]
cont_names =["geoHash","minuteOfDay"]
procs = [FillMissing, Categorify, Normalize]

teachingSetName="_teach.csv"
debugging = True 
debugdir = "debug/"

app = Flask(__name__)

#def save_debug_info(user,data):
#        if debugging:
#            file = open(debugdir+user+'.txt', 'a+')
#            file.write(data+"\n")
#            file.close()      

@app.route('/')
def hello_world():
    return "Not so good"

@app.route('/retrain')
def retrain():
    userId = request.args.get('userId')
    if userId != None:
        try:
            teachingSet = pd.read_csv(data_dir+userId+teachingSetName)
            teachingSet= make_shure_we_got_enough_rows(teachingSet)
            valid_idx = list(np.random.randint(0,len(teachingSet),int(len(teachingSet)*0.1)))
            data = (TabularList.from_df(teachingSet, path=model_dir+userId, cat_names=cat_names, cont_names=cont_names, procs=procs)
                .split_by_idx(valid_idx)
                .label_from_df(cols=dep_var)
                .databunch())
            learner=tabular_learner(data, layers=[200,100],metrics=accuracy)
            learner.fit_one_cycle(7)
            learner.save(name=userId)
            data.export()
            return json.dumps({"error":0 })
        except:
            return json.dumps({"error":2 })  # Training error or training file not found
    else:
        return json.dumps({"error":1 })   #no id

@app.route('/predict')
def predict():
    userId = request.args.get('userId')
    if userId != None: 
        detectedActivity = request.args.get('detectedActivity')
        geoHash = request.args.get('geoHash')
        minuteOfDay = request.args.get('minuteOfDay')
        weekday = request.args.get('weekday')
        if detectedActivity != None and geoHash != None and minuteOfDay != None and weekday != None and userId != None:
            try:
                data = TabularDataBunch.load_empty(model_dir+userId)
                learn = tabular_learner(data, layers=[200,100])
                learn.load(userId);
                prediction,accuracy = predict_journey(learn,detectedActivity,geoHash,minuteOfDay,weekday)
                return json.dumps({"probability": str(accuracy), "fromStation": str(prediction)[0:5], "toStation": str(prediction)[5:10],"error":0})
            except:
                return json.dumps({"error":2}) 
        else:
            return json.dumps({"error":1}) #Not all parameters
    else:
        return json.dumps({"error":1})   #no id
    
@app.route('/delete')
def delete():
    print("delete")
    userId = request.args.get('userId')
    if userId != None:
        try:
            shutil.rmtree(model_dir+userId)  #The model
            #oldname = ":"
            for filename in os.listdir(data_dir):
                if filename.startswith(userId):
                    os.remove(data_dir+filename)
            return json.dumps({"error":0})
        except:
            return json.dumps({"error":1})
    else:
        return json.dumps({"error":2})   #no id