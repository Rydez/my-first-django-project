# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 20:33
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20180113_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number', regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='validated',
            field=models.BooleanField(default=False),
        ),
    ]
