from rest_framework.viewsets import ModelViewSet

from mods.content.models import ContentCustomFields
from mods.content.serializers import CustomContentFieldSerializer


class ContentCustomFieldsView(ModelViewSet):
    serializer_class = CustomContentFieldSerializer
    queryset = ContentCustomFields.objects.all().order_by('-id')

    def get_queryset(self):
        params = {}
        if self.request.query_params.get("type_ref", None) is not None:
            params.update({"type_ref": self.request.query_params["type_ref"]})

        return ContentCustomFields.objects.filter(**params).order_by('-id')