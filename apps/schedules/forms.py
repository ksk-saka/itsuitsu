# -*- coding: utf-8 -*-
from django.forms import ModelForm, ValidationError, HiddenInput
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from apps.schedules.models import Schedule, ScheduleDate, ScheduleUser, ScheduleRegister


class ScheduleForm(ModelForm):
    """ScheduleForm

    スケジュール登録/更新フォームです。
    """
    class Meta:
        model = Schedule
        fields = [
            'name',
            'description',
        ]
        labels = {
            'name': '名前',
            'description': '説明',
        }


class ScheduleDateForm(ModelForm):
    """ScheduleDateForm

    スケジュール日付登録/更新フォームです。
    """
    class Meta:
        model = ScheduleDate
        fields = [
            'date',
        ]
        labels = {
            'date': '',
        }


class ScheduleInlineFormSet(BaseInlineFormSet):
    """BaseScheduleDateFormSet

    スケジュール登録/更新フォームセットです。
    """
    def clean(self):
        dates = [form['date'].value() for form in self.forms if form['date'].value()]
        if len(dates) > len(set(dates)):
            raise ValidationError('日付が重複しています。')


ScheduleDateFormSet = inlineformset_factory(
    Schedule,
    ScheduleDate,
    form=ScheduleDateForm,
    formset=ScheduleInlineFormSet,
    extra=2,
    can_delete=False,
    min_num=1,
    validate_min=True,
)


class ScheduleUserForm(ModelForm):
    """ScheduleUserForm

    スケジュールユーザ登録/更新フォームです。
    """
    class Meta:
        model = ScheduleUser
        fields = [
            'name',
            'comment',
        ]
        labels = {
            'name': 'ニックネーム',
            'comment': 'コメント',
        }


class ScheduleRegisterForm(ModelForm):
    """ScheduleRegisterForm

    スケジュール登録登録/更新フォームです。
    """
    class Meta:
        model = ScheduleRegister
        fields = [
            'date',
        ]
        labels = {
            'date': '',
        }


ScheduleRegisterFormSet = inlineformset_factory(
    ScheduleUser,
    ScheduleRegister,
    form=ScheduleRegisterForm,
    formset=ScheduleInlineFormSet,
    extra=2,
    can_delete=False,
    min_num=1,
    validate_min=True,
)
