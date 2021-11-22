from rest_framework.viewsets import ModelViewSet

from mods.content.models import Flow
from mods.content.serializers import FlowSerializer


class FlowView(ModelViewSet):
    serializer_class = FlowSerializer
    queryset = Flow.objects.all().order_by('-id')