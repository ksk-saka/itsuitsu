# -*- coding: utf-8 -*-
from django.db import models
from libs.models import Base


class Schedule(Base):
    """Schedule

    スケジュールモデルです。
    """
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True)
    code = models.CharField(max_length=64)

    def __repr__(self):
        return '{}: {}'.format(self.id, self.name)


class ScheduleDate(Base):
    """ScheduleDate

    スケジュール日付モデルです。
    """
    schedule = models.ForeignKey(Schedule)
    date = models.DateTimeField(blank=False)

    def __repr__(self):
        return '{}: {}'.format(self.id, self.date)
