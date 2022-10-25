"""
Django settings for team_work project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import json
import os
import urllib
from pathlib import Path

from dotenv import dotenv_values
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$$ns#!$a%##&^5q)jhimi(0os0%dm8vy=leq@f#&*o_)5m86@t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    'django_filters',
    'smart_selects',
    'users',
    'articles'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'team_work.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'articles.context_processors.notification_context.checking_status_notification'
            ],
        },
    },
]

WSGI_APPLICATION = 'team_work.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv("SQL_ENGINE"),
        "NAME": os.getenv("SQL_DB_NAME"),
        "USER": os.getenv("SQL_DB_USER"),
        "PASSWORD": os.getenv("SQL_DB_PASSWORD"),
        "HOST": os.getenv("SQL_DB_HOST"),
        "PORT": os.getenv("SQL_DB_PORT"),
        "OPTIONS": json.loads(os.getenv('SQL_OPTIONS')),
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/


LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_ROOT = os.path.join(BASE_DIR, "static-root")

#STATIC_ROOT = "/home/cfedeploy/webapps/cfehome_static_root/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

LOGIN_URL = '/users/authorization'
LOGIN_ERROR_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Media storage
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# Summernote
SUMMERNOTE_THEME = 'bs4'
X_FRAME_OPTIONS = 'SAMEORIGIN'
# Smart selects
JQUERY_URL = True

AUTH_USER_MODEL = 'users.User'

SUMMERNOTE_CONFIG = {
    'iframe': True,
    'summernote': {
        'airMode': False,
        'width': '100%',
        'height': '480',
        'lang': 'ru-RU',
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'italic', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['table', ['table']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['insert', ['link', 'picture', 'emoji']],
            ['view', ['codeview', 'help']],
        ],
    },
    'attachment_require_authentication': True,
    'lazy': True,
    'css': (
        '../../../static/plugins/summernote/smileys/summernote-ext-emoji-ajax.css',
        '../../../static/plugins/bootstrap-icons/bootstrap-icons.css',
    ),
    'css_for_inplace': (
        '../../../static/plugins/summernote/smileys/summernote-ext-emoji-ajax.css',
        '../../../static/plugins/bootstrap-icons/bootstrap-icons.css',
    ),
    'js': (  # This is for SummernoteWidget
        '../../../static/plugins/summernote/smileys/summernote-ext-emoji-ajax.js',
    ),
    'js_for_inplace': (  # Also for SummernoteInplaceWidget
        '../../../static/plugins/summernote/smileys/summernote-ext-emoji-ajax.js',
    ),
}
