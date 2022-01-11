from rest_framework.serializers import ModelSerializer

from mods.content.models import NodeConfig

# Flow nodes details get serializer
class NodeConfigDetailsSerializer(ModelSerializer):
    class Meta:
        model = NodeConfig
        fields = ('id', 'flow_node', 'key', 'value')
