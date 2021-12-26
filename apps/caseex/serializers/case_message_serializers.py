from rest_framework import serializers
from apps.caseex.models import CaseMessage

class CaseMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CaseMessage
        fields = "__all__"#("message_type",)
