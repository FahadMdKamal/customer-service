from rest_framework import serializers
from apps.core.models import Texonomy


class TexonomySerilizer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)

    class Meta:
        model = Texonomy
        fields = ('id', 'texonomy_type', 'name', 'parent', 'details', 'slug')
