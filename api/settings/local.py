from .base import *
import os

print("local ---------")

DEBUG = env.bool('DJANGO_DEBUG', default=True)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='up8ol8l&)5mrqt$8+f3oud6%t%8%=n!wx_+5fh1t0&0l0(jx++')

#celery
CELERY_BROKER_URL = 'amqp://localhost'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'HOST': '127.0.0.1',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'PORT': 5432,
    },
    'original': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(ROOT_DIR.path('db.sqlite3')),
    }
}