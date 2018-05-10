from rest_framework import serializers

from .models import Property, Floorplan

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property

        fields = ('name', 'address', 'city', 'floorplans')
        depth = 1

class FloorplanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floorplan

        fields = ('name', 'property', 'rooms', 'floorplan_image', 'stock_picture', )
        depth = 1
