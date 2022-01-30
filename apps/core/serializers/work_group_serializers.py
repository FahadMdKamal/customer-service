from xml.parsers.expat import model
from rest_framework import serializers
from apps.core.models import WorkGroups


class WorkGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkGroups
        fields = '__all__'
