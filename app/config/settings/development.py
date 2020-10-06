from .base import *

DEBUG = True
SECURE_SSL_REDIRECT = False
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += ('rest_framework.renderers.BrowsableAPIRenderer',)