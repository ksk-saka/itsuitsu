# -*- coding: utf-8 -*-
from django.db import models
from libs.models import Base


class Schedule(Base):
    """Schedule

    スケジュール
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)
