from django import apps
from rest_framework import serializers
from apps.core.models import MavrikApps, MaverikChannels
from mods.queue_service.models import QueueItems


class QueueItemsSerializer(serializers.ModelSerializer):
    app = serializers.SerializerMethodField()
    channel = serializers.SerializerMethodField()
    sender = serializers.SerializerMethodField()
    attending_user = serializers.SerializerMethodField()
    users = serializers.SerializerMethodField()

    class Meta:
        model = QueueItems
        # fields = '__all__'
        exclude = ['app_id']

    def get_app(self, object):
        app_obj = MaverikChannels.objects.filter(app_id=object.app_id).first()
        return {
            "app_id": app_obj.id,
            "app_name": app_obj.channel_name,
            "app_code": app_obj.app_id,


        }

    def get_channel(self, object):
        obj = MaverikChannels.objects.filter(app_id=object.app_id).first()
        return {
            "platform": obj.channel_type,
            "channel_name": obj.channel_name
        }

    def get_sender(self, object):
        return {
            "profile_pic": "pic url",
            "name": "sender name",
            "privilege": "priv"
        }

    def get_attending_user(self, object):
        return {
            "user_id": 8000,
            "name": "",
            "profile_pic": "AUN pic"

        }

    def get_users(self, object):
        return{
            "user_id": 1,
            "profile_pic": "google.com/image.png",
            "name": "John Doe",
            "online_since": "22 mins",
            "status": "working hard"
        }
