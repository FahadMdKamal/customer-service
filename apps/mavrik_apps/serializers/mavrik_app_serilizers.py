from rest_framework import serializers

from apps.mavrik_apps.models import MavrikApps, ChannelTypes

class MavrikChannelTypeSerializer(serializers.ModelSerializer):
    """
    Responsible for Representing Mavrik Channel Types
    """
    class Meta:
        model = ChannelTypes
        fields = ('id', 'channel_name',)


class MavrikAppSerializer(serializers.ModelSerializer):
    """
    Represent Apps and performs object's Create and Update functionality
    """
    allowed_channel_types = MavrikChannelTypeSerializer(many=True, read_only=True)
    channels = serializers.JSONField(write_only=True)

    class Meta:
        model = MavrikApps
        fields = ('id', 
        'app_code', 
        'app_domain', 
        'app_config', 
        'app_icon', 
        'status', 
        'allowed_domains',
        'channels',
        'allowed_channel_types')

    def create(self, validated_data):
        channels_data = validated_data.pop('channels')
        app = MavrikApps.objects.create(**validated_data)

        for channel in channels_data:
            app.allowed_channel_types.add(channel)
        return app


    def update(self, instance, validated_data):
        instance.app_code = validated_data.get('app_code', instance.app_code)
        instance.app_domain = validated_data.get('app_domain', instance.app_domain)
        instance.app_config = validated_data.get('app_config', instance.app_config)
        instance.app_icon = validated_data.get('app_icon', instance.app_icon)
        instance.allowed_domains = validated_data.get('allowed_domains', instance.allowed_domains)

        if validated_data.get('channels'):
            channel_data = validated_data.pop('channels')
            if channel_data:
                instance.allowed_channel_types.clear()
                for channel in channel_data:
                    instance.allowed_channel_types.add(channel)
        instance.save()
        return instance 
