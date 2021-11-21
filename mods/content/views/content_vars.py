from rest_framework.viewsets import ModelViewSet

from mods.content.models import ContentVars
from mods.content.serializers import ContentVarsSerializer


class ContentVarsView(ModelViewSet):
    serializer_class = ContentVarsSerializer
    queryset = ContentVars.objects.all().order_by('-id')

    def get_queryset(self):
        params = {}
        if self.request.query_params.get("var_type", None) is not None:
            params.update({"var_type__icontains": self.request.query_params["var_type"]})

        return ContentVars.objects.filter(**params).order_by('-id')