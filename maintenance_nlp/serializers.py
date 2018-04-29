from rest_framework import serializers

# from maintenance.models import MaintenanceRequest, MaintenanceUpdate, Comment
#
# class MaintenanceReadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MaintenanceRequest
#
#         fields = ('resident', 'date_submitted', 'category', 'description', 'staff', 'updates', 'status')
#         depth = 1
#
# class MaintenancePostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MaintenanceRequest
#
#         fields = ('resident', 'category', 'description', 'staff', 'apartment_no',)
#
# class MaintenanceUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MaintenanceUpdate
#
#         fields = ('staff', 'comment', 'update_type', 'request', )
#
#
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#
#         fields = ('submitted_by', 'request', 'text', )