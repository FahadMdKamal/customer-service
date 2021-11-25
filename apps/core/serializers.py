from rest_framework import serializers
from django.contrib.auth.models import Group, User
from apps.core.models import Texonomy


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password', 'groups')

    def create(self, validated_data):
        groups_data = validated_data.pop('groups')
        user = User.objects.create(**validated_data)

        for groupdata in groups_data:
            user.groups.add(groupdata)

        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name')


class TexonomySerilizer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)

    class Meta:
        model = Texonomy
        fields = ('texonomy_type', 'name', 'parent', 'details', 'slug')

