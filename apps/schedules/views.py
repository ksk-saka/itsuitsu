# -*- coding: utf-8 -*-
import logging
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.crypto import get_random_string
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from apps.schedules.forms import ScheduleForm, ScheduleDateFormSet, ScheduleUserForm,\
    ScheduleRegisterFormSet
from apps.schedules.models import Schedule, User
from libs.views import AjaxRequestMixin, FormsetMixin

logger = logging.getLogger('sca')

# TODO: 403,404,500画面のハンドリング
# TODO: クラス名を変更する（ex.Create->Add）
# TODO;: URLを変更する（namespaceをいい感じに）


def index(request):
    """ index

    一覧画面です。（仮）
    :param request:
    :return:
    """
    schedules = Schedule.objects.all()
    return render(request, 'schedules/index.html', {
        'schedules': schedules,
    })


class ScheduleList(DetailView):
    """ScheduleList

    スケジュールを表示します。
    """
    model = Schedule
    template_name = "schedules/list.html"
    context_object_name = 'schedule'

    def get_object(self, queryset=None):
        return get_object_or_404(Schedule, code=self.request.GET.get('code'))

    def get_context_data(self, **kwargs):
        context = super(ScheduleList, self).get_context_data(**kwargs)
        schedule = context['schedule']
        attendances = []
        for date in schedule.dates:
            registers = date.attendance_set.all()
            attendances.append(tuple(register.user.id for register in registers))
        context['attendances'] = attendances
        return context


class BaseScheduleUserCreate(AjaxRequestMixin, FormsetMixin):
    """BaseScheduleUserCreate

    ScheduleUserCreateの基底クラスです。
    """


class ScheduleUserCreate(BaseScheduleUserCreate, CreateView):
    """UserCreate

    スケジュールユーザを登録します。
    """
    model = User
    form_class = ScheduleUserForm
    formset_class = ScheduleRegisterFormSet
    template_name = 'user/add.html'
    success_url = '/schedules/'

    def __schedule(self):
        return get_object_or_404(Schedule, id=self.kwargs['id'])

    def form_valid(self, form, formset):
        self.form_extra_fields = {
            'schedule': self.__schedule(),
        }
        return super(ScheduleUserCreate, self).form_valid(form, formset)

    def get_context_data(self, **kwargs):
        context = super(ScheduleUserCreate, self).get_context_data(**kwargs)
        schedule = self.__schedule()
        context['schedule'] = schedule  # 他の人のも見れるかも
        for form in context['formset']:
            form.fields['date'].queryset = schedule.dates
        return context


class ScheduleCreate(FormsetMixin, CreateView):
    """ScheduleCreate

    スケジュールを登録します。
    """
    model = Schedule
    form_class = ScheduleForm
    formset_class = ScheduleDateFormSet
    template_name = 'schedules/add.html'
    success_url = '/schedules/'

    def form_valid(self, form, formset):
        self.form_extra_fields = {
            'code': get_random_string(30),
        }
        return super(ScheduleCreate, self).form_valid(form, formset)
