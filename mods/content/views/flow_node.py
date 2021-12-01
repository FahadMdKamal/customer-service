import json

import export as export
from django.core.exceptions import ObjectDoesNotExist
from django.db.migrations import serializer
from rest_framework.views import APIView
from rest_framework import response, status
from rest_framework.viewsets import ModelViewSet

from mods.content.models import Content
from mods.content.models.flow_node import FlowNode
from mods.content.models.node_config import NodeConfig
from mods.content.serializers import FlowNodeSerializer, FlowNodeAllSerializer


class FlowNodeView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                result = {}

                flow_node = FlowNode.objects.filter(pk=data['id']).update(name=data['name'], flow_id=data["flow"],
                                                                          node_type=data["node_type"])
                try:
                    config = data['config']
                    if config:
                        if NodeConfig.objects.filter().exists():
                            for key, value in data["config"].items():
                                NodeConfig.objects.filter(flow_node=data["id"], key=key).update(value=value)
                        else:
                            for key, value in config.items():
                                node_config = NodeConfig(flow_node=flow_node, key=key, value=value)
                                node_config.save()
                except:
                    pass

                return response.Response(data=data, status=status.HTTP_201_CREATED)
            except ObjectDoesNotExist:
                pass
        else:
            result = {}
            flow_node = FlowNode.objects.create(flow_id=data["flow"], node_type=data["node_type"])
            result.update({"id": flow_node.id, "flow": data["flow"], "node_type": data["node_type"]})

            try:
                content_type = data["content_type"]
                contnt = Content.objects.create(title="")
                result.update({"content_type": content_type, "content_id": contnt.id})
            except:
                pass
            return response.Response(data=result, status=status.HTTP_201_CREATED)


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
