# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-08 00:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190208_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_to_danger',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='dangers',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
