from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from mods.content.models import Content


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

