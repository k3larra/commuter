#!/usr/bin/python
#import shutil
import sys, getopt
#import time
#import numpy as np
#import os
#Setup
from fastai import *          # Quick accesss to most common functionality
from fastai.tabular import *  # Quick accesss to tabular functionality     # Access to example data provided with fastai
#from fastai.vision import *
sys.path.append("../code") # go to parent dir
from commuter import *
#print("Python version: "+sys.version)
PATH="../data/"
dep_var = 'journey'
cat_names = ["detectedActivity","weekday"]
cont_names =["geoHash","minuteOfDay"]
procs = [FillMissing, Categorify, Normalize]

debugging = True 

def save_debug_info(user,data):
        if debugging:
            file = open("debug/"+user+'.txt', 'a+')
            file.write(data+"\n")
            file.close()       
            
def main(argv):
    save_debug_info("serverDebug"," Python version: "+sys.version)
    try:
      opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
       print ('pendlaren_TF12.py -h(help) -i <id>')
       sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print (
            'pendlaren_TF12.py -h(help) --version <model version> --delete <True/default:False> --predict <True/default:False>')
            sys.exit()
        elif opt in ("-i"):
            user = arg
        else:
            save_debug_info("serverDebug","Something is wrong")
    if (user==''):
        save_debug_info("serverDebug","No userID given")
        sys.exit()
    save_debug_info("serverDebug","userID:"+user)
    save_debug_info(user,"Requested retraining")
    print("YEs")
    #teachingSetName="_teaching_set_minimal.csv"
    teachingSetName="_teaching_set.csv"
    #teachingSetName="_teaching_set_aug.csv"
    #teachingSetName="_train_valid.csv"
    teachingSet = pd.read_csv(PATH+user+teachingSetName)
    teachingSet= make_shure_we_got_enough_rows(teachingSet)
    valid_idx = list(np.random.randint(0,len(teachingSet),int(len(teachingSet)*0.1)))
    data = (TabularList.from_df(teachingSet, path=user, cat_names=cat_names, cont_names=cont_names, procs=procs)
        .split_by_idx(valid_idx)
        .label_from_df(cols=dep_var)
        .databunch())
    learner=tabular_learner(data, layers=[200,100], metrics=accuracy,callback_fns=ShowGraph)
    learner.fit_one_cycle(7)

         
                
                             
if __name__ == "__main__":
   main(sys.argv[1:])