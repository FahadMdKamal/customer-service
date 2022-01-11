from rest_framework.serializers import ModelSerializer

from mods.content.models import ContentMedia
   

class ContentMediaSerializer(ModelSerializer):
    class Meta:
        model = ContentMedia
        fields = '__all__'

