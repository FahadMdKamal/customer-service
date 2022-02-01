from rest_framework import serializers
from apps.core.models import Taxonomy

class TaxonomyMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        exclude = ("created_at","updated_at","parent", "crumbs", "ref_path")


class TaxonomySerilizer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)
    children = serializers.SerializerMethodField()

    class Meta:
        model = Taxonomy
        fields = '__all__'

    def get_children(self, obj):
        taxos = Taxonomy.objects.filter(parent=obj.id)
        taxo_serilizer = TaxonomyMiniSerializer(taxos, many=True).data
        if taxos.count() > 0:
            return {"total_childs": taxos.count(), "children": taxo_serilizer}

        return {"children": 0}


class TaxonomyListSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        fields = ('id', 'name', 'taxonomy_type')
