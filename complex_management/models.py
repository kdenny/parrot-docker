# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
# from packagemanager.models import Apartment
from maintenance.models import Room

class Property(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    city = models.CharField(max_length=150)

    def __str__(self):  # __unicode__ for Python 2
        return self.name


class RoomItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  # __unicode__ for Python 2
        return self.name


class FloorplanRoom(models.Model):
    name = models.CharField(max_length=100)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='floorplan_rooms')
    room_items = models.ManyToManyField(RoomItem, related_name='items')

    def __str__(self):  # __unicode__ for Python 2
        return self.property.name + ' - ' + self.name

class Floorplan(models.Model):
    name = models.CharField(max_length=250)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='floorplans')
    rooms = models.ManyToManyField(FloorplanRoom, related_name='floorplans_included_in')
    floorplan_image = models.CharField(max_length=500, blank=True, null=True)
    stock_picture = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.property.name + ' - ' + self.name