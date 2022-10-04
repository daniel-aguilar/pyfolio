from .production import *  # noqa: F401,F403

SECRET_KEY = 'pythonista'

DEBUG = True

ALLOWED_HOSTS = []


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'application.log',
            'formatter': 'default',
        }
    },
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        }
    },
    'loggers': {
        'pyfolio': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    },
}


SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
