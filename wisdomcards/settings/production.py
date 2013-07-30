from defaults import *
from os import environ

# Allowed hosts. Add host domain or IP to it. Do not add '*'.
# Example: ['www.example.com']
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': environ.get('DB_ENGINE'),
        'NAME': environ.get('DB_NAME'),
        'HOST': environ.get('DB_HOST'),
        'PORT': environ.get('DB_PORT'),
        'USER': environ.get('DB_USER'),
        'PASSWORD': environ.get('DB_PASSWORD'),
    }
}

# Modify it for any changes on apps, this variable is for Django template loader.
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.app_directories.Loader
INSTALLED_APPS += (
    'wisdom_cards',
    'rest_framework',
    'django.contrib.admin',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    ),
    'PAGINATE_BY': 10,
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECRET_KEY = environ.get('DJANGO_SECRET_KEY')

STATIC_ROOT = 'static'
STATICFILES_DIRS = ()
