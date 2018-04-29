# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from packagemanager.models import Package, Apartment, Resident

# Register your models here.

admin.site.register(Package)
admin.site.register(Apartment)
admin.site.register(Resident)