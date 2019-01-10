#!/usr/bin/env bash
MODEL_DIR=$1
#MODEL_DIR=pendlaren/YWenyQ7PfzbdaY9lggNw0cAmvfT2/
#echo "Path to model used for this prediction: ${MODEL_DIR}"
#--json-instances=./${MODEL_DIR}pred.json \
#--text-instances=./${MODEL_DIR}pred.txt
for d in "$MODEL_DIR"*/ ; do
    saved_model=$d
done
#echo ./${MODEL_DIR}pred.json
#echo $saved_model

gcloud ml-engine local predict \
--model-dir=$saved_model \
--json-instances=./${MODEL_DIR}pred.json \
--format=json