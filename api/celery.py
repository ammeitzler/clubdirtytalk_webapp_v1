from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings.local")

app = Celery('api',
             broker='amqp://guest@localhost//',
             backend='amqp://guest@localhost//',
             include=['project.tasks'] #References your tasks. Donc forget to put the whole absolute path.
             )

app.conf.update(
        CELERY_TASK_SERIALIZER = 'json',
        CELERY_RESULT_SERIALIZER = 'json',
        CELERY_ACCEPT_CONTENT=['json'],
        CELERY_TIMEZONE = 'Europe/Oslo',
        CELERY_ENABLE_UTC = True
                )


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()