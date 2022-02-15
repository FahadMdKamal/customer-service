from django_mailbox.models import Mailbox
from rest_framework import serializers
from apps.core.models.apps_model import Apps

from apps.core.models.workgroup import WorkGroups
from apps.core.serializers.workgroup_serializers import WorkGroupMiniSerializers

from apps.core.models import Channels
from apps.core.utils import ChoicesFieldSerializer


class MailboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailbox
        fields = '__all__'


class ChannelsMiniSerializer(serializers.ModelSerializer):

    workgroups = serializers.SerializerMethodField()

    class Meta:
        model = Channels
        fields = '__all__'

    def get_workgroups(self, instance):
        objects = WorkGroups.objects.filter(channel=instance)
        return WorkGroupMiniSerializers(objects, many=True).data if objects.exists() else []

class ChannelsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channels
        fields = ('id', 'channel_name', 'app')

class AppMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apps
        fields = ('id', 'app_name')


class ChannelSerializers(serializers.ModelSerializer):
    connectivity_status = ChoicesFieldSerializer(choices= Channels.CONNECTIVITY_STATUS)
    status = ChoicesFieldSerializer(choices= Channels.STATUS)
    channel_type = ChoicesFieldSerializer(choices= Channels.CH_TYPES)
    mail_box = serializers.SerializerMethodField()
    app_detail = serializers.SerializerMethodField()

    class Meta:
        model = Channels
        fields = "__all__"
        extra_kwargs = {
            'app': {'write_only': True}
        }
    
    def get_mail_box(self, instance):
        return MailboxSerializer(instance.mail_box).data if instance.mail_box else ""
    
    
    def get_app_detail(self, instance):
        return AppMiniSerializer(instance.app).data
    