# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Apartment(models.Model):
    number = models.CharField(max_length=20, primary_key=True)

        # Returns the string representation of the model.
    def __unicode__(self):              # __unicode__ on Python 2
        return str(self.number)

class Resident(models.Model):
    name = models.CharField(max_length=100)
    apartment_number = models.ForeignKey(Apartment, related_name='residents', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

    def __unicode__(self):
        return unicode(self.name)

    def __str__(self):
        return unicode(self.name)



class Package(models.Model):
    date_received = models.DateTimeField(auto_now_add=True)
    recipient = models.ForeignKey(Resident, related_name='packages', on_delete=models.CASCADE)
    apartment_no = models.ForeignKey(Apartment, related_name='packages', on_delete=models.CASCADE)
    package_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='pending')



