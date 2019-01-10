#!/usr/bin/python
import shutil
import sys, getopt
import tensorflow as tf
import time
import numpy as np
import os
from tensorflow.contrib.cloud.python.ops import bigquery_reader_ops
from google.cloud import bigquery
debugging = True 



def main(argv):
    print("Tensorflow version: "+tf.VERSION+ " Python version: "+sys.version+" BigQuery version: "+bigquery.__version__)
    TABLE = ''
    ROOT_DIR = "pendlaren"
    # tf.logging.set_verbosity(tf.logging.INFO)
    PROJECT = "skanependlaren"
    DATASET = "commuting"
    QUEUE_SIZE = 100
    TIME = int(round(time.time() * 1000))
    NUM_PARTITIONS = 20
    #TIME = int(round(time.time() * 1000)-(1000*60*60*6)) ##6 timmar sen
    useActivity = True
    useLocation = True
    useWeekday = True
    useTime = True
    retrainAll = False
    print("Fan o hans moster")
    try:
      opts, args = getopt.getopt(argv,"hi:t:w:l:a:r:")
    except getopt.GetoptError:
       print ('pendlaren_TF12.py -h(help) -i <id>')
       sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print (
            'pendlaren_TF12.py -h(help) --version <model version> --delete <True/default:False> --predict <True/default:False>')
            sys.exit()
        elif opt in ("-i"):
            TABLE = arg
        elif opt in ("-t"):
            if arg == "false":
                useTime = False
        elif opt in ("-w"):
            if arg == "false":
                useWeekday = False
        elif opt in ("-l"):
            if arg=="false":
                useLocation = False
        elif opt in ("-a"):
            if arg == "false":
                useActivity = False
        elif opt in ("-r"):
            if arg == "true":
                retrainAll = True
        else:
         print("Something is wrong")
    print("table: "+TABLE)
    if useTime:
     print("useTime is true")
    if useWeekday:
     print("useWeekday is true")
    if useLocation:
     print("useLocation is true")
    if useActivity:
     print("useActivity is true")
    if retrainAll:
     print("retrainAll");
    if (TABLE==''):
        print ("Parameter -v is needed if this is iteractive use ./pendlaren_TF12.py -h for help")
        if debugging:
            TABLE = "tnK534JMwwfhvUEycn69HPbhqkt2"  # Training set
            print("Training set: ", TABLE)
        else:
            sys.exit()
    #Remove output folder so everything has to retrain
    export_dir = os.path.join(ROOT_DIR, TABLE)
    print(os.path.abspath(export_dir))
    if retrainAll:
         try:
             shutil.rmtree(export_dir)
             print("Deleting all")
         except:
             print("No dir to remove")

    def query(project, dataset, table):
        sqlQuery = """
               SELECT startStation, endStation FROM """ + dataset + """.""" + table + """ LIMIT 10000
               """
        labelArray = []
        bqclient= bigquery.Client(project=project)
        query_job = bqclient.query(sqlQuery)
        # Print the results.
        for row in query_job.result():
            labelArray = np.append(labelArray, row["startStation"] + row["endStation"])
        uniqueArray = np.unique(labelArray).tolist()
        print(uniqueArray)
        print(np.shape(uniqueArray))
        return uniqueArray

    def input_fn_from_bigquery():
        features = dict(
            detectedActivity=tf.FixedLenFeature([1], tf.int64),
            startStation=tf.FixedLenFeature([1], dtype=tf.string),
            endStation=tf.FixedLenFeature([1], dtype=tf.string),
            longitude=tf.FixedLenFeature([1], dtype=tf.float32),
            latitude=tf.FixedLenFeature([1], tf.float32),
            geoHash=tf.FixedLenFeature([1], tf.int64),
            locationAccuracy=tf.FixedLenFeature([1], dtype=tf.int64),
            time=tf.FixedLenFeature([1], dtype=tf.int64),
            minuteOfDay=tf.FixedLenFeature([1], dtype=tf.int64),
            weekday=tf.FixedLenFeature([1], dtype=tf.int64),
            detectedActivityConfidence=tf.FixedLenFeature([1], dtype=tf.int64),
            uid=tf.FixedLenFeature([1], dtype=tf.string)
        )

        training_data = dict()
        if (useActivity):
            training_data.update(detectedActivity=tf.FixedLenFeature([1], tf.int64, default_value=0))
        if (useLocation):
            training_data.update(geoHash=tf.FixedLenFeature([1], tf.int64))
        if(useTime):
            training_data.update(minuteOfDay = tf.FixedLenFeature([1], tf.int64, default_value=0))
        if(useWeekday):
            training_data.update(weekday = tf.FixedLenFeature([1], tf.int64, default_value=0))

        # detectedActivity=tf.FixedLenFeature([1], tf.int64, default_value=0),
        # geoHash=tf.FixedLenFeature([1], tf.int64),
        # minuteOfDay=tf.FixedLenFeature([1], tf.int64, default_value=0),
        # weekday=tf.FixedLenFeature([1], tf.int64, default_value=0),

        label = dict(
            startStation=tf.FixedLenFeature([1], dtype=tf.string, default_value="80000"),
            endStation=tf.FixedLenFeature([1], dtype=tf.string, default_value="81000")
        )
        # Create a Reader.

        reader = bigquery_reader_ops.BigQueryReader(project_id=PROJECT,
                                                    dataset_id=DATASET,
                                                    table_id=TABLE,
                                                    timestamp_millis=TIME,
                                                    num_partitions=NUM_PARTITIONS,
                                                    features=features)
        queue = tf.train.string_input_producer(reader.partitions())
        row_id, examples_serialized = reader.read_up_to(queue, QUEUE_SIZE)  ##OK then we get a vector
        features = tf.parse_example(examples_serialized, features=training_data)
        labels = tf.parse_example(examples_serialized, features=label)
        start_stop = tf.add(labels["startStation"], labels["endStation"], name="label")  ##construct start stop
        return features, start_stop



    #Get the labels
    my_label_vocabulary = query(PROJECT, DATASET, TABLE)


    #RAW
    # geo = tf.feature_column.numeric_column("geoHash")
    # bound = [1242202139, 1242207471, 1242211563, 1242211811, 1242211935, 1242212183,
    #          1242212927, 1242213051, 1242213299, 1242479279, 1242479403, 1242481883,
    #          1242483247, 1254862663, 1254867995, 1254873327]
    # geoBucket = tf.feature_column.bucketized_column(geo, boundaries=bound)
    # detectedActivity = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_identity(key="detectedActivity",num_buckets=7,default_value=0))
    # minuteOfDay = tf.feature_column.numeric_column("minuteOfDay")
    # weekday = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_identity(key="weekday",num_buckets=7,default_value=0))
    # feature_columns = [geoBucket,detectedActivity,minuteOfDay,weekday]
    # classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
    #                                             hidden_units=[10,10],
    #                                             n_classes=len(my_label_vocabulary),
    #                                             model_dir=export_dir,
    #                                             label_vocabulary=my_label_vocabulary)

    #Below LinearClassifier (Logistic regression) https://www.tensorflow.org/get_started/feature_columns
    detectedActivity = tf.feature_column.categorical_column_with_identity(key="detectedActivity",num_buckets=7,default_value=0)
    geoHash = tf.feature_column.categorical_column_with_hash_bucket("geoHash",100,dtype=tf.int64)
    minuteOfDay = tf.feature_column.numeric_column("minuteOfDay")
    weekDay = tf.feature_column.categorical_column_with_identity(key="weekday",num_buckets=7,default_value=0)

    #feature_columns = [detectedActivity,geoHash,minuteOfDay,weekDay]
    feature_columns = []
    if(useActivity):
        feature_columns.append(detectedActivity)
    if(useLocation):
        feature_columns.append(geoHash)
    if(useTime):
        feature_columns.append(minuteOfDay)
    if(useWeekday):
        feature_columns.append(weekDay)
    classifier = tf.estimator.LinearClassifier(feature_columns=feature_columns,
                                            n_classes=len(my_label_vocabulary),
                                            model_dir=export_dir,
                                            label_vocabulary=my_label_vocabulary)

    try:
         classifier.train(input_fn=input_fn_from_bigquery, max_steps=1000)
    except:
        print("Unexpected error:", sys.exc_info()[0])

    #if (debugging):
    #    #TABLE = "cross_test_1"
    #    TABLE = "tnK534JMwwfhvUEycn69HPbhqkt2"
    #    QUEUE_SIZE = 100
    #    NUM_PARTITIONS = 10
    #    print("Cross evaluation set", TABLE);
     #   score = classifier.evaluate(input_fn=input_fn_from_bigquery,steps=1000)
     #   print(score)

    # if (debugging):
    #     for x in range(0,10):
    #         hepp = classifier.predict(input_fn=input_fn_from_bigquery,predict_keys=keys)
    #         pred = hepp.next()
    #         print (pred["probabilities"])
    #         print (pred["classes"])

    #Delete trained folders if exists, so there will only be one folder for prediction.
    if not debugging:
        dirs = os.listdir(export_dir)
        for i, val in enumerate(dirs):
            if(os.path.isdir(export_dir+'/'+val)):
                shutil.rmtree(export_dir+'/'+val)
                print("Deleted: "+export_dir+'/'+val)

    #TEst tf.estimator.train_and_evaluate()
    #try:
    #feature_spec = tf.feature_column.make_parse_example_spec(feature_columns)
    # feature_spec = {"detectedActivity": tf.VarLenFeature(dtype=tf.int64),
    #                 "geoHash": tf.VarLenFeature(dtype=tf.int64),
    #                 "minuteOfDay": tf.FixedLenFeature(dtype=tf.int64,shape=[1],default_value=0),
    #                 #"minuteOfDay": tf.VarLenFeature(dtype=tf.int64),
    #                 "weekday": tf.VarLenFeature(dtype=tf.int64)}
    # #
    # feature_spec2 = {"detectedActivity": tf.placeholder(dtype=tf.int64, shape=[1]),
    #                 "geoHash": tf.placeholder(dtype=tf.int64, shape=[1]),
    #                 "minuteOfDay": tf.placeholder(dtype=tf.int64, shape=[1]),
    #                 "weekday": tf.placeholder(dtype=tf.int64, shape=[1])}
    def return_fn():
        feature_spec ={}
        if (useActivity):
            feature_spec.update({"detectedActivity": tf.placeholder(dtype=tf.int64, shape=[1])})
        if (useLocation):
            feature_spec.update({ "geoHash": tf.placeholder(dtype=tf.int64, shape=[1])})
        if(useTime):
            feature_spec.update({ "minuteOfDay": tf.placeholder(dtype=tf.int64, shape=[1])})
        if(useWeekday):
            feature_spec.update({"weekday": tf.placeholder(dtype=tf.int64, shape=[1])})
        # feature_spec2 = {"detectedActivity": tf.placeholder(dtype=tf.int64, shape=[1]),
        #                  "geoHash": tf.placeholder(dtype=tf.int64, shape=[1]),
        #                  "minuteOfDay": tf.placeholder(dtype=tf.int64, shape=[1]),
        #                  "weekday": tf.placeholder(dtype=tf.int64, shape=[1])}
        # feature_spec4 = {"detectedActivity": tf.VarLenFeature(dtype=tf.int64),
        #                 "geoHash": tf.VarLenFeature(dtype=tf.int64),
        #                 #"minuteOfDay": tf.FixedLenFeature(dtype=tf.int64, shape=[1], default_value=0),
        #                 "minuteOfDay": tf.VarLenFeature(dtype=tf.int64),
        #                 "weekday": tf.VarLenFeature(dtype=tf.int64)}
        return tf.estimator.export.ServingInputReceiver(features=feature_spec,receiver_tensors=feature_spec);


    #export_input_fn = tf.estimator.export.build_parsing_serving_input_receiver_fn(feature_spec)
    #export_input_fn = tf.estimator.export.ServingInputReceiver(features=feature_spec2,receiver_tensors=feature_spec2)
    try:
        dir = classifier.export_savedmodel(export_dir_base=export_dir, serving_input_receiver_fn=return_fn)
        print("Export path: " + dir)
    except:
      print("Unexpected error:", sys.exc_info()[0])


if __name__ == "__main__":
   main(sys.argv[1:])