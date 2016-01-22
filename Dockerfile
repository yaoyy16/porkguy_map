FROM python:3-onbuild
MAINTAINER lucemia <davidchen@gliacloud.com>
# Install software
RUN apt-get update -y
ADD requirements.txt /home/requirements.txt
RUN pip install -r /home/requirements.txt


ADD ./ /home/src

# FIXME the logs folder location is weird
RUN (cd /home/src && python manage.py migrate --noinput)
RUN (cd /home/src && python manage.py collectstatic --noinput)
RUN (cd /home/src && python manage.py import_city)
RUN (cd /home/src && python manage.py import_fundget)
RUN (cd /home/src && python manage.py import_surplus)
RUN (cd /home/src && python manage.py import_lotterystore)
RUN (cd /home/src && python manage.py import_org)
RUN (cd /home/src && python manage.py add_prize_time)
RUN (cd /home/src && python manage.py add_project)
RUN (cd /home/src && python manage.py update_city)
RUN (cd /home/src && python manage.py update_org)
RUN (cd /home/src && python manage.py update_result)
RUN (cd /home/src && python manage.py update_store)
RUN (cd /home/src && python manage.py update_surplus)
RUN (cd /home/src && python manage.py remove_same)

WORKDIR /home/src
