# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PropertySerializer, FloorplanSerializer
from .models import Property, Floorplan

# Create your views here.

from rest_framework.response import Response

class FloorplanView(APIView):

    def get(self, request, floorplan='0'):
        if (floorplan == '0'):
            f = Floorplan.objects.all()
            srz = FloorplanSerializer(f, many=True)

            return Response(srz.data)

class PropertyView(APIView):

    def get(self, request, property='0'):
        if (property == '0'):
            p = Property.objects.all()
            srz = PropertySerializer(p, many=True)

            return Response(srz.data)