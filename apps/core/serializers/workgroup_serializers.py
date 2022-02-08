from rest_framework import serializers
from apps.core.models import WorkGroups, Channels

from django.contrib.auth import get_user_model
from apps.core.utils.choice_fields_serializer import ChoicesFieldSerializer


class ChannelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Channels
        fields = ('channel_name', 'channel_type',)


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')



class WorkGroupSerializers(serializers.ModelSerializer):
    user_role = ChoicesFieldSerializer(WorkGroups().ROLE)

    class Meta:
        model = WorkGroups
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = UserSerializers(instance.user.all(), many=True).data
        return rep

class WorkGroupMiniSerializers(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    class Meta:
        model = WorkGroups
        fields = ['id', 'name', 'user_role', 'users' ]
    
    def get_users(self, obj):
        return UserSerializers(obj.user.all(), many=True).data if isinstance(obj, WorkGroups) else []

class WorkGroupListSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkGroups
        fields = ['id', 'name', 'user_role' ]
