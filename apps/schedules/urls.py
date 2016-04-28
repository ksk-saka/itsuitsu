# -*- coding: utf-8 -*-
from django.conf.urls import url
from apps.schedules import views
from apps.schedules.views import ScheduleCreate, ScheduleList, ScheduleUserCreate

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', ScheduleList.as_view(), name='list'),
    url(r'^add/$', ScheduleCreate.as_view(), name='add'),
    url(r'^(?P<id>[0-9]+)/user-add/$', ScheduleUserCreate.as_view(), name="user_add"),
]
