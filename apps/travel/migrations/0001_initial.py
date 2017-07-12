# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-25 02:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_reg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('begin_date', models.DateTimeField(default=datetime.date.today, verbose_name='Date')),
                ('end_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='login_reg.User')),
                ('other_users', models.ManyToManyField(to='login_reg.User')),
            ],
        ),
    ]
