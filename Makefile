#
# Makefile
# lizongzhe, 2016-01-30 16:11
#
SHELL = /bin/bash

origin = $(shell git config --get remote.origin.url| sed "s/[^a-z0-9A-Z_]/_/g")

ifndef TRAVIS_BRANCH
TRAVIS_BRANCH = $(shell git rev-parse --abbrev-ref HEAD)
endif

branch = $(shell echo $(TRAVIS_BRANCH)| sed "s/[^a-z0-9A-Z_]/_/g")

image_name = $(origin)_$(branch)

swarm_command = cd swarm-master && source activite && cd .. &&


test:
    $(swarm_command) \
    docker info

clean_project:
    rm -f $$(find **/*.pyc)


build: clean_project
    $(swarm_command) \
    docker build -t $(image_name) .

docker-compose.yml:
    python -c "print open('compose.template').read().format(name='$(image_name)')" > docker-compose.yml

deploy: build docker-compose.yml
    $(swarm_command) \
    docker-compose stop && docker-compose rm -f && docker-compose scale $(image_name).server=1

