# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from apps.schedule.models import Schedule, ScheduleDate


class ScheduleForm(ModelForm):
    """ScheduleForm

    スケジュール登録/編集フォームです。
    """
    class Meta:
        model = Schedule
        fields = [
            'name',
            'description',
        ]
        labels = {
            'name': 'スケジュール名',
            'description': '説明',
        }


class ScheduleDateForm(ModelForm):
    """ScheduleDateForm

    スケジュール日付登録/編集フォームです。
    """
    class Meta:
        model = ScheduleDate
        fields = [
            'date',
        ]
        labels = {
            'date': '日にち',
        }

ScheduleDateFormSet = inlineformset_factory(
    Schedule,
    ScheduleDate,
    form=ScheduleDateForm,
    extra=1,
    can_delete=False,
    min_num=1,
    validate_min=True,
)
