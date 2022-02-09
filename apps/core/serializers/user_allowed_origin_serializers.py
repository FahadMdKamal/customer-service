from rest_framework import serializers

from apps.core.models import UserAllowOrigin


class UserAllowedOriginSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserAllowOrigin
        fields = "__all__"
    
    def validate_user(self, value):
        """
        Check that the blog post is about Django.
        """
        if not value:
            raise serializers.ValidationError("Related User Id is required")
        return value
