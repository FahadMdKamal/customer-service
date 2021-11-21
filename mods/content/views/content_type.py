from rest_framework.viewsets import ModelViewSet

from mods.content.models import ConverseContentType
from mods.content.serializers import ConverseContentTypeSerializer


class ConverseContentTypeView(ModelViewSet):
    serializer_class = ConverseContentTypeSerializer
    queryset = ConverseContentType.objects.all().order_by('-id')

    def get_queryset(self):
        params = {}
        if self.request.query_params.get("type_ref", None) is not None:
            params.update({"type_ref": self.request.query_params["type_ref"]})

        if self.request.query_params.get("type_name", None) is not None:
            params.update({"type_name__icontains": self.request.query_params["type_name"]})

        return ConverseContentType.objects.filter(**params).order_by('-id')
