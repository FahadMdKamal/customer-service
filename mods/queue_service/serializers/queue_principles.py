from rest_framework import serializers
from mods.queue_service.models import QueuePrinciples


class QueuePrinciplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueuePrinciples
        fields = "__all__"