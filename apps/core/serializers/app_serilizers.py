from rest_framework import serializers

from apps.core.models import Apps
from apps.core.models.channel_model import Channels
from .workgroup_serializers import WorkGroupMiniSerializers
from .channel_serializers import ChannelsMiniSerializer

class AppListSerializer(serializers.ModelSerializer):
    """
    Represent Apps and performs object's Create and Update functionality
    """

    class Meta:
        model = Apps
        fields = ('id', 
        'app_name', 
        'app_code')
    

class AppSerializer(serializers.ModelSerializer):
    """
    Represent Apps and performs object's Create and Update functionality
    """
    channels = serializers.SerializerMethodField()

    class Meta:
        model = Apps
        fields = ('id', 
        'app_name', 
        'app_code', 
        'app_domain', 
        'app_config', 
        'app_icon', 
        'status', 
        'allowed_domains',
        'channels',
        'allowed_channel_types')
    
    def get_channels(self, instance):
        objects = Channels.objects.filter(app=instance)
        return ChannelsMiniSerializer(objects, many=True).data if objects.exists() else []

    def create(self, validated_data):
        channels_data = validated_data.pop('channels')
        app = Apps.objects.create(**validated_data)

        for channel in channels_data:
            app.allowed_channel_types.add(channel)
        app.save()
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
