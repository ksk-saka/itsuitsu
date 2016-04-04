# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20160317_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='schedule',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='scheduledate',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Schedule'),
        ),
    ]