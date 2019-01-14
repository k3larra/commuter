#!/usr/bin/python
import sys, getopt
from fastai import *         
from fastai.tabular import *
sys.path.append("../code")
from commuter import *

PATH="../data/"
dep_var = 'journey'
cat_names = ["detectedActivity","weekday"]
cont_names =["geoHash","minuteOfDay"]
procs = [FillMissing, Categorify, Normalize]

teachingSetName="_teach.csv"
debugging = True 
debugdir = "debug/"

def save_debug_info(user,data):
        if debugging:
            file = open(debugdir+user+'.txt', 'a+')
            file.write(data+"\n")
            file.close()       
            
def main(argv):
    #save_debug_info("serverDebug"," Python version: "+sys.version)
    user=''
    detectedActivity = 0
    geoHash = 0
    minuteOfDay = 0
    weekday = 0
    try:
        opts, args = getopt.getopt(argv,"hi:a:g:m:w:")
    except getopt.GetoptError:
        print ('pendlaren_FastAI_predict.py -h(help) -i <id>')
        #sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('Parameter error')
            sys.exit()
        elif opt in ("-i"):
            user = arg
        elif opt in ("-a"):
            detectedActivity = arg
        elif opt in ("-g"):
            geoHash = arg
        elif opt in ("-m"):
            minuteOfDay = arg
        elif opt in ("-w"):
            weekday = arg    
        else:
            save_debug_info("serverDebug","Something is wrong")
    if (user==''):
        save_debug_info("serverDebug","No userID given")
        #sys.exit()
    data = TabularDataBunch.load_empty('../models/'+user)
    learn = tabular_learner(data, layers=[200,100])
    learn.load(user);
    prediction,accuracy = predict_journey(learn,detectedActivity,geoHash,minuteOfDay,weekday)
    print(str(prediction)[0:5])
    print(str(prediction)[5:10])
    print(str(accuracy))
    
if __name__ == "__main__":
    main(sys.argv[1:])