from rest_framework.serializers import ModelSerializer

from mods.content.models import Upload


class UploadDetailSerializer(ModelSerializer):
    class Meta:
        model = Upload
        fields = "__all__"

class UploadShortSerializer(ModelSerializer):
    class Meta:
        model = Upload
        fields = ('app_id', 'owner', 'filepath', 'secure_url')
