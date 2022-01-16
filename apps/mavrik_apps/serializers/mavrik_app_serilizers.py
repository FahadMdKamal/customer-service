from rest_framework import serializers

from apps.mavrik_apps.models import MavrikApps, ChannelTypes
from apps.core.utils import ChoicesFieldSerializer

class MavrikAppSerializer(serializers.ModelSerializer):

    class Meta:
        model = MavrikApps
        fields = '__all__'
        depth=1

    # def create(self, validated_data):
    #     # channels = validated_data.pop('channels')

    #     # validated_data['allowed_channel_types'] = channels
    #     # print(channels)
    #     return super().create(validated_data)