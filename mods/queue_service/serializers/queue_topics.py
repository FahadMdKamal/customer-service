from rest_framework import serializers
from mods.queue_service.models import QueueTopics


class TopicCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueTopics
        fields = "__all__"