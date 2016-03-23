from .common import *

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
SECRET_KEY = env("DJANGO_SECRET_KEY", default='t7%-87xofeg6d28q8x6!cf#)nr*e6&occwb-ltur3&*(amisc4')


# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')
