# -*- coding: utf-8 -*-
from itsuitsu.settings.base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'itsuitsu',
        'USER': 'itsuitsu',
        'PASSWORD': 'itsuitsu',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
