from rest_framework import serializers
from apps.caseex.models import CaseAudience


class CaseAudienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CaseAudience
        fields = "__all__"
