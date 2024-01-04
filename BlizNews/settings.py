"""
Django settings for BlizNews project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
# from __future__ import absolute_import, unicode_literals
import os
from pathlib import Path
# import djcelery

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%jc@j(4=!asbspsc!6h=64x)iq)#cnnp5lr_v$0!rxh344yp(o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "0.0.0.0",
    "127.0.0.1",
    '31.129.103.150'
    'bliznews.ru'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'News_app',

]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BlizNews.urls'

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            # django-jinja defaults
            "match_extension": ".jinja2",
            "match_regex": None,
            "app_dirname": "templates",
            # "environment": "config.utils.environment",
            "constants": {},
            "globals": {},
            "context_processors": [

            ],
        },
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'BlizNews.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# local

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'BlizNewsDB',
#         'USER': 'BlizNewsUser',
#         'PASSWORD': '1',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Docker-version Win

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'BlizNewsDB',
        'USER': 'BlizNewsUser',
        'PASSWORD': '1',
        'HOST': 'bliznews-PostgresDB-1',
        'PORT': '5432',
    }
}

# Docker-version VPS

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'bliznewsdb',
#         'USER': 'bliznewsuser',
#         'PASSWORD': '1',
#         'HOST': 'PostgresDB',
#         'PORT': '5432',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('ru', 'Русский'),
    ('en', 'English'),
]

# LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'), ]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'home/app/web/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]
#
MEDIA_URL = 'media/'
# MEDIA_ROOT = BASE_DIR / 'uploads'

STATIC_ROOT = '/home/app/web/static/'
MEDIA_ROOT = '/home/app/web/media/'

# STATIC_URL = "/static/"
# # По какому пути можно будет найти файлы
# STATIC_ROOT = BASE_DIR / "static"
#
# # Аналогично static файлам
# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Celery settings

CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"

# # CELERY_BROKER_URL = 'amqp://localhost:5672'
#
# CELERY_BROKER_URL = 'redis://redis:6379/0'
# CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

# CELERY_BROKER_URL = 'amqp://localhost:5672'

CELERY_BROKER_URL = 'redis://bliznews-redis-1:6379/0'
CELERY_RESULT_BACKEND = 'redis://bliznews-redis-1:6379/0'
