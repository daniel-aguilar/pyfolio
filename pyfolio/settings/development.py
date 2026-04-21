# flake8: noqa
from .production import *

SECRET_KEY = 'pythonista'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS += [
    'django_extensions',
]


DATABASES['default']['OPTIONS'] = {
    'sslmode': 'disable'
}


MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STORAGES['default'] = {
    'BACKEND': 'django.core.files.storage.FileSystemStorage',
}


SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
