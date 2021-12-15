from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    confirm_new_password= serializers.CharField(required=True)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def validate(self, data):
        new_password = data.get('new_password')
        confirm_new_password = data.get('confirm_new_password')
        user = self.user
        if new_password != confirm_new_password:
            raise serializers.ValidationError("Both Passwords didn't matched")
        data['user'] = user
        return data
    
    def validate_old_password(self, data):
        user = self.user
        if not user.check_password(data):
            raise serializers.ValidationError("Invalid Old Password.")
        return data
