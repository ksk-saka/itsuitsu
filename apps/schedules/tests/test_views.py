# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase
from apps.schedules.models import Schedule


class ScheduleViewsTests(TestCase):
    """ScheduleViewsTests

    viewsをテストします。
    """
    fixtures = ['apps/schedules/tests/initial_data.json']

    def test_schedule_create_view(self):
        """test_schedule_create_view

        ScheduleCreateクラスをテストします。
        """
        url = reverse('schedules:add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedules/add.html')

        count = Schedule.objects.count()
        response = self.client.post(url, {
            'name': 'TEST NAME',
            'scheduledate_set-0-date': '2016-01-01',
            'scheduledate_set-TOTAL_FORMS': 3,
            'scheduledate_set-INITIAL_FORMS': 0,
            'scheduledate_set-MIN_NUM_FORMS': 1,
            'scheduledate_set-MAX_NUM_FORMS': 1000,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Schedule.objects.count(), count + 1)

    def test_schedule_update_view(self):
        """test_schedule_update_view

        ScheduleUpdateクラスをテストします。
        """
        schedule = Schedule.objects.all()[0]

        url = reverse('schedules:edit', kwargs={'id': schedule.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedules/edit.html')

        response = self.client.post(url, {
            'name': 'TEST NAME',
        })
        self.assertEqual(response.status_code, 302)
        e = Schedule.objects.get(pk=schedule.id)
        self.assertEqual(e.name, 'TEST NAME')
