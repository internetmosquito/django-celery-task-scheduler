# django-celery-task-scheduler
An example project on how to use Django + Celery + Redis to deal with periodic tasks

Basically the project has a periodic task that runs every five minutes (images/tasks.py) that will process 
a specified file containing images urls and save them in database and in the folder specied. If no images url
file is specified or destination folder, then the ones used in tasks/settings.py are used.

The task is scheduled through Celery and will run every 5 minutes. Images that are depicted as new (via the 
image_url field itsef) will be saved in db (no binary data) and also in the path specified, otherwise, if 
image is found in filesystem it is the discarded.

Django home page can be visited to check what images have been saved, we use a ListView there to show the 
images so it can be easily checked what new contents are added.

So summarising:

* Celery is used as the periodic task scheduler. 
* Redis is used to communicate celery workers with beat and Django
* SQLite is the db used to store image data
* Results of periodic taks is shown in the Django main page
* Supervisor is used to run the Celery worker and beat 

While everything can be run locally, it is recommended to use Docker to run the application

## Requisites

* Python +3.4
* Django 1.8.2
* Redis 3.2.5
* Celery 3.1.18
* Supervisor 3.0
* Docker 1.12.3
* Docker-compose 1.6.2

## Setup

You can either choose to install this locally or simply use Docker to set up things for you

### Locally

Assuming a Linux (Ubuntu 16.04 version), follow this:

First install Redis

```
sudo apt-get update
sudo apt-get install build-essential tcl
```

Get the specified version of Redis and install it

```
curl -O http://download.redis.io/releases/redis-3.2.5.tar.gz
```

Unzip and install

```
tar xzvf redis-3.2.5.tar.gz
```

Compile and install

```
cd redis-3.2.5
make
make test
sudo make install
```

Start and test it

```
sudo systemctl start redis
```

```
sudo systemctl start redis
```

Create a virtual environment (not mandatory)

Install requirements.txt

```
pip install -r requirements.txt
```

Install Supervisor

```
sudo apt-get install supervisor
sudos service supervisor start
```

Copy config files for local to supervisor config directory

```
cp supervisor/celery_images_beat.conf /etc/supervisor/conf.d/
cp supervisor/celery_images_worker.conf /etc/supervisor/conf.d/
```

Update supervisor with new jobs

```
sudo service supervisor reread
sudo service supervisor update
```

### Docker

Assuming you have already installed docker and docker-compose, its pretty simple

Build the containers

```
docker-compose build
```


## Running

Again, this depends on whether you want to do this locally or with Docker.

### Locally

You will first have to overwrite settings.py file with local_settings.py one, I don't know why this happens 
but for some reason can do this in the build process. Overwrite the CELERY STUFFF section at bottom of file 
in imgret/settings.py with the following contents, basically specifies that our redis server is running at 
localhost:

```
# CELERY STUFF
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Madrid'
```

You will need to change the supervisor config file to point to the paths in you local filesystem, thus change

* supervisor/celery_images_beat.conf
* supervisor/celery_images_worker.conf

Once you've changes the paths, move them to supervisor conf directory

```
cp supervisor/celery_images_beat.conf /etc/supervisor/conf.d/
cp supervisor/celery_images_worker.conf /etc/supervisor/conf.d/
```


Make sure db is initialized properly

```
python manage.py makemigrations
python manage.py makemigrations images
python manage.py migrate
```

Start Django server

```
python manage.py runserver
```

Make sure redis is started along with supervisor jobs

```
sudo supervisorctl status
```

You can now go to http://localhost:8000/, you should see something similar to this after a few minutes

![ImageFetcher](https://dl.dropboxusercontent.com/u/16504598/Selection_155.png)


### Docker

Things are simpler, simply make sure your containers are running

```
docker-componse up -d
```

You need to ssh to machine running supervisor to run manually supervisor again, I don't know why this happens 
yet, but seems like there is no other option

```
docker exec -i -t djangocelerytaskscheduler_web_1 bash
```

And then run 

```
service supervisor start
```

You should be able to go now to http://127.0.0.1:8000 and see the same results as before

## LIVE DEMO

A DigitalOcean droplet can be found [here](http://95.85.57.55:8000/)


## Things to improve

* Fix several issues with Docker
* Add proper dev / production settings scheme
* Use Fabric to deploy automatically
* Add CircleCI for Continous Integration
* Use Gunicorn instead of Django embedded server
* Fix Docker so app folder is writable by foo user, otherwise Django does not start correctly
* More tests

Feel free to contact me for questions, toughts, etc...
