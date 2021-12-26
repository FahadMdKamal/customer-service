from rest_framework import serializers
from apps.caseex.models import CaseId


class CaseIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = CaseId
        fields = "__all__"
