# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-11 00:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0012_auto_20170710_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='begin_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]