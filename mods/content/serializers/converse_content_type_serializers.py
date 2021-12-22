from rest_framework.serializers import ModelSerializer

from mods.content.models import ConverseContentType

class ConverseContentTypeSerializer(ModelSerializer):
    class Meta:
        model = ConverseContentType
        fields = '__all__'

