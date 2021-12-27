from typing import OrderedDict
from rest_framework import serializers
from apps.casex.models import CaseMessage, CaseId, CaseAudience
from apps.core.utils import ChoicesFieldSerializer


class CaseMessageSerializer(serializers.ModelSerializer):
    app_id = serializers.CharField(write_only=True)
    case_id = serializers.CharField(write_only=True, required=False)
    message_type = ChoicesFieldSerializer(choices=CaseMessage.MESSAGE_TYPE)
    body_format = ChoicesFieldSerializer(choices=CaseMessage.BODY_FORMAT)

    class Meta:
        model = CaseMessage
        fields = "__all__"
        depth=1

    def create(self, validated_data):
        app_id = validated_data.pop('app_id')
        case_id = validated_data.pop('case_id', None)
        if not case_id:
            case_id = CaseId(app_id = app_id)
            case_id.save()

        case_message = CaseMessage(**validated_data)
        case_message.caseid = case_id
        case_message.save()

        if not CaseAudience.objects.filter(case_id=case_id).exists():
            case_audiance = CaseAudience(
            case_id = case_id, 
            source_message = case_message,
            )
            case_audiance.save()

        return case_message
