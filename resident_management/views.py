# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-

from django.shortcuts import render
from maintenance.models import MaintenanceRequest
from packagemanager.models import Package
from maintenance.serializers import MaintReqReadSerializer
from packagemanager.serializers import PackageReadSerializer
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserReadSerializer, JustUserSerializer
from .models import ResidentProfile, User

# Create your views here.

from rest_framework.response import Response

class ResidentHomeView(APIView):

    def get(self, request, apt_no='0'):
        if (apt_no != '0'):
            maint_requests = MaintenanceRequest.objects.filter(apartment_no=apt_no).exclude(status='complete').order_by('date_submitted')
            packages = Package.objects.filter(apartment_no=apt_no).filter(status='pending').order_by('date_received')
            pserializer = PackageReadSerializer(packages, many=True)
            mserializer = MaintReqReadSerializer(maint_requests, many=True)

            data = {
                'packages': pserializer.data,
                'maintenance': mserializer.data
            }

            return Response(data)

class Username(APIView):
    def get(self, request):
        current_user = request.user.username

        uu = User.objects.get(username=current_user)

        rp = ResidentProfile.objects.get(user=uu.id)
        rs = UserReadSerializer(rp)

        data = {
            'resident': rs.data
        }

        return Response(data)