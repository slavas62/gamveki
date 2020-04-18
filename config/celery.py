from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery()

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

app.conf.beat_schedule = {
    # 00:00 4:00 8:00 12:00 16:00 20:00 24:00
    'update-modis': {
        'task': 'fires_app.tasks.modis_update_task',
        'schedule': crontab(minute=0, hour='0,2,4,6,8,10,12,14,16,18,20,22'),
    },
    'update-viirs': {
        'task': 'fires_app.tasks.viirs_update_task',
        'schedule': crontab(minute=0, hour='1,3,5,7,9,11,13,15,17,19,21,23'),
    },
}
app.conf.timezone = 'Europe/Moscow'