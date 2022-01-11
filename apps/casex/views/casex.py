from rest_framework.viewsets import ModelViewSet
from apps.casex.models import CaseMessage
from apps.casex.serializers import CaseMessageSerializer


class CaseMessageAPIView(ModelViewSet):
    """
    An endpoint for CaseMessage.
    """
    serializer_class = CaseMessageSerializer
    queryset = CaseMessage.objects.all().order_by('-id')
