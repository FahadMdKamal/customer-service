import json
from django.core.exceptions import ObjectDoesNotExist
from django.db.migrations import serializer
from rest_framework.views import APIView
from rest_framework import response, status
from rest_framework.viewsets import ModelViewSet

from mods.content.models.flow_node import FlowNode
from mods.content.models.node_config import NodeConfig
from mods.content.serializers import FlowNodeSerializer, FlowNodeAllSerializer


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
                    serializer.data["config"] = request.data["config"]
                    return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NodeListView(ModelViewSet):
    serializer_class = FlowNodeAllSerializer
    queryset = FlowNode.objects.all().order_by('-id')

    def get_queryset(self):
        params = {}
        if self.request.query_params.get("flow_id", None) is not None:
            params.update({"flow_id": self.request.query_params["flow_id"]})
        if self.request.query_params.get("node_type", None) is not None:
            params.update({"node_type": self.request.query_params["node_type"]})

        return FlowNode.objects.filter(**params).order_by('-id')


class FlowNodeDeleteView(APIView):
    def post(self, request):
        id = request.data["id"]
        FlowNode.objects.filter(id=id).delete()
        NodeConfig.objects.filter(flow_node_id=id).delete()

        return response.Response(data="success", status=status.HTTP_200_OK)
