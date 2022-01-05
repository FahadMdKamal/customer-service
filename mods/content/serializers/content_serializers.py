from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from mods.content.models import Content, content


class ContentListSerializer(ModelSerializer):

    class Meta:
        model = Content
        exclude = ('parent_id',)

class ContentSerializer(ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = '__all__'

    def get_children(self, instance):

        contents = Content.objects.filter(parent_id=instance.id)

        return ContentListSerializer(contents, many=True).data

