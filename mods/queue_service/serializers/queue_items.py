from dataclasses import field
from django import apps
from rest_framework import serializers
from apps.core.models import MavrikApps, MaverikChannels
from mods.queue_service.models import QueueItems

class QueueItemsSerializer(serializers.ModelSerializer):
    app = serializers.SerializerMethodField()

    class Meta:
        model = QueueItems
        fields = '__all__'
    
    def get_app(self, object):
        app_obj = MaverikChannels.objects.filter(app_id=object.app_id).first()
        return {
            "app_id": app_obj.id,
            "app_name": app_obj.channel_name,
        }