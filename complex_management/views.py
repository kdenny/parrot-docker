# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PropertySerializer, FloorplanSerializer
from .models import Property, Floorplan, FloorplanRoom

# Create your views here.

from rest_framework.response import Response

def add_room_to_floorplan(room, floorplan):
    f = Floorplan.objects.get(id=floorplan)
    r = FloorplanRoom.objects.create(
        name = room['name'],
        property = f.property
    )
    r.save()

    f.rooms.add(r)
    r.save()

    fs = FloorplanSerializer(f)

    return fs.data

class FloorplanView(APIView):

    def get(self, request, floorplan='0'):
        if (floorplan == '0'):
            f = Floorplan.objects.all()
            srz = FloorplanSerializer(f, many=True)

            return Response(srz.data)
        else:
            f = Floorplan.objects.get(id=floorplan)
            srz = FloorplanSerializer(f)

            return Response(srz.data)

    def post(self, request, floorplan='0'):
        if (floorplan == '0'):
            fd = request.data
            complex = Property.objects.get(id=fd['complex']['id'])
            f = Floorplan.objects.create(
                name = fd['name'],
                property = complex
            )
            if 'floorplan_image' in fd:
                f.floorplan_image = fd['floorplan_image']
            if 'stock_picture' in fd:
                f.stock_picture = fd['stock_picture']
            f.save()
            srz = FloorplanSerializer(f, many=True)

            return Response(srz.data)
        else:
            room_data = request.data
            data = add_room_to_floorplan(room_data, floorplan)
            return Response(data)

class PropertyView(APIView):

    def get(self, request, property='0'):
        if (property == '0'):
            p = Property.objects.all()
            srz = PropertySerializer(p, many=True)

            return Response(srz.data)
        else:
            p = Property.objects.get(id=property)
            srz = PropertySerializer(p)

            return Response(srz.data)

    def post(self, request):
        pd = request.data
        p = Property.objects.create(
            name = pd['name'],
            address = pd['address'],
            city = pd['city']
        )
        p.save()

        srz = PropertySerializer(p)

        return Response(srz.data)
