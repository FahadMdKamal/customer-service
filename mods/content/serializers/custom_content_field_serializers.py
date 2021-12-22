from rest_framework.serializers import ModelSerializer

from mods.content.models import ContentCustomFields


class CustomContentFieldSerializer(ModelSerializer):
    class Meta:
        model = ContentCustomFields
        fields = '__all__'
