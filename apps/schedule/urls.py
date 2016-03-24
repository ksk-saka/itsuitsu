# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from .views import ScheduleCreate, ScheduleUpdate

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', ScheduleCreate.as_view(), name='add'),
    url(r'^(?P<id>[0-9]+)/edit/$', ScheduleUpdate.as_view(), name='edit'),
]
