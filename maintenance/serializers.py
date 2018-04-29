from rest_framework import serializers

from maintenance.models import MaintenanceRequest, MaintenanceUpdate, Comment, Room, MaintenanceItem, Issue, MaintReq

class MaintenanceReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRequest

        fields = ('resident', 'date_submitted', 'category', 'description', 'staff', 'updates', 'status')
        depth = 1

class MaintenancePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRequest

        fields = ('resident', 'category', 'description', 'staff', 'apartment_no',)

class MaintenanceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceUpdate

        fields = ('staff', 'comment', 'update_type', 'request', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment

        fields = ('submitted_by', 'request', 'text', )


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room

        fields = ('name', 'id', 'items',)
        depth = 1

class MaintenanceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceItem

        fields = ('name', 'id', 'issues',)
        depth = 1

class NewMaintRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintReq


        fields = ('resident', 'apartment_no', 'room', 'item', 'issue',  )


class MaintReqReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintReq


        fields = ('resident', 'apartment_no', 'room', 'item', 'issue', 'date_submitted', 'description', 'priority', 'status', )
        depth = 1