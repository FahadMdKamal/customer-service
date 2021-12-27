from rest_framework.viewsets import ModelViewSet
from apps.casex.models import CaseMessage
from apps.casex.serializers import case_message_serializers


class CaseMessageAPIView(ModelViewSet):
    """
    An endpoint for CaseMessage.
    """
    serializer_class = case_message_serializers
    queryset = CaseMessage.objects.all().order_by('-id')
