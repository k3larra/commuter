import os
import sys
import datetime
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
deleted_data_dir = '../../userdata/deleted_data/'
model_dir = '../../userdata/models/'
data_dir = '../../userdata/data/'

dep_var = 'journey'
cat_names = ["detectedActivity","weekday"]
#cont_names =["geoHash","minuteOfDay"]
cont_names =["longitude","latitude","minuteOfDay"]
#usecols=['detectedActivity','geoHash','minuteOfDay','weekday','journey']
usecols=['detectedActivity','longitude','latitude','minuteOfDay','weekday','journey']
procs = [FillMissing, Categorify, Normalize]
teachingSetName="_teach.csv"
#trainedModels = []

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def loadAllModels(model_dir):
    for model_dir_id in get_immediate_subdirectories(model_dir):
        trainedModels.append(Model(model_dir_id,model_dir+model_dir_id))

def updateModel(id):
    found=-1
    for i in range(len(trainedModels)):
        if(trainedModels[i].id == id ):
            found = i
    del trainedModels[found]
    if found > -1:
        trainedModels.append(Model(id,model_dir+id))
    return found

def removeModel(id):
    found=-1
    for i in range(len(trainedModels)):
        if(trainedModels[i].id == id ):
            found = i
    del trainedModels[found]
    return found

def getModel(id):
    found=-1
    for i in range(len(trainedModels)):
        if(trainedModels[i].id == id ):
            found = i
    if found>-1:
        return trainedModels[found].learn
    else:
        return None

class Model(object):
    def __init__(self,id,path):
        data = TabularDataBunch.load_empty(path)
        learn = tabular_learner(data, layers=[200,100])
        learn.load(id);   
        self.learn = learn
        self.id = id

#loadAllModels(model_dir)
#flask stuff
app = Flask(__name__)

#print(model_dir+'tnK534JMwwfhvUEycn69HPbhqkt2')
#data2 = TabularDataBunch.load_empty(path=Path('../../userdata/models/tnK534JMwwfhvUEycn69HPbhqkt2'))
#learn2 = tabular_learner(data2, layers=[200,100])
#learn2.load('tnK534JMwwfhvUEycn69HPbhqkt2');

@app.route('/')
def hello_world():
    return "Not so good"

@app.route('/retrain')
def retrain():
    userId = request.args.get('userId')
    if userId != None:
        try:
            teachingSet = pd.read_csv(data_dir+userId+teachingSetName,usecols=usecols)
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
            #updateModel(userId)
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
        #geoHash = request.args.get('geoHash')
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        minuteOfDay = request.args.get('minuteOfDay')
        weekday = request.args.get('weekday')
        if detectedActivity != None and latitude != None and longitude != None and minuteOfDay != None and weekday != None and userId != None:
            try:
                #print(Path(model_dir+userId))
                data = TabularDataBunch.load_empty(path=Path(model_dir+userId))               
                learn = tabular_learner(data, layers=[200,100])
                learn.load(userId);
                #prediction,accuracy = predict_journey(getModel(userId),detectedActivity,geoHash,minuteOfDay,weekday)
                #prediction,accuracy = predict_journey(learn,detectedActivity,geoHash,minuteOfDay,weekday)
                prediction,accuracy = predict_journey(learn,detectedActivity,latitude,longitude,minuteOfDay,weekday)
                return json.dumps({"probability": str(accuracy), "fromStation": str(prediction)[0:5], "toStation": str(prediction)[5:10],"error":0})
            except:
                return json.dumps({"error":2}) 
        else:
            return json.dumps({"error":1}) #Not all parameters
    else:
        return json.dumps({"error":1})   #no id
    
@app.route('/delete')
def delete():
    userId = request.args.get('userId')
    if userId != None:
        try:
            #Delete model folder
            shutil.rmtree(model_dir+userId,ignore_errors=True)  #The model
            #Create folder for backup
            foldername = deleted_data_dir+datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') ##Remove then later after study
            os.mkdir(foldername) ##Remove then later after study
            os.chmod(foldername, 0o775)  ##Remove then later after study
            for filename in os.listdir(data_dir):
                if filename.startswith(userId):
                    shutil.copyfile(data_dir+filename, foldername+"/"+filename) ##Remove then later after study
                    os.remove(data_dir+filename)       
            return json.dumps({"error":0})
        except:
            return json.dumps({"error":1})
    else:
        return json.dumps({"error":2})   #no id        

    
app.run()