from rest_framework import serializers
from apps.core.models import Taxonomy
from apps.core.utils.extract_object_childrens import ExtractModelChildren

class TaxonomyMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        exclude = ("created_at","updated_at", "crumbs", "ref_path",)


class TaxonomySerilizer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)
    children = serializers.SerializerMethodField()

    class Meta:
        model = Taxonomy
        fields = '__all__'
    

    def get_children(self, obj):
        db_obj = Taxonomy.objects.filter(parent=obj.id)
        extractor = ExtractModelChildren(Taxonomy)
        return extractor.extract_serialized_children(db_obj.first(), TaxonomyMiniSerializer)


class TaxonomyListSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        fields = ('id', 'name', 'taxonomy_type')
