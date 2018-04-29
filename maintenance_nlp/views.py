# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
import csv
from pprint import pprint
import os

# Create your views here.

class MaintenanceText(APIView):

    def post(self, request):
        query = request.data['query']

        cats = []

        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)

        with open(dir_path + "/maintenance_sources/Categories.csv", 'rb') as catfile:
            cread = csv.DictReader(catfile)
            for row in cread:
                cats.append(row)

        qw = str(query).lower().split()
        pprint(qw)

        subjects = []
        categories = []
        subs = []

        for cat in cats:
            if cat['Word_1'] in qw:
                if cat['Word_2'].strip() == '-' or cat['Word_2'].strip() in qw:
                    s_obj = {
                        'phrase': cat['Phrase'],
                        'category': cat['Category']
                    }
                    subjects.append(s_obj)
                    if cat['Category'] not in categories:
                        categories.append(cat['Category'])
                    if cat['Phrase'] not in subs:
                        subs.append(cat['Phrase'])


        data = {
            'data': subjects,
            'categories': ", ".join(categories),
            'subjects': ", ".join(subs)
        }


        return Response(data)