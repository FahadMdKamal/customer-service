from rest_framework.serializers import ModelSerializer

from mods.content.models import ContentData

class ContentDataSerializer(ModelSerializer):
    class Meta:
        model = ContentData
        fields = '__all__'
