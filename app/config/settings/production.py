import sentry_sdk
import dj_database_url as db
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

"""
DEBUG must be False for production settings
"""
DEBUG = False

"""
Enable Sentry Event monitoring for Django
Set the SENTRY_DSN variable inside .env
"""
if env.bool('DJANGO_PRODUCTION_SENTRY'):
    sentry_sdk.init(
        dsn=env("SENTRY_DSN"),
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
        environment="prod"
    )

"""
Load database from environment variable DATABASE_URL
"""
if env.bool('DJANGO_PRODUCTION_POSTGRES'):
    DATABASES = {
        'default': db.config(
            conn_max_age=env.int('POSTGRES_CONN_MAX_AGE', 500)
        )
    }

"""
Enable Logging if
"""
if env.bool('DJANGO_LOGGING'):
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': env.path('DJANGO_LOGGING_FILE'),
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }

"""
Secutiry Settings
"""
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 86400
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')