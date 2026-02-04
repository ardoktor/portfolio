from .settings import *

# Local development overrides
DEBUG = True
ALLOWED_HOSTS = ['*']

# Remove whitenoise middleware (not needed locally)
MIDDLEWARE = [m for m in MIDDLEWARE if 'whitenoise' not in m.lower()]

# Use simple static storage locally
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Disable security redirects locally
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
