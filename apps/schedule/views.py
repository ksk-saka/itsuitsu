# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.crypto import get_random_string
from django.views.generic.edit import CreateView, UpdateView
from apps.schedule.forms import ScheduleForm, ScheduleDateFormSet
from apps.schedule.models import Schedule


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
    model = Schedule
    form_class = ScheduleForm
    formset_class = ScheduleDateFormSet
    template_name = 'schedule/add.html'
    success_url = '/schedule/'

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset = self.get_form(self.formset_class)
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset = self.get_form(self.formset_class)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save(commit=False)
        self.object.code = get_random_string(30)
        self.object.save()
        formset.instance = self.object
        formset.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )


class ScheduleUpdate(UpdateView):
    """ScheduleUpdate

    スケジュールを編集します。
    """
    form_class = ScheduleForm
    template_name = 'schedule/edit.html'
    success_url = '/schedule/'

    def get_object(self, queryset=None):
        return get_object_or_404(Schedule, id=self.kwargs['id'])
