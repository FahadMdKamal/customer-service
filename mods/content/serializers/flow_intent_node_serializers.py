from rest_framework.serializers import ModelSerializer
from .flow_node_all_data_serializer import FlowNodeAllDataSerializer

from mods.content.models import Flow


class FlowIntentNodeSerializer(ModelSerializer):
    flownodes = FlowNodeAllDataSerializer(many=True, read_only=True)
    class Meta:
        model = Flow
        fields = ("id", "name", "app_id", "group", "flownodes")
        depths = 1