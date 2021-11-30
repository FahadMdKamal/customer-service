import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import response, status
from mods.content.models.flow_node import FlowNode
from mods.content.models.node_config import NodeConfig
from mods.content.serializers import FlowNodeSerializer


class FlowNodeView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                flow = FlowNode.objects.filter(pk=data['id']).update(name=data['name'], flow_id=data["flow"],
                                                                  node_type=data["node_type"])
                for key, value in data["config"].items():
                    NodeConfig.objects.filter(flow_node=data["id"], key=key).update(value=value)
                result = json.loads(request.body)
                return response.Response(data=result, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                pass
        else:
            serializer = FlowNodeSerializer(data=request.data)
            if serializer.is_valid():
                flow = serializer.save()
                if flow:
                    return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
