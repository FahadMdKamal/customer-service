from dataclasses import field
from rest_framework import serializers
from mods.queue_service.models import QueueItems

class QueueItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueItems
        fields = '__all__'
