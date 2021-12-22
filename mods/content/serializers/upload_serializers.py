from rest_framework.serializers import ModelSerializer

from mods.content.models import Upload


class UploadSerializer(ModelSerializer):
    class Meta:
        model = Upload
        fields = "__all__"
