# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-31 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dangers',
            name='photo',
            field=models.ImageField(default='ruta/ficticia', upload_to='imagenes/libros'),
            preserve_default=False,
        ),
    ]
