# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Schedule


class ScheduleForm(ModelForm):
    """ScheduleForm

    スケジュール登録/編集フォームです。
    """
    class Meta:
        model = Schedule
        fields = ['name']
        labels = {
            'name': '名前'
        }
