#!/bin/bash -x
set -e

REPO=porkguy

docker login --username=$DOCKER_USER --password=$DOCKER_PASS --email=$DOCKER_EMAIL
docker pull lucemia/$REPO || true
docker build -t $REPO .
docker tag -f $REPO lucemia/$REPO
docker push lucemia/$REPO

pip install fabric
fab -u davidchen -i google_compute_engine -H builder.gliacloud.com deploy
