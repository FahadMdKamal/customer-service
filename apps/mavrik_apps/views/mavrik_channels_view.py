from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from apps.core.utils.api_response_decorator import decorate_response
from ..models import MaverikChannels
from ..serializers import MavrikChannelSerializers


class MavrikChannelsApiView(ModelViewSet):

    # def post(self, request, *args, **kwargs):
        
    #     if request.data.get('id'):
    #         db_object = MaverikChannels.objects.get(id=request.data.get('id'))
    #         serializer = MavrikChannelSerializers(db_object, data=request.data, partial=True)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return decorate_response(serializer.data, True, status.HTTP_201_CREATED, "App Updated successfully")
    #     else:
    #         serializer = MavrikChannelSerializers(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return decorate_response(serializer.data, True, status.HTTP_201_CREATED, "App Updated successfully")
    #     return decorate_response(serializer.errors, True, status.HTTP_400_BAD_REQUEST, "App Update Faild")

    allowed_methods= ("POST", "PATCH")
    serializer_class = MavrikChannelSerializers
    queryset = MaverikChannels.objects.all()