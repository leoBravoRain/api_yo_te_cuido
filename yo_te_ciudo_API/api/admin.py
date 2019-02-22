# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Dangers, Area_Of_Company, Suggestions_From_User

# Register your models here.

admin.site.register(Dangers)
admin.site.register(Area_Of_Company)
admin.site.register(Suggestions_From_User)