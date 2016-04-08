# -*- coding: utf-8 -*-
from django.forms import ModelForm, ValidationError
from django.forms.models import BaseInlineFormSet, inlineformset_factory
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


class BaseScheduleDateFormSet(BaseInlineFormSet):
    """BaseScheduleDateFormSet

    スケジュール登録/編集フォームセットです。
    """
    def clean(self):
        dates = [form['date'].value() for form in self.forms if form['date'].value()]
        if len(dates) > len(set(dates)):
            raise ValidationError('日にちが重複しています。')


ScheduleDateFormSet = inlineformset_factory(
    Schedule,
    ScheduleDate,
    form=ScheduleDateForm,
    formset=BaseScheduleDateFormSet,
    extra=2,
    can_delete=False,
    min_num=1,
    validate_min=True,
)
