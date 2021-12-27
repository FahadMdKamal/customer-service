from rest_framework import serializers
from apps.casex.models import CaseId


class CaseIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = CaseId
        fields = "__all__"
