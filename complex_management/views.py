# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PropertySerializer, FloorplanSerializer, FloorplanRoomSerializer
from .models import Property, Floorplan, FloorplanRoom, RoomItem

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

    def get(self, request, floorplan_id='0', property_id='0'):
        if (floorplan_id == '0') and (property_id == '0'):
            f = Floorplan.objects.all()
            srz = FloorplanSerializer(f, many=True)

            return Response(srz.data)
        else:
            if property_id == '0':
                f = Floorplan.objects.get(id=floorplan_id)
                srz = FloorplanSerializer(f)

                return Response(srz.data)
            else:
                f = Floorplan.objects.filter(property=property_id)
                srz = FloorplanSerializer(f, many=True)

                return Response(srz.data)


    def post(self, request, floorplan_id='0'):
        if (floorplan_id == '0'):
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
            fs = Floorplan.objects.all()
            srz = FloorplanSerializer(fs, many=True)

            return Response(srz.data)
        else:
            room_data = request.data
            data = add_room_to_floorplan(room_data, floorplan_id)
            return Response(data)

class PropertyView(APIView):

    def get(self, request, property_id='0'):
        if (property_id == '0'):
            p = Property.objects.all()
            srz = PropertySerializer(p, many=True)

            return Response(srz.data)
        else:
            p = Property.objects.get(id=property_id)
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

class RoomItemList(APIView):

    def get(self, request, room_id='0'):
        if (room_id == '0'):
            r = FloorplanRoom.objects.all()
            srz = FloorplanRoomSerializer(r, many=True)

            return Response(srz.data)
        else:
            p = FloorplanRoom.objects.get(id=room_id)
            srz = FloorplanRoomSerializer(p)

            return Response(srz.data)

    def post(self, request, room_id='0'):
        rid = request.data

        r = FloorplanRoom.objects.get(id=room_id)

        ri = RoomItem.objects.create(
            name = rid['name']
        )
        ri.save()
        r.room_items.add(ri)
        r.save()

        # srz = FloorplanRoomSerializer(r)

        f = Floorplan.objects.get(id=r.floorplan.id)
        srz = FloorplanSerializer(f)

        return Response(srz.data)