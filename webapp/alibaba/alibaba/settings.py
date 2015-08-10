#coding=utf-8
"""
Django settings for crawler project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    from local_settings import *
except ImportError:
    print "Don't have local settings"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8w81chmmaumpd=a6wkbzzt5y9_a-+!yf%v754+efejkb13&oo@'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": CACHES_LOCATION,
        'KEY_PREFIX': 'alibaba.',
        'TIMEOUT': 300,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            "SOCKET_TIMEOUT": 5,  # in seconds
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    }
}
AUTH_USER_MODEL='auth.User'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# SECURITY WARNING: don't run with debug turned on in production!

TEMPLATE_DEBUG = DEBUG

MANAGERS = ADMINS

ALLOWED_HOSTS = []


# Application definition

ROOT_URLCONF = 'alibaba.urls'

TEMPLATES_DIRS = (os.path.join(BASE_DIR, "templates").replace('\\', '/'),)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates").replace('\\', '/'),  # insert your TEMPLATE_DIRS here
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.core.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                # insert your TEMPLATE_LOADERS here
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ]
        },
    },
]

WSGI_APPLICATION = 'alibaba.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
        'CHARSET': 'utf8'
    }
}



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh_CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = False

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (
os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
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
    }
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'alibaba',
    }
}

FIRST_DAY_OF_WEEK = 1


from django_redis import get_redis_connection
REDIS = get_redis_connection("default")

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_AGE = 1209600

from django.contrib.messages import constants as message_constants

MESSAGE_LEVEL = message_constants.DEBUG

LOGIN_URL = "/member/login"
LOGIN_REDIRECT_URL = "/member/"
LOGOUT_URL = "/member/logout"

FILE_UPLOAD_TEMP_DIR = "/tmp"
EMAIL_TIMEOUT = 5

DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i'
TIME_FORMAT = 'H:i'

DJANGO_REDIS_IGNORE_EXCEPTIONS = True
AUTHENTICATION_BACKENDS =('django.contrib.auth.backends.ModelBackend',)
INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'search',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.security.SecurityMiddleware',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

SUIT_CONFIG = {
    'ADMIN_NAME': u'搜索',
    'LIST_PER_PAGE': 50
}

