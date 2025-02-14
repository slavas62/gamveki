# -*- coding: utf-8 -*-

"""
Django settings for config project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys

import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_DIR = os.path.join(os.path.dirname(sys.executable), '..')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '20g6urh^08^fgi%2p-uk+^gp(e%$@80woj^f-t$$=jei@u@bd$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'solo',
    'fires_app',
    'django_celery_beat',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
#'''
# Для доступа к контейнеру БД на одной виртуалке (НЦ ОМЗ)
DATABASES = {
    'default': dj_database_url.config(default='postgres://'),
}

'''
# Доступ к внешней БД устанавливается также в пусковом файле fires.sh, предназначенного для развертывания докер-контейнера "fires" на виртуалке ВМ-2 (ЦОД РКС)
# или
# Для доступа по внутрисетевому адрессу к контейнеру БД на другой виртуалке, находящейся во внутренней сети (ЦОД РКС)
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', # Add 'postgresql_psycopg2', 'postgresql'
        'NAME': 'gamveki',
        'USER': 'postgres',
        'PASSWORD': 'ntnhfrcby_19',
        'HOST': '10.200.129.16', # внутрисетевой IP адрес другой виртуалки '192.168.31.8'
        'PORT': '5432',
    }
}
'''
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = False


# Подключаем брокера
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
if not CELERY_BROKER_URL:
    CELERY_BROKER_URL = 'redis://localhost:6379/1'

# Регистрируем задачи приложения
# CELERY_IMPORTS = [
#     "fires_app.tasks"
# ]

# Определяем очередь для задач
#CELERY_TASK_ROUTES = {
#   'fires_app.tasks.modis_update_task': {'queue': 'fires', },
#   'fires_app.tasks.viirs_update_task': {'queue': 'fires', },
#}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ENV_DIR, 'www', 'static')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'console_errors': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'update': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}

try:
    from config.settings_local import *
except ImportError:
    pass
