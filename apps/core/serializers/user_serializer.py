from rest_framework import serializers
from django.contrib.auth.models import Group, User


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
