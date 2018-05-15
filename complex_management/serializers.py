from rest_framework import serializers

from .models import Property, Floorplan, FloorplanRoom

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property

        fields = ('name', 'address', 'city', 'floorplans', 'id',)
        depth = 1

class FloorplanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floorplan

        fields = ('name', 'property', 'rooms', 'floorplan_image', 'stock_picture', 'id', )
        depth = 2

class FloorplanRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorplanRoom

        fields = ('name', 'property', 'room_items', 'id', )
        depth = 1
