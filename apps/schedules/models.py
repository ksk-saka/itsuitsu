# -*- coding: utf-8 -*-
from django.db import models
from django.utils import formats
from django.utils.timezone import localtime
from libs.models import Base


class Schedule(Base):
    """Schedule

    スケジュールを管理します。
    """
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True)
    code = models.CharField(max_length=64)

    def __repr__(self):
        return '[{}]: {}'.format(self.id, self.name)

    def __str__(self):
        return self.name

    @property
    def dates(self):
        return self.date_set.all()

    @property
    def users(self):
        return self.user_set.all()


class Date(Base):
    """Date

    スケジュールの日付を管理します。
    """
    schedule = models.ForeignKey(Schedule)
    date = models.DateTimeField()

    class Meta:
        ordering = ['date']

    def __repr__(self):
        return '[{}]: {}'.format(self.id, self.__str__())

    def __str__(self):
        formatted = formats.date_format(localtime(self.date), 'Y/m/d(D) H:i')
        return formatted


class User(Base):
    """User

    ユーザを管理します。
    """
    schedule = models.ForeignKey(Schedule)
    attendances = models.ManyToManyField(Date, through='Attendance')
    name = models.CharField(max_length=25)
    comment = models.CharField(max_length=50, blank=True)

    def __repr__(self):
        return '[{}]: {}'.format(self.id, self.name)

    def __str__(self):
        return self.name


class Attendance(Base):
    """Attendance

    ユーザの出欠を管理します。
    """
    user = models.ForeignKey(User)
    date = models.ForeignKey(Date)

    def __repr__(self):
        return '[{}]: {}'.format(self.id, self.__str__())

    def __str__(self):
        return '{} - {}'.format(self.user, self.date)
