from rest_framework.viewsets import ModelViewSet
from apps.core.models import UserAllowOrigin

from apps.core.serializers import UserAllowedOriginSerializers


class UserAllowedOriginView(ModelViewSet):
    """
    Responsible for managing user's origin data
    """

    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    serializer_class = UserAllowedOriginSerializers
    queryset = UserAllowOrigin.objects.all()
