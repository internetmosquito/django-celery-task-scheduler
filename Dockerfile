# use base python image with python 2.7
FROM python:3.4

ENV INSTALL_PATH /app

RUN mkdir -p $INSTALL_PATH


WORKDIR $INSTALL_PATH


COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt

COPY . .

# install python dependencies
RUN pip install -r requirements.txt

# create unprivileged user
RUN adduser --disabled-password --gecos '' foo

# Install celery and supervisor
RUN apt-get update && apt-get install -y supervisor
CMD ["/usr/bin/supervisord"]
COPY ./supervisor/celery_images_worker_production.conf /etc/supervisor/conf.d/
COPY ./supervisor/celery_images_beat_production.conf /etc/supervisor/conf.d/
CMD ["touch /app/images_worker.log"]
CMD ["touch /app/images_beat.log"]
CMD ["supervisorctl reread"]
CMD ["supervisorctl update"]

