#!/bin/bash -x
set -e

REPO=porkguy

docker pull lucemia/$REPO || true
docker build -t $REPO .
docker tag -f $REPO lucemia/$REPO
docker push lucemia/$REPO

# the origin fabric not support python 3
pip install -e git+https://github.com/pashinin/fabric.git#egg=fabric
fab -u davidchen -i google_compute_engine -H builder.gliacloud.com deploy
