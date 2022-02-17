from rest_framework import serializers
from apps.core.models import Taxonomy
# from apps.core.utils.extract_object_childrens import ExtractModelChildren

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
        db_obj = Taxonomy.objects.filter(parent=obj)
        return TaxonomyMiniSerializer(db_obj, many=True).data


        # extractor = ExtractModelChildren(Taxonomy)
        # return extractor.extract_serialized_children(db_obj.first(), TaxonomyMiniSerializer) if db_obj else None



    # def get_children(self, obj):
    #     db_obj = list(Taxonomy.objects.filter(parent__id=obj.id))

    #     for d in db_obj:
    #         ne_ch = Taxonomy.objects.filter(parent=d)
    #         if ne_ch:
    #             db_obj.append(ne_ch)

    #     return TaxonomyMiniSerializer(db_obj, many=True).data
class TaxonomyListSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        fields = ('id', 'name', 'taxonomy_type')
