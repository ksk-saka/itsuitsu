# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.http import urlencode


def build_url(*args, **kwargs):
    get = kwargs.pop('get', {})
    url = reverse(*args, **kwargs)
    if get:
        url += '?' + urlencode(get)
    return url