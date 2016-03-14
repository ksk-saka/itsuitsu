# -*- coding: utf-8 -*-
from itsuitsu.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'itsuitsu',
        'USER': 'itsuitsu',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
