from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import response, status
import json
from mods.content.models.node_config import NodeConfig

from mods.content.serializers import NodeConfigSerializer


class AddNodeConfigView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        serializer = NodeConfigSerializer(data=data)
        if serializer.is_valid():
            node_config = serializer.save()
            if node_config:
                return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateNodeConfigView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                flow = NodeConfig.objects.get(pk=data['id'])
                serialized_node_config = NodeConfigSerializer(data=flow)

                if serialized_node_config.is_valid():
                    serialized_node_config.create()

                return response.Response({'message': 'node config updated successfully', 'data': data})
            except ObjectDoesNotExist:
                pass
