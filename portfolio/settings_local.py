from .settings import *

# Local development overrides
DEBUG = True
ALLOWED_HOSTS = ['*']

# Remove whitenoise middleware (not needed locally)
MIDDLEWARE = [m for m in MIDDLEWARE if 'whitenoise' not in m]
