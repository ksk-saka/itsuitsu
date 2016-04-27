# -*- coding: utf-8 -*-
from django.db import models
from libs.models import Base


class Schedule(Base):
    """Schedule

    スケジュールデータを管理します。
    """
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True)
    code = models.CharField(max_length=64)

    def __repr__(self):
        return '{}: {}'.format(self.id, self.name)

    def __str__(self):
        return self.name

    @property
    def dates(self):
        return self.scheduledate_set.all()

    @property
    def users(self):
        return self.scheduleuser_set.all()


class ScheduleDate(Base):
    """ScheduleDate

    スケジュールの日付データを管理します。
    """
    schedule = models.ForeignKey(Schedule)
    date = models.DateTimeField()

    class Meta:
        ordering = ['date']

    def __repr__(self):
        return '{}: {}'.format(self.id, self.date)

    def __str__(self):
        return self.date.strftime('%m/%d(%a) %H:%M')


class ScheduleUser(Base):
    """ScheduleUser

    スケジュールのユーザデータを管理します。
    """
    schedule = models.ForeignKey(Schedule)
    name = models.CharField(max_length=25)
    comment = models.CharField(max_length=50, blank=True)

    def __repr__(self):
        return '{}: {}'.format(self.id, self.name)

    def __str__(self):
        return self.name

    @property
    def registers(self):
        return self.scheduleregister_set.all()


class ScheduleRegister(Base):
    """ScheduleRegister

    スケジュールの登録データを管理します。
    """

    date = models.ForeignKey(ScheduleDate)
    user = models.ForeignKey(ScheduleUser)

    def __repr__(self):
        return '{}: {},{},{}'.format(self.id, self.date, self.user, self.result)

    def __str__(self):
        return '{},{}'.format(self.user, self.date)
