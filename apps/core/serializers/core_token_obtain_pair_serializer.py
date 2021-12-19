from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .group_serializer import GroupSerializer
from .user_serializers import UserProfileSerializers, UserSerializers


class CoreTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['user'] = UserSerializers(self.user).data
        data['profile'] = UserProfileSerializers(self.user.profile).data
        return data

    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)

    #     groups = user.groups.all()
    #     serializer = GroupSerializer(groups, many=True)

    #     token['username'] = user.username
    #     token['email'] = user.email
    #     token['first_name'] = user.first_name
    #     token['last_name'] = user.last_name
    #     token['groups'] = serializer.data
    #     return token
