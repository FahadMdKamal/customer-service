from rest_framework.serializers import ModelSerializer

from mods.content.models import NodeContent

class NodeContentSerializer(ModelSerializer):
    class Meta:
        model = NodeContent
        fields = ('id', 'flow_node', 'content')

