from rest_framework import serializers

from mods.webhook.models import Webhooks


class CaptureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webhooks
        fields = "__all__"
