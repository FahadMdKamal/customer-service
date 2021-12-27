from rest_framework.viewsets import ModelViewSet
from apps.caseex.serializers import CaseMessageSerializer
from apps.caseex.models import CaseMessage


class CaseMessageAPIView(ModelViewSet):
    """
    An endpoint for CaseMessage.
    """
    serializer_class = CaseMessageSerializer
    queryset = CaseMessage.objects.all().order_by('-id')
