from rest_framework.serializers import ModelSerializer

from mods.content.models import ContentText

class ContentTextSerializer(ModelSerializer):
    class Meta:
        model = ContentText
        fields = '__all__'

