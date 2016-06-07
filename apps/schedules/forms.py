# -*- coding: utf-8 -*-
from django.forms import ModelForm, ValidationError, TextInput
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from apps.schedules.models import Schedule, Date, User, Attendance


class ScheduleForm(ModelForm):
    """ScheduleForm

    """
    class Meta:
        model = Schedule
        fields = [
            'name',
            'description',
        ]
        labels = {
            'name': 'イベント名',
            'description': '説明（任意）',
        }
        help_texts = {
            'name': '（例）◯◯さん歓迎会',
            'description': '（例）◯◯さんの歓迎会です。〆切は今週末まで。',
        }


class DateForm(ModelForm):
    """DateForm

    """
    class Meta:
        model = Date
        fields = [
            'date',
        ]
        labels = {
            'date': '',
        }


class DateInlineFormSet(BaseInlineFormSet):
    """DateInlineFormSet

    """
    def clean(self):
        dates = [form['date'].value() for form in self.forms if form['date'].value()]
        if not dates:
            raise ValidationError('日付を入力してください。')
        if len(dates) > len(set(dates)):
            raise ValidationError('日付が重複しています。')


ScheduleFormSet = inlineformset_factory(
    Schedule,
    Date,
    form=DateForm,
    formset=DateInlineFormSet,
    extra=3,
    can_delete=False,
)


class ScheduleUserForm(ModelForm):
    """ScheduleUserForm

    スケジュールユーザ登録/更新フォームです。
    """
    class Meta:
        model = User
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
        model = Attendance
        fields = [
            'date',
        ]
        labels = {
            'date': '',
        }


ScheduleRegisterFormSet = inlineformset_factory(
    User,
    Attendance,
    form=ScheduleRegisterForm,
    formset=DateInlineFormSet,
    extra=2,
    can_delete=False,
    min_num=1,
    validate_min=True,
)
