# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import django

# Create your models here.
danger_states = [('sin_control','sin_control'), ('controlado','controlado'), ('eliminado','eliminado')]

# Area of company
# This must to be a company like a foreign key
class Area_Of_Company(models.Model):

    # This must to be a company like a foreign key

    # Area name
    area_name = models.CharField(max_length = 100)

    # Display object with its area name
    def __str__(self):
        return self.area_name

# Location
class Dangers(models.Model):

    # Add photo field
    latitude = models.DecimalField(max_digits=30, decimal_places=15)

    longitude = models.DecimalField(max_digits=30, decimal_places=15)

    comment = models.CharField(max_length = 2000)

    state = models.CharField(max_length = 2000, choices = danger_states, )

    date = models.DateTimeField(default=django.utils.timezone.now)

    photo = models.ImageField(upload_to= 'imagenes/dangers')

    floor_number = models.CharField(max_length = 2000)

    # Id for local managment system of risk of each company (each company has its own MS)
    # It can be an empty value
    id_management_system = models.CharField(max_length = 2000, blank = True)

    # area of company
    area_name = models.ForeignKey(Area_Of_Company, null = True)

    # # Metodo para obtener nombre de objeto
    # def __unicode__(self):
    #   return self.id

# Comment to Danger
class Comment_To_Danger(models.Model):

    danger = models.ForeignKey(Dangers, on_delete=models.CASCADE)
    date = models.DateTimeField(default=django.utils.timezone.now)
    photo = models.ImageField(upload_to= 'imagenes/comments')
    comment = models.CharField(max_length = 2000)

