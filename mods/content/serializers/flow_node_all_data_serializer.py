from rest_framework.serializers import ModelSerializer
from .node_config_serializers import NodeConfigSerializer

from mods.content.models import (
    Content,
    FlowNode,
)

class FlowNodeAllDataSerializer(ModelSerializer):
    config = NodeConfigSerializer(many=True)

    class Meta:
        model = FlowNode
        fields = ('id', 'name', 'flow', 'node_type', "config", "content_type", "initial_content_id")
        depths = -1

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if ret["node_type"] == "start":
            ret.pop("content_type")
            ret.pop("initial_content_id")
        try:
            from django.core import serializers
            qs = list(Content.objects.filter(id=ret["initial_content_id"]).values())
            content = qs
        except:
            content = None

        ret["content"] = content
        return ret
