from rest_framework import serializers

from packagemanager.models import Package, Resident, Apartment

class PackageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package

        fields = ('date_received', 'recipient', 'apartment_no', 'package_type', 'status', 'id')
        depth = 1

class PackageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package

        fields = ('date_received', 'recipient', 'apartment_no', 'package_type', 'status', )

class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident

        fields = ('name', 'apartment_number', 'packages', )

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ('number', 'residents', 'packages' )
        depth = 1