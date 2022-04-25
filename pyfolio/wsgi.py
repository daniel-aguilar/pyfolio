"""
WSGI config for pyfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyfolio.settings.production')

application = get_wsgi_application()
