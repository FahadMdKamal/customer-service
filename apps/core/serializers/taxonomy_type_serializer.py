from rest_framework import serializers
from apps.core.models import TaxonomyType


class TaxonomyTypeSerilizer(serializers.ModelSerializer):

    class Meta:
        model = TaxonomyType
        fields = "__all__"
