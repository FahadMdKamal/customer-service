from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from mods.content.models import (
    FlowNode,
    NodeConfig,
)


class FlowNodeSerializer(ModelSerializer):
    config = serializers.JSONField(write_only=True, default={})

    class Meta:
        model = FlowNode
        fields = ('id', 'name', 'flow', 'node_type', 'content_type', 'config')

    def create(self, validated_data):
        """
        Create and return a new `FlowNode` instance, given the validated data.
        """
        config = validated_data.pop('config')
        flow_node = FlowNode.objects.create(**validated_data)
        for key, value in config.items():
            node_config = NodeConfig(flow_node=flow_node, key=key, value=value)
            node_config.save()

        validated_data["id"] = flow_node.id
        validated_data["config"] = config
        return validated_data
