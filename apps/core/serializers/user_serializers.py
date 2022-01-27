from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password

from apps.core.models import Profile, Organization

from .mavrik_app_serilizers import MavrikAppSerializer

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class UserProfileSerializers(serializers.ModelSerializer):
    allowed_apps = MavrikAppSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('profile_image', 'mobile', 'organization', 'allowed_apps')


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    profile = UserProfileSerializers(source='profile_data')
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password', 'groups', 'profile')

    def create(self, validated_data):
        groups_data = validated_data.pop('groups')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])

        for groupdata in groups_data:
            user.groups.add(groupdata)

        return user


class UserUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'groups')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)


    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        if validated_data.get('groups') is not None and self.user.is_admin:
            groups_data = validated_data.pop('groups')
            if groups_data:
                instance.groups.clear()
                for group in groups_data:
                    instance.groups.add(group)
        instance.save()
        return instance 


class UserProfileUpdateSerializers(serializers.ModelSerializer):
    """Update User Profile OneToOne Model Data"""
    profile = UserProfileSerializers(source='profile_data')

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'profile')

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        if validated_data.get('profile_data') is not None:
            for k, v in validated_data.get('profile_data').items():
                setattr(instance.profile_data, k, v)
            instance.profile_data.save()

        instance.save()
        return instance 
