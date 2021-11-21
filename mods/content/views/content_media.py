from rest_framework.viewsets import ModelViewSet

from mods.content.models import ContentMedia
from mods.content.serializers import ContentMediaSerializer


class ContentMediaView(ModelViewSet):
    serializer_class = ContentMediaSerializer
    queryset = ContentMedia.objects.all().order_by('-id')

    def get_queryset(self):
        params = {}
        if self.request.query_params.get("media_type", None) is not None:
            params.update({"media_type": self.request.query_params["media_type"]})

        if self.request.query_params.get("public_url_byid", None) is not None:
            params.update({"id": self.request.query_params["public_url_byid"]})

        if self.request.query_params.get("status", None) is not None:
            params.update({"status": self.request.query_params["status"]})

        return ContentMedia.objects.filter(**params).order_by('-id')