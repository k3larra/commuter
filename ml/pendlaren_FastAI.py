#!/usr/bin/python
#import shutil
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
    save_debug_info("serverDebug"," Python version: "+sys.version)
    try:
        opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
        print ('pendlaren_TF12.py -h(help) -i <id>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('Parameter error')
            sys.exit()
        elif opt in ("-i"):
            user = arg
        else:
            save_debug_info("serverDebug","Something is wrong")
    if (user==''):
        save_debug_info("serverDebug","No userID given")
        sys.exit()
    
    teachingSet = pd.read_csv(PATH+user+teachingSetName)
    teachingSet= make_shure_we_got_enough_rows(teachingSet)
    valid_idx = list(np.random.randint(0,len(teachingSet),int(len(teachingSet)*0.1)))
    data = (TabularList.from_df(teachingSet, path='../models/'+user, cat_names=cat_names, cont_names=cont_names, procs=procs)
        .split_by_idx(valid_idx)
        .label_from_df(cols=dep_var)
        .databunch())
    learner=tabular_learner(data, layers=[200,100],metrics=accuracy)
    learner.fit_one_cycle(7)
    learner.save(name=user)
    data.export()                          
if __name__ == "__main__":
   main(sys.argv[1:])