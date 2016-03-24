# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from .forms import ScheduleForm
from .models import Schedule


def index(request):
    """ index

    一覧画面です。（仮）
    :param request:
    :return:
    """
    schedules = Schedule.objects.all()
    return render(request, 'schedule/index.html', {
        'schedules': schedules,
    })


class ScheduleCreate(CreateView):
    """ScheduleCreate

    スケジュールを登録します。
    """
    form_class = ScheduleForm
    template_name = 'schedule/add.html'
    success_url = '/schedule/'


class ScheduleUpdate(UpdateView):
    """ScheduleUpdate

    スケジュールを編集します。
    """
    form_class = ScheduleForm
    template_name = 'schedule/edit.html'
    success_url = '/schedule/'

    def get_object(self, queryset=None):
        return get_object_or_404(Schedule, id=self.kwargs['id'])
