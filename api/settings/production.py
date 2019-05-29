from .base import *
import os

print("production ---------")

ALLOWED_HOSTS = ['0.0.0.0', '18.224.94.174', '3.18.105.6','18.216.255.48']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', True)

SECRET_KEY = env('DJANGO_SECRET_KEY', default='up8ol8l&)5mrqt$8+f3oud6%t%8%=n!wx_+5fh1t0&0l0(jx++')

#celery
# CELERY_BROKER_URL = 'amqp://localhost'
CELERY_BROKER_URL = 'amqp://guest:guest@rabbit:5672/%2F'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    },
    'original': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(ROOT_DIR.path('db.sqlite3')),
    }
}