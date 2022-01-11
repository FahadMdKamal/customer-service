from rest_framework.serializers import ModelSerializer

from mods.content.models import Flow

class FlowSerializer(ModelSerializer):
    class Meta:
        model = Flow
        fields = ('id', 'name', 'app_id', 'group')

    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        ret = super().to_representation(instance)
        try:
            group_name = instance.group.name
        except:
            group_name = None
        ret["group_name"] = group_name
        return ret