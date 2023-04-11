from .production import *  # noqa: F401,F403

SECRET_KEY = 'pythonista'

DEBUG = True

ALLOWED_HOSTS = []


LOGGING['handlers']['file'] = {
    'class': 'logging.FileHandler',
    'filename': 'application.log',
    'formatter': 'default',
}
LOGGING['loggers'] = {  # noqa: F405
    'emr': {
        'handlers': ['console', 'file'],
        'level': 'DEBUG',
    },
}


SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False


DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
