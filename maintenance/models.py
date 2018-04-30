# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from packagemanager.models import Resident, Apartment
from django.contrib.auth.models import User

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    account = models.OneToOneField(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name = models.CharField(max_length=150)
    staff = models.ManyToManyField(Staff)

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

class Room(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return str(str(self.name))

    def __str__(self):
        return str(str(self.name))

class MaintenanceItem(models.Model):
    name = models.TextField()
    room = models.ForeignKey(Room, related_name='items', on_delete=models.CASCADE)

    def __unicode__(self):
        return str(str(self.name))

    def __str__(self):
        return str(str(self.name))

class Issue(models.Model):
    name = models.TextField()
    item = models.ForeignKey(MaintenanceItem, related_name='issues', on_delete=models.CASCADE)
    priority = models.CharField(max_length=25, null=True)

    def __unicode__(self):
        return str(str(self.item.name)-str(self.name))

    def __str__(self):
        return str(str(self.item.name)-str(self.name))

class MaintenanceRequest(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    apartment_no = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    date_submitted = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    item = models.ForeignKey(MaintenanceItem, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    description = models.CharField(max_length=250,null=True)
    priority = models.CharField(max_length=25, null=True)
    status = models.CharField(max_length=100, default='pending')

    def __unicode__(self):
        return str(self.resident.name + "-" + self.room.name + "-" + self.item.name + "-" + str(self.date_submitted))

    def __str__(self):
        return str(self.resident.name + "-" + self.room.name + "-" + self.item.name + "-" + str(self.date_submitted))

class MaintenanceUpdate(models.Model):
    comment = models.TextField()
    request = models.ForeignKey(MaintenanceRequest, related_name='updates', on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    update_type = models.CharField(max_length=100)

    def __unicode__(self):
        return str(str(self.request.id) + "-" + self.update_type + "-" + str(self.date))

    def __str__(self):
        return str(str(self.request.id) + "-" + self.update_type + "-" + str(self.date))

class Comment(models.Model):
    submitted_by = models.ForeignKey(Resident, on_delete=models.CASCADE)
    request = models.ForeignKey(MaintenanceRequest, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
