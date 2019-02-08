# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import django

# Create your models here.

danger_states = [('sin_control','sin_control'), ('controlado','controlado'), ('eliminado','eliminado')]

# Location
class Dangers(models.Model):

	# Add photo field
    latitude = models.DecimalField(max_digits=30, decimal_places=15)

    longitude = models.DecimalField(max_digits=30, decimal_places=15)

    comment = models.CharField(max_length = 2000)

    state = models.CharField(max_length = 2000, choices = danger_states)

    date = models.DateTimeField(default=django.utils.timezone.now)

    photo = models.ImageField(upload_to= 'imagenes/dangers')

    # # Metodo para obtener nombre de objeto
    # def __unicode__(self):
    # 	return self.id

# Comment to Danger
class Comment_To_Danger(models.Model):

	danger = models.ForeignKey(Dangers, on_delete=models.CASCADE)
	date = models.DateTimeField(default=django.utils.timezone.now)
	photo = models.ImageField(upload_to= 'imagenes/comments')
	comment = models.CharField(max_length = 2000)
