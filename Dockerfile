FROM python:3-onbuild
MAINTAINER lucemia <davidchen@gliacloud.com>
# Install software
RUN apt-get update -y
ADD requirements.txt /home/requirements.txt
RUN pip install -r /home/requirements.txt


ADD ./src /home/src

# FIXME the logs folder location is weird
RUN (cd /home/src && python manage.py migrate --noinput)
RUN (cd /home/src && python manage.py collectstatic --noinput)
RUN (cd /home/src && python manage.py loaddata apis)

WORKDIR /home/src
