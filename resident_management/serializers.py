from rest_framework import serializers

from .models import ResidentProfile, User

class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentProfile

        fields = ('user', 'resident')
        depth = 1

class JustUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ('username', 'id')
        depth = 1
