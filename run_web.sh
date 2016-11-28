#!/bin/sh
# prepare init migration
su -m foo -c "python manage.py makemigrations images"
# migrate db, so we have the latest db schema
su -m foo -c "python manage.py migrate"
# start development server on public ip interface, on port 8000
su -m foo -c "python manage.py runserver 0.0.0.0:8000"