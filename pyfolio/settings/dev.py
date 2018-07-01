from .production import *

SECRET_KEY = 'pythonista'

DEBUG = True

ALLOWED_HOSTS = []

SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
