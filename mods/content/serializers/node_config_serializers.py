from rest_framework.serializers import ModelSerializer

from mods.content.models import NodeConfig


class NodeConfigSerializer(ModelSerializer):
    class Meta:
        model = NodeConfig
        fields = ('id', 'flow_node', 'key', 'value')

    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        ret = super().to_representation(instance)
        name = ret["key"]
        value = ret["value"]
        ret[name] = value
        ret.pop("key")
        ret.pop("value")
        ret.pop("id")
        ret.pop("flow_node")
        return ret

