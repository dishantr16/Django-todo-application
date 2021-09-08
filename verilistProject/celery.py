from __future__ import unicode_literals
from datetime import timezone
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'verilistProject.settings')

app = Celery('verilistProject')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/kolkata')
app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'VerilistApp.tasks.send_mail_func',
        'schedule': crontab(hour=5, minute=45),
        # 'args': (2,)
    }
}

app.autodiscover_tasks()
