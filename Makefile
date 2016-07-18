#
# Makefile
# lizongzhe, 2016-01-30 16:11
#
SHELL = /bin/bash
VPATH = .make

%.success: %
	echo "$*" > .make/$@ && \
	echo "$*" > .make/$*

IMAGE_FILES = $(shell find image/* -type f)
export host = $(shell echo "$(DOCKER_HOST)"|sed 's/[^:]*:\/\///'|sed 's/:[^:]*$$//')
export port = $(shell for port in $$(seq 8000 65000); do echo -ne "\035" | telnet $(host) $$port > /dev/null 2>&1; [ $$? -eq 1 ]  && break; done;echo $$port)
export IMAGE = porkman
wait_time = 3


build: $(IMAGE_FILES)
	curl https://raw.githubusercontent.com/gliacloud/deploy/new/src/build.sh -o build.sh && source build.sh && docker tag $$IMAGE_NAME $(IMAGE) && rm build.sh

MODELS_FILE=$(shell find src/**/models.py)
setup:: $(MODELS_FILE)
	docker run -it --rm -v `pwd`/src:/work -w /work $(IMAGE) python manage.py makemigrations

MIGRATE_FILES=$(shell find src/**/migrations/**.py)
setup:: $(MIGRATE_FILES) 
	docker run -it --rm -v `pwd`/src:/work -w /work $(IMAGE) python manage.py migrate


clear_containers:
	docker-compose -f deploy/docker-compose.yml stop
	docker-compose -f deploy/docker-compose.yml rm

init: build.success setup.success clear_containers

include init

RUN=docker-compose -f deploy/docker-compose.yml run --rm main

shell: 
	$(RUN) shell


PYTHON_FILES = $(shell find src/**/*.py)
test: $(PYTHON_FILES)
	$(RUN) py.test . --cov=.
	$(RUN) flake8 .


coverage: test.success
	( sleep $(wait_time) && open http://localhost:8000 )&
	$(RUN) coverage html
	cd src/htmlcov && python -m SimpleHTTPServer


runserver: 
	(sleep $(wait_time) && open http://$(host):`docker-compose -f deploy/docker-compose.yml port main 80|sed 's/.*://'`)&
	docker-compose -f deploy/docker-compose.yml up -d main


