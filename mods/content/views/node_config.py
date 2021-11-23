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
        flow = NodeConfig.objects.get(pk=data['id'])
        serializer = NodeConfigSerializer(flow, data=request.data)
        if serializer.is_valid():
            flow = serializer.save()
            if flow:
                return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

