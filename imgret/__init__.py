from __future__ import absolute_import

# Make sure Celery app is started along with Django
from .celery import app as celery_app