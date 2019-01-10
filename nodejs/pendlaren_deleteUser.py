#!/usr/bin/python
import shutil
import sys, getopt
import tensorflow as tf
import time
import numpy as np
import os
import subprocess
from subprocess import Popen, PIPE
from tensorflow.contrib.cloud.python.ops import bigquery_reader_ops
from google.cloud import bigquery



def main(argv):
    #print("Tensorflow version: "+tf.VERSION+ "Python version: "+sys.version)
    UID = ''
    ROOT_DIR = "pendlaren"
    UPLOAD = True
    RETRAIN_ALL = False
    DELETE = False
    PREDICT = False
    # tf.logging.set_verbosity(tf.logging.INFO)
    PROJECT = "skanependlaren"
    DATASET = "commuting"
    TIME = int(round(time.time() * 1000))
    NUM_PARTITIONS = 1
    try:
      opts, args = getopt.getopt(argv,"hu:",["uid="])
    except getopt.GetoptError:
       print ('pendlaren_deleteUser.py -h(help) --uid/-u <user id>')
       sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('pendlaren_deleteUser.py -h(help) --uid/-u <user id>')
            sys.exit()
        elif opt in ("-u", "--uid"):
         UID = arg

    #print ("Deleting: "+UID)
    export_dir = os.path.join(ROOT_DIR, UID)
    try:
        shutil.rmtree(export_dir)
    except:
        print("No local files found to delete")

    print(UID)
    Process = subprocess.Popen(['./delete_User_Local_Cloud_BQTable.sh ' + UID], shell=True, stdin=PIPE, stderr=PIPE)
    print (Process.communicate())


if __name__ == "__main__":
   main(sys.argv[1:])