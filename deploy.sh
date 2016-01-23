#!/bin/bash -x
set -e

REPO=porkguy

docker login --username=$DOCKER_USER --password=$DOCKER_PASS --email=$DOCKER_EMAIL
docker pull lucemia/$REPO || true
docker build -t $REPO .
docker tag -f $REPO lucemia/$REPO
docker push lucemia/$REPO

# the origin fabric not support python 3
pip install -e git+https://github.com/pashinin/fabric.git
fab -u davidchen -i google_compute_engine -H builder.gliacloud.com deploy
