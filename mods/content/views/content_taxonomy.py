from rest_framework.viewsets import ModelViewSet

from mods.content.models import ContentTaxonomy
from mods.content.serializers import ContentTaxonomySerializer


class ContentTaxonomyView(ModelViewSet):
    serializer_class = ContentTaxonomySerializer
    queryset = ContentTaxonomy.objects.all().order_by('-id')

    def get_queryset(self):
        params = {}
        if self.request.query_params.get("taxonomy_type", None) is not None:
            params.update({"taxonomy_type": self.request.query_params["taxonomy_type"]})

        if self.request.query_params.get("name", None) is not None:
            params.update({"name__icontains": self.request.query_params["name"]})

        if self.request.query_params.get("parent_id", None) is not None:
            params.update({"parent_id": self.request.query_params["parent_id"]})

        if self.request.query_params.get("taxonomy_slug", None) is not None:
            params.update({"taxonomy_slug": self.request.query_params["taxonomy_slug"]})

        return ContentTaxonomy.objects.filter(**params).order_by('-id')