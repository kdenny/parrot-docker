# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse

from packagemanager.models import Apartment, Resident, Package
from packagemanager.serializers import PackageReadSerializer, PackageCreateSerializer, ResidentSerializer, ApartmentSerializer
import os
from pprint import pprint
from django.http import JsonResponse

from twilio.rest import TwilioRestClient

account = "AC03baeadb37d7438a8d8b57e819b98b83"
token = "b56cce2fd0222dfea54d36e627a4798b"
client = TwilioRestClient(account, token)

class PackagesListView(APIView):

    def get(self, request, apartment_key='0'):
        if (apartment_key == '0'):
            packages = Package.objects.filter(status='pending').order_by('date_received')
        else:
            packages = Package.objects.filter(apartment_no=apartment_key).filter(status='pending').order_by('date_received')
            print(packages)

        serializer = PackageReadSerializer(packages, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)

        serializer = PackageCreateSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            print("serialized!")
            for package in request.data:

                resident_obj = Resident.objects.get(id=package['recipient'])
                resident_phone = '+1' + str(resident_obj.phone_number).strip()
                text_string = "Hi {0}! You have a package waiting for you at the front desk.".format(resident_obj.name)

                message = client.messages.create(to=resident_phone, from_="+12157098547",
                                                 body=text_string)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            #################### END POST RELATED METHODS ####################

class PackagePickup(APIView):


    def post(self, request):
        print(request.data)
        picked_up = request.data
        for pack in picked_up:
            pack_obj = Package.objects.get(id=pack['id'])
            pack_obj.status = 'picked_up'
            pack_obj.save()
        packages = Package.objects.filter(status='pending').order_by('date_received')

        return Response(packages)

class CheckBarcode(APIView):


    def post(self, request):
        print(request.data)
        package = drogher.barcode('1Z999AA10123456784')
        print(package.is_valid)
        print(package.shipper)
        print(package.tracking_number)
        a = {
            'shipper': package.shipper,
            'tracking': package.tracking_number
        }

        return Response(a)

class PackagesByFloor(APIView):
    def get(self, request):
        packages = {}
        for floor in xrange(1,5):
            name = "floor_" + str(floor)
            floor_packs = Package.objects.filter(apartment_no__number__startswith=str(floor)).order_by('apartment_no__number')
            floor_packs_ser = PackageReadSerializer(floor_packs, many=True)
            packages[name] = floor_packs_ser.data

        return Response(packages)


class ApartmentsListView(APIView):

    def get(self, request):
        apartments = Apartment.objects.all()
        for floor in xrange(1,4):
            print(floor)
        third_floor = Package.objects.filter(apartment_no__number__startswith='3')
        third_ser = PackageReadSerializer(third_floor, many=True)
        packages = {
            'first_floor' : [],
            'second_floor' : [],
            'third_floor' : third_ser.data,
            'fourth_floor' : []
        }
        pprint(packages)
        for p in third_floor:
            print(p)

        serializer = ApartmentSerializer(apartments, many=True)
        return Response(serializer.data)

class ApartmentResidentsView(APIView):

    def get(self, request, apartment_key='0'):
        if (apartment_key != '0'):
            apartment = Apartment.objects.get(number=apartment_key)
            residents = apartment.residents
        else:
            return None

        serializer = ResidentSerializer(residents, many=True)
        return Response(serializer.data)
