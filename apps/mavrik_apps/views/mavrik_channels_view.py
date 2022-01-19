from rest_framework.viewsets import ModelViewSet
from ..models import MaverikChannels
from ..serializers import MavrikChannelSerializers


class MavrikChannelsApiView(ModelViewSet):
    serializer_class = MavrikChannelSerializers
    queryset = MaverikChannels.objects.all()