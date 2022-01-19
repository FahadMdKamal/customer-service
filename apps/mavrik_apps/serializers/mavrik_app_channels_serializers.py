from dataclasses import field
from rest_framework import serializers

from apps.core.utils.choice_fields_serializer import ChoicesFieldSerializer

from ..models import MaverikChannels

class MavrikChannelSerializers(serializers.ModelSerializer):
    connectivity_status = ChoicesFieldSerializer(choices=MaverikChannels.CONNECTIVITY_STATUS)

    class Meta:
        model = MaverikChannels
        fields = "__all__"