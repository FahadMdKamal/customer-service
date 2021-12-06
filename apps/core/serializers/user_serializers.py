from rest_framework import serializers
from django.contrib.auth.models import Group, User
from django.contrib.auth.password_validation import validate_password


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password', 'groups')

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


    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        if validated_data.get('groups') is not None:
            groups_data = validated_data.pop('groups')
            if groups_data:
                instance.groups.clear()
                for group in groups_data:
                    instance.groups.add(group)
        instance.save()
        return instance 


class UserProfileUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
    
        instance.save()
        return instance 
