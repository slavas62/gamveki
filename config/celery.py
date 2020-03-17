from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('fires_app')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()

app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

app.conf.beat_schedule = {
    # 00:00 4:00 8:00 12:00 16:00 20:00 24:00
    'update-modis': {
        'task': 'fires_app.tasks.modis_update_task',
        'schedule': crontab(minute=0, hour='0,2,6,10,14,18,22'),
    },
    'update-viirs': {
        'task': 'fires_app.tasks.viirs_update_task',
        'schedule': crontab(minute=0, hour='0,4,8,12,16,20'),
    },
}
app.conf.timezone = 'Europe/Moscow'