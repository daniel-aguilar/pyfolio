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


MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # noqa: F405
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
