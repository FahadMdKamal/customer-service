from django_mailbox.models import Mailbox
from rest_framework import serializers

from apps.core.models.workgroup import WorkGroups
from apps.core.serializers.workgroup_serializers import WorkGroupMiniSerializers

from ..models import Channels
from apps.core.utils import ChoicesFieldSerializer

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
        fields = ('id', 'channel_name')


class ChannelSerializers(serializers.ModelSerializer):
    connectivity_status = ChoicesFieldSerializer(choices= Channels.CONNECTIVITY_STATUS)
    status = ChoicesFieldSerializer(choices= Channels.STATUS)
    channel_type = ChoicesFieldSerializer(choices= Channels.CH_TYPES)
    mailbox_name = serializers.CharField(allow_blank=True, allow_null=True)
    uri = serializers.CharField(allow_blank=True, allow_null=True)
    from_email = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = Channels
        fields = "__all__"
        depth=1

    def validate(self, attrs):
        channel_type = attrs['channel_type']
        if channel_type == 'email':
            if not attrs.get('uri', None) and not attrs.get('mailbox_name', None) and not attrs.get('from_email', None):
                raise serializers.ValidationError('(mailbox_name, uri, from_email) fields are required for mail-type channel')
        return super().validate(attrs)

    def create(self, validated_data):
        mailbox_name = validated_data.pop('mailbox_name')
        uri = validated_data.pop('uri')
        from_email = validated_data.pop('from_email')

        if validated_data['channel_type'] == "email":
            mail_box = Mailbox()
            mail_box.name = mailbox_name
            mail_box.uri = uri
            mail_box.from_email = from_email
            mail_box.save()

            validated_data['mail_box'] = mail_box
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        mailbox_name = validated_data.pop('mailbox_name')
        uri = validated_data.pop('uri')
        from_email = validated_data.pop('from_email')

        if validated_data['channel_type'] == "email":
            instance.mail_box.name = mailbox_name
            instance.mail_box.uri = uri
            instance.mail_box.from_email = from_email
            instance.mail_box.save()

            validated_data['mail_box'] = instance.mail_box

        return super().update(instance, validated_data)

    
