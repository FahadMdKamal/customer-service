from rest_framework import serializers
from apps.core.models import Taxonomy


class TaxonomySerilizer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)

    class Meta:
        model = Taxonomy
        fields = ('id', 'taxonomy_type', 'name', 'parent', 'details', 'slug')
