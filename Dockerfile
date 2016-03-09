FROM debian:latest
MAINTAINER lucemia <davidchen@gliacloud.com>
# Install software
RUN apt-get update -y
RUN apt-get install python-lxml libpq-dev python-pip -y
RUN apt-get install python-dev -y
ADD requirements.txt /home/requirements.txt
ADD requirements /home/requirements
RUN pip install -r /home/requirements.txt


ADD ./src /home/src
WORKDIR /home/src

RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput
RUN python manage.py loaddata apis
