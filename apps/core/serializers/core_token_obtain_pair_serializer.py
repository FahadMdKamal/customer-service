from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .user_serializers import UserSerializers


class CoreTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['user'] = UserSerializers(self.user).data
        return data
