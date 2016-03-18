# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Schedule
from django.core.exceptions import *

def index(request):
    """ index

    一覧画面です。（仮）
    :param request:
    :return:
    """
    schedules = Schedule.objects.all()
    return render(request, 'index.html', {
        'schedules': schedules,
    })


def add(request):
    """

    編集画面です。（仮）
    :param request:
    :return:
    """
    return render(request, 'edit.html')
