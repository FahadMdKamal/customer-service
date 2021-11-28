from rest_framework import serializers
from django.contrib.auth.models import Group, User

from apps.core.models import Texonomy

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

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
        fields = ('id', 'name')


class TexonomySerilizer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)

    class Meta:
        model = Texonomy
        fields = ('id', 'texonomy_type', 'name', 'parent', 'details', 'slug')


class CoreTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        groups = user.groups.all()
        serializer = GroupSerializer(groups, many=True)
        token['username'] = user.username
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['groups'] = serializer.data

        return token
