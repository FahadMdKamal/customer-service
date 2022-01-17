from rest_framework import serializers

from apps.mavrik_apps.models import MavrikApps, ChannelTypes
# from apps.mavrik_apps.serializers import MavrikChannelTypeSerializer


class MavrikChannelTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChannelTypes
        fields = ('id', 'channel_name',)


class MavrikAppSerializer(serializers.ModelSerializer):
    allowed_channel_types = MavrikChannelTypeSerializer(many=True)

    class Meta:
        model = MavrikApps
        fields = ('id', 'app_code', 'app_domain', 'app_config', 'app_icon', 'status', 'allowed_domains', 'allowed_channel_types')

