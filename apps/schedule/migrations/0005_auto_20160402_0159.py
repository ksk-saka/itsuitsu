# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20160401_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='description',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]