# -*- coding: utf-8 -*-
from django.db import models


class Base(models.Model):
    """Base

    基底モデル
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Schedule(Base):
    """Schedule

    スケジュール
    """
    name = models.CharField(max_length=255)
