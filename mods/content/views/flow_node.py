from django.core.checks import messages
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import response
import json

from mods.content.models.flow_node import FlowNode
from mods.content.serializers import FlowNodeSerializer


class AddNodeView(APIView):

    def post(self, request):
        serializer = FlowNodeSerializer(data=request.data)
        if serializer.is_valid():
            flow = serializer.save()
            if flow:
                return response.Response(serializer.data)
        return response.Response(serializer.errors)


class UpdateNodeView(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                flow = FlowNode.objects.get(pk=data['id'])
                serialized_flow = FlowNodeSerializer(data=flow)

                if serialized_flow.is_valid():
                    serialized_flow.create()

                return response.Response({'message': 'flow node updated successfully', 'data': data})
            except ObjectDoesNotExist:
                pass

