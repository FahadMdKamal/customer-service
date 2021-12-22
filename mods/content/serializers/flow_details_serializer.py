from rest_framework.serializers import ModelSerializer
from .flow_node_detail_serializers import FlowNodeDetailsSerializer

from mods.content.models import Flow


class FlowDetailsSerializer(ModelSerializer):
    # flownodes = serializers.StringRelatedField(many=True)
    flownodes = FlowNodeDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Flow
        fields = ("id", "name", "app_id", "group", "flownodes")
        depths = 1
