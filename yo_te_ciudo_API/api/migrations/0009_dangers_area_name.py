# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-20 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_area_of_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='dangers',
            name='area_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Area_Of_Company'),
        ),
    ]
