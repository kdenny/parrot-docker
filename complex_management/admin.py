# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from complex_management.models import Property, Floorplan

# Register your models here.

admin.site.register(Property)
admin.site.register(Floorplan)