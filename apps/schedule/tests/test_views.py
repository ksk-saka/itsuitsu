# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase
from apps.schedule.models import Schedule


class ScheduleViewsTests(TestCase):
    """ScheduleViewsTests

    viewsをテストします。
    """
    fixtures = ['apps/schedule/tests/initial_data.json']

    def test_schedule_create_view(self):
        """test_schedule_create_view

        ScheduleCreateクラスをテストします。
        """
        url = reverse('schedule:add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule/add.html')

        count = Schedule.objects.count()
        response = self.client.post(url, {
            'name': 'TEST NAME',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Schedule.objects.count(), count + 1)

    def test_schedule_update_view(self):
        """test_schedule_update_view

        ScheduleUpdateクラスをテストします。
        """
        schedule = Schedule.objects.all()[0]

        url = reverse('schedule:edit', kwargs={'id': schedule.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule/edit.html')

        response = self.client.post(url, {
            'name': 'TEST NAME',
        })
        self.assertEqual(response.status_code, 302)
        e = Schedule.objects.get(pk=schedule.id)
        self.assertEqual(e.name, 'TEST NAME')
