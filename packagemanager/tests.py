# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from packagemanager.models import Package, Apartment, Resident

class PackageTestCase(TestCase):
    def setUp(self):
        apt = Apartment.objects.create(number='310')
        bill1 = Resident.objects.create(name='Bill Bixby', apartment_number=apt)
        box = Package.objects.create(recipient=bill1, apartment_no=bill1.apartment_number, package_type='small', status='pending')

    def test_packages(self):
        g = Package.objects.all()
        print(g)
        a = Apartment.objects.all()
        print(a[0].residents)
        print(Apartment._meta.get_fields())
