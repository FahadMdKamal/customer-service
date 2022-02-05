from rest_framework.serializers import ModelSerializer
from .node_config_serializers import NodeConfigSerializer

from mods.content.models import FlowNode

class FlowNodeAllSerializer(ModelSerializer):
    # mevrik = NodeConfigSerializer(many=True)
    config = NodeConfigSerializer(many=True)

    class Meta:
        model = FlowNode
        fields = ('id', 'name', 'flow', 'node_type', "mevrik", "content_type", "initial_content_id")
        depths = -1

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if ret["node_type"] == "start":
            ret.pop("content_type")
            ret.pop("initial_content_id")

        return ret

