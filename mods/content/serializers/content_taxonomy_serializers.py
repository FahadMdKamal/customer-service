from rest_framework.serializers import ModelSerializer

from mods.content.models import ContentTaxonomy


class ContentTaxonomySerializer(ModelSerializer):
    class Meta:
        model = ContentTaxonomy
        fields = '__all__'

