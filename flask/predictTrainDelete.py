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


dep_var = 'journey'
cat_names = ["detectedActivity","weekday"]
cont_names =["geoHash","minuteOfDay"]
procs = [FillMissing, Categorify, Normalize]
teachingSetName="_teach.csv"
trainedModels = []

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

loadAllModels(model_dir)
#flask stuff
app = Flask(__name__)
data2 = TabularDataBunch.load_empty(model_dir+'ehaBtfOPDNZjzy1MEvjQmGo4Zv12')
learn2 = tabular_learner(data2, layers=[200,100])
learn2.load('ehaBtfOPDNZjzy1MEvjQmGo4Zv12');

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
            updateModel(userId)
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
                #data = TabularDataBunch.load_empty(model_dir+userId)
                #learn = tabular_learner(data, layers=[200,100])
                #learn.load(userId);
                prediction,accuracy = predict_journey(getModel(userId),detectedActivity,geoHash,minuteOfDay,weekday)
                #prediction,accuracy = predict_journey(learn,detectedActivity,geoHash,minuteOfDay,weekday)
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
            removeModel(userId)        
            return json.dumps({"error":0})
        except:
            return json.dumps({"error":1})
    else:
        return json.dumps({"error":2})   #no id        

    
