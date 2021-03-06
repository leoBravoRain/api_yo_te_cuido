# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-30 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dangers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=30)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=30)),
                ('comment', models.CharField(max_length=2000)),
                ('state', models.BooleanField(default=True)),
            ],
        ),
    ]
