from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .group_serializer import GroupSerializer


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
