# from rest_framework import serializers
# from apps.core.models import MavrikApps, MaverikChannels

from rest_framework.response import Response
from rest_framework.views import APIView
from mods.queue_service.models import QueueItems
from apps.social.serializers import QueueItemsSerializer


class QueueItemList(APIView):

    serializer_class = QueueItemsSerializer

    def get(self, request, *args, **kwargs):
        params = {}

        if self.request.query_params.get("app-id", None) is not None:
            params.update({"id": self.request.query_params["app-id"]})

        qitms = QueueItems.objects.filter(**params).all()
        qitm_sr = QueueItemsSerializer(qitms, many=True).data
        return Response({'messages': qitm_sr})
