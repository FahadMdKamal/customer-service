from rest_framework.serializers import ModelSerializer
from .node_config_detail_serializers import NodeConfigDetailsSerializer

from mods.content.models import FlowNode


class FlowNodeDetailsSerializer(ModelSerializer):
    nodeconfigs = NodeConfigDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = FlowNode
        fields = ('id', 'name', 'flow', 'node_type', 'nodeconfigs')

