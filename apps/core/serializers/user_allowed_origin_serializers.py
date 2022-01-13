from rest_framework import serializers

from apps.core.models import UserAllowOrigin


class UserAllowedOriginSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserAllowOrigin
        fields = "__all__"
