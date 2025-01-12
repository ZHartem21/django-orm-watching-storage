import os

import dj_database_url
from dotenv import load_dotenv

load_dotenv('db_settings.env')


DATABASES = {
        'default': dj_database_url.config(default=os.environ['DATABASE_URL'])
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = os.getenv('DEBUG', False)

ROOT_URLCONF = 'project.urls'


ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
