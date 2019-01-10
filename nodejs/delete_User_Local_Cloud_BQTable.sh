#!/usr/bin/env bash
UIDE=$1
gcloud config set project skanependlaren
#Delete Table
bq rm -f -t commuting.$UIDE