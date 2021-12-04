from rest_framework import serializers
from apps.core.models import Taxonomy


class TaxonomySerilizer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)
    child_count = serializers.SerializerMethodField()

    class Meta:
        model = Taxonomy
        fields = ('id',
                  'app_id',
                  'taxonomy_type',
                  'context',
                  'name',
                  'description',
                  'slug',
                  'crumbs',
                  'ref_path',
                  'parent',
                  'display_order',
                  'photo_url',
                  'details',
                  'status',
                  'created_at',
                  'updated_at',
                  'child_count')

    def get_child_count(self, obj):
        return Taxonomy.objects.filter(parent=obj.id).count()


class TaxonomyListSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        fields = ('id', 'name', 'taxonomy_type')
