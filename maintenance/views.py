# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from maintenance.models import MaintenanceRequest, Room, MaintenanceItem, Issue, MaintReq
from maintenance.serializers import MaintenanceReadSerializer, MaintenancePostSerializer, MaintenanceUpdateSerializer, CommentSerializer, RoomSerializer, MaintenanceItemSerializer, NewMaintRequestSerializer, MaintReqReadSerializer
from rest_framework.views import APIView
from rest_framework import status
from pprint import pprint
# Create your views here.

from rest_framework.response import Response

class MaintenanceListView(APIView):

    def get(self, request, apartment_key='0'):
        if (apartment_key == '0'):
            maint_requests = MaintReq.objects.exclude(status='complete').order_by('date_submitted')
        else:
            maint_requests = MaintReq.objects.filter(apartment_no=apartment_key).order_by('date_submitted')

        serializer = MaintReqReadSerializer(maint_requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        this_req = request.data

        this_req['resident'] = 1
        this_req['category'] = 1
        this_req['staff'] = [1]

        serializer = MaintenancePostSerializer(data=this_req)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            #################### END POST RELATED METHODS ####################

class MaintenanceDetailView(APIView):

    def get(self, request, maint_id='0'):
        if (maint_id != '0'):
            maint_request = MaintReq.objects.get(id=maint_id)

            serializer = MaintenanceReadSerializer(maint_request)
            return Response(serializer.data)

class MaintenanceUpdateView(APIView):

    def get(self, request, maint_id='0'):
        if (maint_id != '0'):
            maint_request = MaintenanceRequest.objects.get(id=maint_id)

            serializer = MaintenanceReadSerializer(maint_request)
            return Response(serializer.data)

    def post(self, request, maint_id='0'):
        if (maint_id != '0'):
            this_update = request.data
            this_update['request'] = maint_id

            ## Update the status of maintenance request object
            maint_request = MaintenanceRequest.objects.get(id=maint_id)
            maint_request.status = this_update['update_type']
            maint_request.save()

            serializer = MaintenanceUpdateSerializer(data=this_update)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                #################### END POST RELATED METHODS ####################

class MaintenanceCommentView(APIView):

    def get(self, request, maint_id='0'):
        if (maint_id != '0'):
            maint_request = MaintenanceRequest.objects.get(id=maint_id)

            serializer = MaintenanceReadSerializer(maint_request)
            return Response(serializer.data)

    def post(self, request, maint_id='0'):
        if (maint_id != '0'):
            this_update = request.data
            this_update['request'] = maint_id

            serializer = CommentSerializer(data=this_update)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                #################### END POST RELATED METHODS ####################


class StaffMaintenanceView(APIView):

    def get(self, request, staff_id='0'):
        if (staff_id != '0'):
            maint_requests = MaintenanceRequest.objects.filter(staff__id=staff_id)

            serializer = MaintenanceReadSerializer(maint_requests)
            return Response(serializer.data)

class CategoryMaintenanceView(APIView):

    def get(self, request, category_id='0'):
        if (category_id != '0'):
            maint_requests = MaintenanceRequest.objects.filter(category__id=category_id)

            serializer = MaintenanceReadSerializer(maint_requests)
            return Response(serializer.data)

class RoomsListView(APIView):

    def get(self, request):
        rooms = Room.objects.all()

        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

class MaintenanceItemListView(APIView):

    def get(self, request, room_id='0'):
        if (room_id != 0):

            mis = MaintenanceItem.objects.filter(room=room_id)

            serializer = MaintenanceItemSerializer(mis, many=True)
            return Response(serializer.data)

class MaintenanceIssue(APIView):

    def post(self, request):
        new_item = request.data
        rm_check = Room.objects.filter(name=new_item['room'])
        if len(rm_check) == 0:
            rm = Room.objects.create(name=new_item['room'])
            rm.save()
        else:
            rm = rm_check[0]

        mi_check = MaintenanceItem.objects.filter(name=new_item['item'], room=rm)
        if len(mi_check) == 0:
            mi = MaintenanceItem.objects.create(name=new_item['item'], room=rm)
            mi.save()
        else:
            mi = mi_check[0]

        iss_check = Issue.objects.filter(name=new_item['issue'], item=mi)
        if len(iss_check) == 0:
            if 'priority' in new_item:
                iss = Issue.objects.create(name=new_item['issue'], item=mi, priority=new_item['priority'])
            else:
                iss = Issue.objects.create(name=new_item['issue'], item=mi)
            iss.save()
        else:
            iss = iss_check[0]

        data = {
            'message': "Created successfully"
        }



        return Response(data, status=status.HTTP_201_CREATED)
        #################### END POST RELATED METHODS ####################

class NewMaintReqView(APIView):

    def post(self, request):

        new_req = {
            'resident': request.data['resident']['id'],
            'apartment_no': request.data['resident']['apartment_number'],
            'room': request.data['room']['id'],
            'item': request.data['item']['id'],
            'issue': request.data['issue']['id'],
        }

        if 'description' in request.data:
            new_req['description'] = request.data['description']
        else:
            new_req['description'] = ''
        pprint(new_req)
        serializer = NewMaintRequestSerializer(data=new_req)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            pprint(serializer.errors)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            #################### END POST RELATED METHODS ####################