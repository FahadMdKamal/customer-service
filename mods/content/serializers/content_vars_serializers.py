from rest_framework.serializers import ModelSerializer

from mods.content.models import ContentVars

class ContentVarsSerializer(ModelSerializer):
    class Meta:
        model = ContentVars
        fields = '__all__'

