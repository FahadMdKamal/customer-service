from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class PasswordResetSerializer(serializers.Serializer):

    email = serializers.EmailField()

    class Meta:
        fields = ('email',)


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField( min_length=6, max_length=68, write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField( min_length=6, max_length=68, write_only=True, required=True)
    uidb64 = serializers.CharField()
    token = serializers.CharField()
  
    class Meta:
        fields = ['password','password2', 'uidb64', 'token']

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords didn't matched.")
        return data
        