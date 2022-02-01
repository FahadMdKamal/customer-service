from dataclasses import field
from xml.parsers.expat import model
from rest_framework import serializers
from apps.core.models import WorkGroups, MaverikChannels

from django.contrib.auth import get_user_model


class ChannelSerializers(serializers.ModelSerializer):
    class Meta:
        model = MaverikChannels
        fields = ('channel_name', 'channel_type',)


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')


class WorkGroupSerializers(serializers.ModelSerializer):
    # user = UserSerializers(many=True)
    # channel = ChannelSerializers(many=True)

    class Meta:
        model = WorkGroups
        # fields = '__all__'
        exclude = ['user']
