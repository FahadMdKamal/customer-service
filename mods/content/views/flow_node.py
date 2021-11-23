import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import response, status
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
            flow_node = FlowNode.objects.get(pk=data['id'])
            serializer = FlowNodeSerializer(flow_node, data=request.data)
            if serializer.is_valid():
                flow_node = serializer.save()
                if flow_node:
                    return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlowNodeView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                flow = FlowNode.objects.get(pk=data['id'])
                serializer = FlowNodeSerializer(flow, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                pass
        else:
            serializer = FlowNodeSerializer(data=request.data)
            if serializer.is_valid():
                flow = serializer.save()
                if flow:
                    return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)