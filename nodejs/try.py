#!/usr/bin/python
#import sys, getopt
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



#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    #get our data as an array from read_in()
        lines = read_in()
        #print(lines[1])
        data = TabularDataBunch.load_empty('../models/tnK534JMwwfhvUEycn69HPbhqkt2')
        learn = tabular_learner(data, layers=[200,100])
        learn.load('tnK534JMwwfhvUEycn69HPbhqkt2');
        prediction,accuracy = predict_journey(learn,lines[0],lines[1],lines[2],lines[3]) 
        #print(str(prediction)[0:5])
        #print(str(prediction)[5:10])
        #print(str(accuracy))
        # Sum  of all the items in the providen array
        #return the sum to the output stream
        print([str(prediction)[0:5],str(prediction)[5:10],str(accuracy)])
        
def main2():
    #get our data as an array from read_in()
        #lines = read_in()
        #print(lines[1])
        data = TabularDataBunch.load_empty('../models/tnK534JMwwfhvUEycn69HPbhqkt2')
        learn = tabular_learner(data, layers=[200,100])
        learn.load('tnK534JMwwfhvUEycn69HPbhqkt2');
        prediction,accuracy = predict_journey(learn,4,1242481883,1163,6) 
        #print(str(prediction)[0:5])
        #print(str(prediction)[5:10])
        #print(str(accuracy))
        # Sum  of all the items in the providen array
        #return the sum to the output stream
        print([str(prediction)[0:5],str(prediction)[5:10],str(accuracy)])

        
# Start process
if __name__ == '__main__':
    main2()