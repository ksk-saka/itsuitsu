# -*- coding: utf-8 -*-
import logging
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from apps.schedules.forms import ScheduleForm, ScheduleDateFormSet, ScheduleUserForm,\
    ScheduleRegisterFormSet
from apps.schedules.models import Schedule, User
from libs.views import AjaxRequestMixin, FormsetMixin

logger = logging.getLogger('sca')

# TODO: 403,404,500画面のハンドリング


class Top(TemplateView):
    """TopView

    TOPページを表示します。
    """
    template_name = 'schedules/index.html'


class New(FormsetMixin, CreateView):
    """New

    つくるページを表示します。
    """
    model = Schedule
    form_class = ScheduleForm
    formset_class = ScheduleDateFormSet
    template_name = 'schedules/new.html'
    success_url = reverse_lazy('schedules:index')

    def form_valid(self, form, formset):
        self.form_extra_fields = {
            'code': get_random_string(30),
        }
        return super(New, self).form_valid(form, formset)


class Detail(DetailView):
    """Detail

    よていページを表示します。
    """
    model = Schedule
    template_name = "schedules/detail.html"
    context_object_name = 'schedule'

    def get_object(self, queryset=None):
        return get_object_or_404(Schedule, code=self.request.GET.get('code'))

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        schedule = context['schedule']
        attendances = []
        for date in schedule.dates:
            registers = date.attendance_set.all()
            attendances.append(tuple(register.user.id for register in registers))
        context['attendances'] = attendances
        return context


class BaseUsersNew(AjaxRequestMixin, FormsetMixin):
    """BaseUsersNew

    """


class UsersNew(BaseUsersNew, CreateView):
    """UsersNew

    ちょうせいページを表示します。
    """
    model = User
    form_class = ScheduleUserForm
    formset_class = ScheduleRegisterFormSet
    template_name = 'schedules/users_new.html'
    success_url = reverse_lazy('schedules:index')

    def __schedule(self):
        return get_object_or_404(Schedule, id=self.kwargs['id'])

    def form_valid(self, form, formset):
        self.form_extra_fields = {
            'schedule': self.__schedule(),
        }
        return super(UsersNew, self).form_valid(form, formset)

    def get_context_data(self, **kwargs):
        context = super(UsersNew, self).get_context_data(**kwargs)
        schedule = self.__schedule()
        context['schedule'] = schedule  # 他の人のも見れるかも
        for form in context['formset']:
            form.fields['date'].queryset = schedule.dates
        return context
