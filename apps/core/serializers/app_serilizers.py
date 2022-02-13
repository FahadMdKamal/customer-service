from rest_framework import serializers

from apps.core.models import Apps
from apps.core.models.channel_model import Channels
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
