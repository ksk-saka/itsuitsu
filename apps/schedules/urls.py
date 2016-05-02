# -*- coding: utf-8 -*-
from django.conf.urls import url
from apps.schedules.views import Top, New, Detail, UsersNew

urlpatterns = [
    url(r'^$', Top.as_view(), name='index'),
    url(r'^new/$', New.as_view(), name='new'),
    url(r'^(?P<id>[0-9]+)/$', Detail.as_view(), name='detail'),
    url(r'^(?P<id>[0-9]+)/users/new/$', UsersNew.as_view(), name='users_new'),
]
