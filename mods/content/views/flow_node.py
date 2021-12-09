import json

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import response, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from mods.content.models import Content, Flow
from mods.content.models.flow_node import FlowNode
from mods.content.models.node_config import NodeConfig
from mods.content.serializers import FlowNodeAllSerializer, IdSerializer


class FlowNodeView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                if Flow.objects.filter(id=data["flow"]).exists() is False:
                    raise ValidationError("Flow id Does not exists")

                flow_node = FlowNode.objects.filter(pk=data['id']).update(name=data['name'], flow_id=data["flow"],
                                                                          node_type=data["node_type"])
                try:
                    config = data['config']
                    if config:
                        if NodeConfig.objects.filter(flow_node_id=data["id"]).exists():
                            for key, value in data["config"].items():
                                NodeConfig.objects.filter(flow_node_id=data["id"], key=key).update(value=value)
                        else:
                            for key, value in config.items():
                                node_config = NodeConfig(flow_node_id=data["id"], key=key, value=value)
                                node_config.save()
                except:
                    pass

                return response.Response(data=data, status=status.HTTP_201_CREATED)
            except ObjectDoesNotExist:
                pass
        else:
            result = {}

            if Flow.objects.filter(id=data["flow"]).exists() is False or isinstance(data["flow"], int) is False:
                raise ValidationError("Flow id Does not exists")

            flow_node = FlowNode.objects.create(flow_id=data["flow"], node_type=data["node_type"])
            result.update({"id": flow_node.id, "flow": data["flow"], "node_type": data["node_type"]})

            try:
                content_type = data["content_type"]
                contnt = Content.objects.create(title="")
                result.update({"content_type": content_type, "content_id": contnt.id})
                flow_node.content_type = content_type
                flow_node.initial_content_id = contnt
                flow_node.save()
            except:
                pass
            return response.Response(data=result, status=status.HTTP_201_CREATED)


class NodeListView(ModelViewSet):
    serializer_class = FlowNodeAllSerializer
    queryset = FlowNode.objects.all().order_by('-id')

    def get_queryset(self):
        params = {}
        errors = []

        # if "flow_id" in list(self.request.query_params.keys()):
        #     flow_id = self.request.query_params.get("flow_id", None)
        #     if flow_id.isnumeric():
        #         if flow_id is not None:
        #             params.update({"flow_id": self.request.query_params["flow_id"]})
        #     else:
        #         errors.append({"flow_id": "flow id must be Integer"})
        # else:
        #     errors.append({"flow_id": "key name will be flow_id"})
        #
        # if "node_type" in list(self.request.query_params.keys()):
        #     if self.request.query_params.get("node_type", None) is not None:
        #         params.update({"node_type": self.request.query_params["node_type"]})
        # else:
        #     errors.append({"node_type": "key name will be node_type"})
        #
        # if len(errors) > 0:
        #     raise ValidationError(errors)

        if self.request.query_params.get("node_type", None) is not None:
            params.update({"node_type": self.request.query_params["node_type"]})

        if self.request.query_params.get("flow_id", None) is not None:
            params.update({"flow_id": self.request.query_params["flow_id"]})
        return FlowNode.objects.filter(**params).order_by('-id')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            if (len(serializer.data)) > 0:
                return self.get_paginated_response(serializer.data)
            else:
                return response.Response(status=404, data={"No Data Found"})

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


class FlowNodeDeleteView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        serializer = IdSerializer(data=request.data)
        if serializer.is_valid():
            if 'id' in data and data['id'] is not None and int(data['id']) > 0:
                try:
                    flow = FlowNode.objects.get(pk=data['id'])
                    flow.delete()
                    NodeConfig.objects.filter(flow_node_id=data['id']).delete()
                    return response.Response(status=200, data={"Flow Node deleted successfully."})
                except ObjectDoesNotExist:
                    return response.Response(status=404, data={"Flow Node not found."})

            else:
                return response.Response(status=404, data={"Flow Node not found."})
        else:
            return response.Response(status=404, data=serializer.errors)
